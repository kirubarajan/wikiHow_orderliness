import pandas as pd
from sklearn.model_selection import KFold
import sys
import os

data_path = "/scratch/lyuqing-zharry/wikihow_probing/data/wikihow_data/new/csv_dir/order_ablation/" + sys.argv[1] + "/1000.csv"           

save_path = "/scratch/lyuqing-zharry/wikihow_probing/data/wikihow_data/new/csv_dir/order_ablation/" + sys.argv[1] + "/"


n_splits = 5

data = pd.read_csv(data_path)

kf = KFold(n_splits=n_splits)
kf.get_n_splits(data)

for i,(train_index, test_index) in enumerate(kf.split(data)):
    data_train = data.iloc[train_index]
    data_test = data.iloc[test_index]
    if not os.path.exists(save_path + "cv_" + str(i)):
        os.makedirs(save_path + "cv_" + str(i))
    data_train.to_csv(save_path + "cv_" + str(i) + "/" + "train.csv",index=False)
    data_test.to_csv(save_path + "cv_" + str(i) + "/" + "val.csv", index=False)
