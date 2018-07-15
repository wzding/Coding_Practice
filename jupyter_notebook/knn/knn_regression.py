import numpy as np
import random
from datetime import datetime
import sys

class KNN(object):

    def __init__(self, k):
        if k <= 0:
            sys.exit("K must be a positive integer")
        self.k = k

    def fit(self, X_train, y_train):
        """
        :type X_train: array, X_train[:,2] has to be in format '%Y-%m-%d %H:%M:%S.%f'.
        :type y_train: array
        :rtype: array
        """
        if len(X_train) == 0 or len(y_train) == 0:
            # print "Training data cannot be empty"
            sys.exit("Training data cannot be empty")
        if sum(y_train < 0) > 0:
            # print "House should not have negative price"
            sys.exit("House should not have negative price") 
        self.X_train = X_train
        self.tr_time = self.timetosec(X_train)
        self.timeorder = [i[0] for i in sorted(enumerate(self.tr_time), key=lambda x:x[1])]
        self.y_train = y_train

    def timetosec(self, data):
        """
        This function converts datatime object to seconds.
        :type data: array with the third column as datetime object
        :rtype: List(float)
        """
        convert_sec = lambda t:(datetime.strptime(t,'%Y-%m-%d %H:%M:%S.%f')-datetime(1970,1,1)).total_seconds()
        time = map(convert_sec ,data[:,2].tolist())
        return time

    def partition(self, vector, left, right, pivotIndex):
        """
        This function picks a pivot and rearranges the list in a way that all elements less than pivot are
        on left side of pivot and others on right. It then returns index of the pivot element.
        :type vector: List
        :type left: int
        :type right: int
        :pivotIndex: int
        :rtype: int
        """
        pivotValue = vector[pivotIndex]
        vector[pivotIndex], vector[right] = vector[right], vector[pivotIndex]  # Move pivot to end
        storeIndex = left
        for i in range(left, right):
            if vector[i] < pivotValue:
                vector[storeIndex], vector[i] = vector[i], vector[storeIndex]
                storeIndex += 1
        vector[right], vector[storeIndex] = vector[storeIndex], vector[right]  # Move pivot to its final place
        return storeIndex

    def _select(self, vector, left, right, k):
        """
        This function returns the k-th smallest, (k >= 0), element of vector within vector[left:right+1] inclusive.
        :type vector: List
        :type left: int
        :type right: int
        :type k: int
        :rtype: List
        """
        while True:
            # select pivotIndex between left and right
            pivotIndex = random.randint(left, right)
            pivotNewIndex = self.partition(vector, left, right, pivotIndex)
            pivotDist = pivotNewIndex - left
            if pivotDist == k:
                return vector[pivotNewIndex]
            elif k < pivotDist:
                right = pivotNewIndex - 1
            else:
                k -= pivotDist + 1
                left = pivotNewIndex + 1

    def select(self, vector, k, left=None, right=None):
        """
        This function returns the k-th smallest, (k >= 0), element of vector within vector[left:right+1].
        Left, right default to (0, len(vector) - 1) if omitted.
        :type vector: List
        :type k: int
        :type left: int
        :type right: int
        :rtype: List
        """
        if left is None:
            left = 0
        lv1 = len(vector) - 1
        if right is None:
            right = lv1
        return self._select(vector, left, right, k)


    def predict(self, X_test):
        '''
        This function implements knn regression to fit non-parametric model for predicting house 
        price by historical house price.
        :type X_test: array
        :rtype: array with the same length as X_test
        '''
        if not len(X_test):
            sys.exit( "Test data cannot be empty")

        y_test = np.zeros(len(X_test))
        test_time = self.timetosec(X_test)
        for i,t in enumerate(test_time): # test points
            distances = []
            for j in self.timeorder: # training points
                # compare datetime
                if self.tr_time[j] >= t:
                    break
                # calculate euclidean distance
                dis = np.sum(np.square(np.subtract(X_test[i][:2], self.X_train[j][:2])))
                # add it to list of distances
                distances.append([dis, j])
            l = len(distances)
            if l == 0:
                y_test[i] = float('nan')
            elif l <= self.k:
                y_test[i] = np.mean(self.y_train[[d[1] for d in distances]])
            else:
                k_dis = self.select([m[0] for m in distances], self.k)
                idx = [d[1] for d in distances if d[0] < k_dis]
                # get mean of k nearest neighbors
                y_test[i] = np.mean(self.y_train[[idx]])

        return y_test

    def mrae(self, X_test, y_test):
        '''
        This function is a performance measurement in Median Relative Absolute Error.
        :type X_test: array
        :type y_test: array
        :rtype: float
        '''
        pred = self.predict(X_test)
        notnan = ~np.isnan(pred)
        if sum(np.isnan(pred)) > 0:
            print str(sum(np.isnan(pred))) + ' Nan values have been predicted'
        return np.median(abs(pred[notnan] - y_test[notnan])/y_test[notnan])
