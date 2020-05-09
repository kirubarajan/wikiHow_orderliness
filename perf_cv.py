import csv
import statistics
from sklearn.metrics import precision_recall_fscore_support

split_num = 5

pres = []
recs = []
f1s = []
for i in range(split_num):
  with open('/scratch/lyuqing-zharry/wikihow_probing/output_dir/new/order_manual_{}_roberta/model_pred_false.csv'.format(i)) as fr:
    reader = csv.DictReader(fr)
    y_pred = []
    y_true = []
    for row in reader:
      y_pred.append(row['pred'])
      y_true.append(row['gold'])
  pre, rec, f1, sup = precision_recall_fscore_support(y_true, y_pred)
  pres.append(pre[1])
  recs.append(rec[1])
  f1s.append(f1[1])
print(statistics.mean(pres))
print(statistics.mean(recs))
print(statistics.mean(f1s))

