import random
import os

train_size = 800
val_size = 200
limit_train_size = 400

splits = []

with open('/scratch/lyuqing-zharry/wikihow_probing/data/wikihow_data/new/ordering_annotation/1000.csv') as fr:
  lines = fr.readlines()
header = lines[0]
lines = lines[1:]
random.shuffle(lines)
for i in range(0,train_size+val_size,val_size):
  splits.append(lines[i:i+val_size])
split_num = int((train_size+val_size)/val_size)
for i in range(split_num):
  path = '/scratch/lyuqing-zharry/wikihow_probing/data/wikihow_data/new/csv_dir/order_manual_{}/'.format(i)
  if not os.path.exists(path):
    os.makedirs(path)
  with open(path + 'train.csv', 'w') as ft, open(path + 'val.csv', 'w') as fv:
    val_set = splits[i]
    train_set = []
    for j in range(split_num):
      if j != i:
        train_set += splits[j]
    assert(len(val_set) == val_size)
    assert(len(train_set) == train_size)
    random.shuffle(val_set)
    random.shuffle(train_set)
    if limit_train_size > 0:
      train_set = train_set[:limit_train_size]
    ft.write(''.join([header] + train_set))
    fv.write(''.join([header] + val_set))
