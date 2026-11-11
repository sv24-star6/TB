import zipfile,io,json
from pathlib import Path
import numpy as np,pandas as pd,cv2,torch
from torch import nn
from torch.utils.data import TensorDataset,DataLoader
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import confusion_matrix,roc_auc_score,accuracy_score,balanced_accuracy_score,recall_score
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path('results');ROOT.mkdir(exist_ok=True);torch.set_num_threads(2)
with zipfile.ZipFile('dataset.zip') as z:
 d=pd.read_csv(io.BytesIO(z.read('jaypee_metadata.csv')))
 lookup={Path(x).name:x for x in z.namelist() if x.endswith('.jpg')}
 a=[]
 for n in d.study_id:
  im=cv2.imdecode(np.frombuffer(z.read(lookup[n]),np.uint8),cv2.IMREAD_GRAYSCALE)
  im=cv2.resize(im,(96,96),interpolation=cv2.INTER_AREA);a.append(im)
X=torch.from_numpy(np.array(a,dtype='float32')[:,None]/255.)
y=(d.findings=='Tuberculosis').astype(int).to_numpy()
class Net(nn.Module):
 def __init__(self):
  super().__init__()
  self.features=nn.Sequential(nn.Conv2d(1,16,3,padding=1),nn.ReLU(),nn.MaxPool2d(2),nn.Conv2d(16,32,3,padding=1),nn.ReLU(),nn.MaxPool2d(2),nn.Conv2d(32,64,3,padding=1),nn.ReLU())
  self.head=nn.Sequential(nn.AdaptiveAvgPool2d(1),nn.Flatten(),nn.Linear(64,1))
 def forward(self,x):return self.head(self.features(x)).squeeze(1)
pred=np.zeros(len(y));oof_fold=np.zeros(len(y),dtype=int);last=None
for fold,(tr,te) in enumerate(StratifiedKFold(n_splits=5,shuffle=True,random_state=42).split(np.zeros(len(y)),y),1):
 torch.manual_seed(100+fold);model=Net()
 optimizer=torch.optim.Adam(model.parameters(),lr=.001);criterion=nn.BCEWithLogitsLoss()
 loader=DataLoader(TensorDataset(X[tr],torch.from_numpy(y[tr].astype('float32'))),batch_size=16,shuffle=True)
 for epoch in range(12):
  model.train()
  for xx,yy in loader:
   optimizer.zero_grad();loss=criterion(model(xx),yy);loss.backward();optimizer.step()
 model.eval()
 with torch.no_grad():pred[te]=torch.sigmoid(model(X[te])).numpy()
 oof_fold[te]=fold;last=model
 print('fold',fold,'complete',flush=True)
yp=(pred>=.5).astype(int);cm=confusion_matrix(y,yp)
metrics={'model':'small CNN 3 convolution layers, 12 epochs per fold, randomly initialized','n':len(y),'evaluation':'5-fold stratified out-of-fold, no hyperparameter search','accuracy':float(accuracy_score(y,yp)),'balanced_accuracy':float(balanced_accuracy_score(y,yp)),'auroc':float(roc_auc_score(y,pred)),'sensitivity':float(recall_score(y,yp)),'specificity':float(recall_score(1-y,1-yp)),'TN_FP_FN_TP':[int(cm[0,0]),int(cm[0,1]),int(cm[1,0]),int(cm[1,1])]}
d['fold']=oof_fold;d['reference_tb']=y;d['cnn_oof_probability_tb']=pred;d['cnn_prediction_tb']=yp
d['result']=np.where((y==1)&(yp==0),'FN',np.where((y==0)&(yp==1),'FP',np.where(y==1,'TP','TN')))
d.to_csv(ROOT/'cnn_oof_predictions.csv',index=False)
indices=np.where(oof_fold==5)[0];pick=[]
for cat in ['FN','FP','TP','TN']:
 ix=[i for i in indices if d.iloc[i].result==cat]
 if ix:pick.append(ix[0])
fig,axes=plt.subplots(len(pick),3,figsize=(9,3*len(pick)),squeeze=False)
for row,i in enumerate(pick):
 model=last;model.eval();acts=[];grads=[]
 def forward_hook(mod,inp,out):acts.append(out)
 def backward_hook(mod,gin,gout):grads.append(gout[0])
 h1=model.features[6].register_forward_hook(forward_hook)
 h2=model.features[6].register_full_backward_hook(backward_hook)
 model.zero_grad();score=model(X[i:i+1]);score.backward();h1.remove();h2.remove()
 weights=grads[0].mean(dim=(2,3),keepdim=True)
 cam=torch.relu((weights*acts[0]).sum(1))[0].detach().numpy()
 cam=cv2.resize(cam,(96,96));cam=(cam-cam.min())/(np.ptp(cam)+1e-8)
 img=X[i,0].numpy();overlay=cv2.applyColorMap(np.uint8(cam*255),cv2.COLORMAP_JET)
 overlay=cv2.cvtColor(overlay,cv2.COLOR_BGR2RGB)/255.
 overlay=.6*np.stack([img]*3,axis=-1)+.4*overlay
 axes[row,0].imshow(img,cmap='gray');axes[row,0].set_title(f'{d.iloc[i].study_id} | {d.iloc[i].result}')
 axes[row,1].imshow(cam,cmap='inferno');axes[row,1].set_title('Grad-CAM (TB logit)')
 axes[row,2].imshow(np.clip(overlay,0,1));axes[row,2].set_title(f'TB score {pred[i]:.2f}')
 for ax in axes[row]:ax.axis('off')
fig.suptitle('Held-out fold 5 Grad-CAM examples (pilot, not clinical validation)')
fig.tight_layout();fig.savefig(ROOT/'cnn_gradcam_examples.png',dpi=150);plt.close(fig)
(ROOT/'cnn_metrics.json').write_text(json.dumps(metrics,indent=2))
print(json.dumps(metrics,indent=2))
