import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
import susi
from sklearn.model_selection import KFold
from susi.SOMPlots import plot_umatrix, plot_estimation_map
import random 
from matplotlib import pyplot as plt
# from sklearn.cross_validation import KFold


f = open("median_feature_vector_splitted.json", "r")
js = json.load(f)

mapping = {"17EC10060":0, "17EC10064":1, "17EC35017":2, "17EC35041":3, "17EC35033":4, "17EC10005":5, "17EC35024":6, "17EC35026":7, "17EC35043":8}

feat = []
labels = []
for files in js:
    fl = js[files]
    for rolls in fl:
        feat.append(fl[rolls])
        labels.append(mapping[rolls])

feat = np.array(feat)
labels = np.array(labels)

print(feat.shape)
print(labels.shape)

np.savez_compressed("features.npz", feat=feat)
np.savez_compressed("labels.npz", labels=labels)



data = np.load("features.npz", allow_pickle=True)
labels = np.load("labels.npz", allow_pickle=True)
data = data['feat']
target = labels['labels']
data_class = {}

# for i in range (data.shape[0]):  # uncomment for balancing dataset
# 	try:
# 		data_class[target[i]].append(data[i])
# 	except:
# 		data_class[target[i]] = []
# 		data_class[target[i]].append(data[i])

# for i in range (100):
# 	for key in list(data_class.keys()):
# 		if (len(data_class[key])) < 10:
# 			average = np.zeros(data_class[key][0].shape)
# 			for vec in data_class[key]:
# 				average+=vec
# 			average/=len(data_class[key])
# 			data_class[key].append(average)

# data_list = []

# for key in list(data_class.keys()):
# 	for i in range (len(data_class[key])):
# 		data_list.append([data_class[key][i],key])

# random.shuffle(data_list)

# data = [x[0] for x in data_list ]
# target = [x[1] for x in data_list ]

data = np.array(data)
target = np.array(target)

for i in range (target.shape[0]): # uncomment to test for multiclass 
	if target[i]<=4:
		target[i] = 0
	else:
		target[i] = 1
# cnts = np.zeros(9)
# for i in range (data.shape[0]):
# 	cnts[target[i]]+=1

# print (cnts)
# plt.hist(target, bins=9)  # `density=False` would make counts
# plt.ylabel('Data Points')
# plt.xlabel('Classes')
# plt.show()





X = data
y = target

# print (X.shape[0])
kf = KFold(n_splits=5)
som = susi.SOMClassifier(
    n_rows = 50, 
    n_columns = 50,
    n_iter_unsupervised=10000,
    n_iter_supervised=5000,
    random_state=42,
)

k_fold_score = 0
index  = 1
for train_index, test_index in kf.split(data):
	X_train, X_test = X[train_index], X[test_index]
	y_train, y_test = y[train_index], y[test_index]
	data = X_train
	target = y_train
	data_class = {}
	




	# print (X_train.shape,X_test.shape,y_train.shape,y_test.shape)
	print ("Running on fold ", index)
	som.fit(X_train, y_train)
	y_pred = som.predict(X_test)
	# print (y_pred,y_test)
	accuracy_score = som.score(X_test, y_test)
	print("Accuracy on fold ", index, accuracy_score)
	k_fold_score+=accuracy_score
	index+=1

print ("Final accuracy", k_fold_score/5)




# split_size = data.shape[0]//5 + 1
# for i in range (5):
# 	test_set = 

# X_train, X_test, y_train, y_test = train_test_split(data, target, test_size = 0.2)
# print (X_train.shape)
# print (X_test.shape)


