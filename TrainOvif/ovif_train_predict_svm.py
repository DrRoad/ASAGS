from sklearn import svm
import numpy as np
import time
start_time = time.time()
X = []
Y = []

for i in range(1,128):
    try:
        file_name = 'Ovif_features_NON_VIOLENT/nonvio_'+str(i)+'.txt'
        file_obj = open(file_name,'r')
        vif = np.loadtxt(file_obj)
        X.append(vif)
        Y.append(0)
        file_obj.close()
    except:
        print 'error in reading nonvio_%d.txt'%i
#reading violent video features
for i in range(1,130):
    try:
        file_name = 'Ovif_features_VIOLENT/vio_'+str(i)+'.txt'
        file_obj = open(file_name,'r')
        vif = np.loadtxt(file_obj)
        X.append(vif)
        Y.append(1)
        file_obj.close()
    except:
        print 'error in reading vio_%d.txt'%i

clf = svm.SVC(kernel = 'linear')
clf.fit(X,Y)
print clf
print("--- %s seconds ---" % (time.time() - start_time))

pred = []

for i in X:
    pred.append(clf.predict(i.reshape(1,-1)))

count = 0

for i in range(0,len(Y)):
    if pred[i][0] == Y[i]:
        count = count + 1

print 'accuracy is : '+str(float(count)/len(Y))
