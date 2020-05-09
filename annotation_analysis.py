num_ordered, num_unordered = 0, 0

with open('/scratch/lyuqing-zharry/wikihow_probing/data/wikihow_data/new/ordering_annotation/1000.csv') as fr:
    lines = fr.readlines()
    for line in lines[1:]:
        tokens = line.split(",")
       	if int(tokens[-1]) == 1:
            num_ordered += 1
        else:
            num_unordered += 1

print(num_ordered, num_unordered)
