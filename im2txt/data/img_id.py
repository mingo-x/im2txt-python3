from os import listdir
import pickle

name_set = set()
trains = listdir("./data/raw-data/train2014-first2000")
for t in trains:
	name_set.add(t)
tests = listdir("./data/raw-data/val2014-first1000")
for t in tests:
	name_set.add(t)
print(len(name_set))
pickle.dump(name_set,open("./data/pic_name_set.p","wb"))