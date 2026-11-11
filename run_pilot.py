import io,zipfile,hashlib,json
from pathlib import Path
import numpy as np,pandas as pd,cv2
from sklearn.model_selection import StratifiedKFold,cross_val_predict
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score,balanced_accuracy_score,accuracy_score,recall_score,confusion_matrix,roc_curve
from skimage.feature import hog,graycomatrix,graycoprops
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
SRC=Path('dataset.zip');OUT=Path('results');OUT.mkdir(exist_ok=True)
with zipfile.ZipFile(SRC) as z:
 meta=pd.read_csv(io.BytesIO(z.read('jaypee_metadata.csv')))
 print('raw labels',meta.findings.value_counts().to_dict(),flush=True)
 lookup={Path(n).name:n for n in z.namelist() if n.lower().endswith('.jpg')}
 hashes=[];shapes=[];features=[]
 for name in meta.study_id:
  raw=z.read(lookup[name]);hashes.append(hashlib.sha256(raw).hexdigest());im=cv2.imdecode(np.frombuffer(raw,np.uint8),cv2.IMREAD_GRAYSCALE)
  if im is None:raise ValueError(name)
  shapes.append(im.shape);im=cv2.resize(im,(128,128),interpolation=cv2.INTER_AREA)
  h=hog(im,pixels_per_cell=(16,16),cells_per_block=(2,2),orientations=9,feature_vector=True)
  hist=cv2.calcHist([im],[0],None,[16],[0,256]).flatten();hist/=hist.sum()
  glcm=graycomatrix((im//16).astype('uint8'),distances=[1,3],angles=[0,np.pi/2],levels=16,symmetric=True,normed=True)
  gl=[graycoprops(glcm,p).mean() for p in ['contrast','homogeneity','energy','correlation']]
  features.append(np.r_[h,hist,gl,float(im.mean()),float(im.std())])
X=np.asarray(features);y=meta.findings.astype(str).str.lower().isin(['true','1','tb','positive','tuberculosis']).astype(int).to_numpy()
assert y.sum()>0 and y.sum()<len(y)
cv=StratifiedKFold(n_splits=5,shuffle=True,random_state=42)
model=make_pipeline(StandardScaler(),LogisticRegression(C=.01,max_iter=2000,class_weight='balanced',random_state=42))
prob=cross_val_predict(model,X,y,cv=cv,method='predict_proba')[:,1];pred=(prob>=.5).astype(int)
cm=confusion_matrix(y,pred)
metrics={'n':len(y),'tb':int(y.sum()),'non_tb':int((1-y).sum()),'exact_duplicate_files':len(hashes)-len(set(hashes)),'unique_image_sizes':len(set(shapes)),'image_size_range':{'min_height':int(min(s[0] for s in shapes)),'max_height':int(max(s[0] for s in shapes)),'min_width':int(min(s[1] for s in shapes)),'max_width':int(max(s[1] for s in shapes))},'model':'HOG + histogram + GLCM + logistic regression','evaluation':'5-fold stratified out-of-fold prediction, fixed hyperparameters','accuracy':accuracy_score(y,pred),'balanced_accuracy':balanced_accuracy_score(y,pred),'auroc':roc_auc_score(y,prob),'tb_sensitivity':recall_score(y,pred),'non_tb_specificity':recall_score(1-y,1-pred),'confusion_matrix_TN_FP_FN_TP':[int(cm[0,0]),int(cm[0,1]),int(cm[1,0]),int(cm[1,1])]}
rng=np.random.default_rng(42);vals=[]
for i in range(2000):
 ids=rng.integers(0,len(y),len(y))
 if len(np.unique(y[ids]))==2:vals.append(roc_auc_score(y[ids],prob[ids]))
metrics['auroc_bootstrap_95pct_percentile_CI']=[float(v) for v in np.percentile(vals,[2.5,97.5])]
meta['label_tb']=y;meta['oof_probability_tb']=prob;meta['oof_prediction_tb']=pred
meta['result']=np.where((y==1)&(pred==0),'FN',np.where((y==0)&(pred==1),'FP',np.where(y==1,'TP','TN')))
meta.to_csv(OUT/'out_of_fold_predictions.csv',index=False)
(OUT/'metrics.json').write_text(json.dumps(metrics,indent=2))
fig,axs=plt.subplots(1,2,figsize=(10,4));axs[0].imshow(cm,cmap='Blues')
axs[0].set_xticks([0,1],['Non-TB','TB']);axs[0].set_yticks([0,1],['Non-TB','TB'])
axs[0].set_xlabel('Predicted');axs[0].set_ylabel('Reference label');axs[0].set_title('5-fold out-of-fold confusion matrix')
for i in range(2):
 for j in range(2):axs[0].text(j,i,str(cm[i,j]),ha='center',va='center',fontsize=15)
fpr,tpr,_=roc_curve(y,prob);axs[1].plot(fpr,tpr,label=f'AUROC {metrics["auroc"]:.3f}')
axs[1].plot([0,1],[0,1],'--',color='gray')
axs[1].set(xlabel='False-positive rate',ylabel='True-positive rate',title='Out-of-fold ROC')
axs[1].legend();fig.tight_layout();fig.savefig(OUT/'pilot_metrics.png',dpi=160);plt.close(fig)
review=[]
for category in ['FN','FP','TP','TN']:
 sub=meta[meta.result==category].copy();sub['uncertainty']=abs(sub.oof_probability_tb-.5);review.append(sub.sort_values('uncertainty').head(15))
review=pd.concat(review)
review[['study_id','result','oof_probability_tb']].assign(radiologist_blinded_label='',radiologist_comments='').to_csv(OUT/'radiologist_review_template.csv',index=False)
print(json.dumps(metrics,indent=2),flush=True)
