from pathlib import Path
import pandas as pd,numpy as np,json
from sklearn.metrics import roc_auc_score
from scipy.stats import binomtest
root=Path(__file__).parent/'results'
a=pd.read_csv(root/'out_of_fold_predictions.csv').set_index('study_id')
b=pd.read_csv(root/'cnn_oof_predictions.csv').set_index('study_id')
assert a.index.is_unique and b.index.is_unique and set(a.index)==set(b.index)
b=b.loc[a.index];y=a.label_tb.to_numpy()
assert np.array_equal(y,b.reference_tb.to_numpy())
p=a.oof_prediction_tb.to_numpy();q=b.cnn_prediction_tb.to_numpy()
pa=a.oof_probability_tb.to_numpy();pb=b.cnn_oof_probability_tb.to_numpy()
ca=(p==y);cb=(q==y);n10=int((ca&~cb).sum());n01=int((~ca&cb).sum())
rs=np.random.default_rng(2026);delta=[]
for _ in range(5000):
 idx=rs.integers(0,len(y),len(y))
 if len(set(y[idx]))==2:
  delta.append(roc_auc_score(y[idx],pa[idx])-roc_auc_score(y[idx],pb[idx]))
report={'n':len(y),'both_correct':int((ca&cb).sum()),'both_wrong':int((~ca&~cb).sum()),'feature_correct_cnn_wrong':n10,'cnn_correct_feature_wrong':n01,'mcnemar_exact_two_sided_p':binomtest(min(n10,n01),n10+n01,.5).pvalue,'auroc_difference_feature_minus_cnn':float(roc_auc_score(y,pa)-roc_auc_score(y,pb)),'auroc_difference_bootstrap_95pct_CI':[float(z) for z in np.percentile(delta,[2.5,97.5])],'both_miss_TB':int(((p==0)&(q==0)&(y==1)).sum()),'both_false_alarm_non_TB':int(((p==1)&(q==1)&(y==0)).sum())}
root.mkdir(exist_ok=True)
(root/'model_comparison.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
