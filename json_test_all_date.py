import json
import jsondiff
import natsort

from os import listdir
from os.path import isfile, join
#
# with open('output/0.json') as f:
#     json1 = json.load(f)
#     #print(json1)
# with open('tests/0.json') as f:
#     json2 = json.load(f)
#     #print(json2)
#
# res = jsondiff.diff(json1, json2)
# print(len(json1["DateIntervals"])-1)
# print(len(res))
#
# if res:
#     print("Diff found")
# else:
#     print("Same")


def accuracy(pred_json, true_json):
    with open(pred_json) as f:
        json1 = json.load(f)

    with open(true_json) as f:
        json2 = json.load(f)

    res = jsondiff.diff(json1, json2)
    all = len(json2["DateIntervals"]) - 1
    false = len(res)
    acc = (all - false)/all
    return acc


files = [f for f in listdir('output')]
sorted_files = natsort.natsorted(files)
all_acc = []

for file in sorted_files:

    try:
        acc = accuracy('output/'+file, 'tests/'+file)
        if acc != 1:
            print("In file ",file, "accuracy ",  acc)
        all_acc.append(acc)
    except:
        print("FileName: ", file)
        print("ERROR")
sum = 0
for i in all_acc:

    sum = sum + i
print(sum/len(files))