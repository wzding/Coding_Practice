import numpy as np
from scipy.stats import norm
from datetime import datetime
import sys

class NWK(object):
    def __init__(self, h):
        if h <= 0:
            sys.exit("Bandwidth must be a positive integer")
        self.h = h

    def fit(self, X_train, y_train):
        """
        :type X_train: array, X_train[:,2] has to be in format '%Y-%m-%d %H:%M:%S.%f'.
        :type y_train: array
        :rtype: array
        """
        if len(X_train) == 0 or len(y_train) == 0:
            # print ""
            sys.exit("Training data cannot be empty")
        
        if sum(y_train < 0) > 0:
            # print "House should not have negative price"
            sys.exit("House should not have negative price")
        self.X_train = X_train
        self.tr_time = self.timetosec(X_train)
        self.timeorder = [i[0] for i in sorted(enumerate(self.tr_time), key=lambda x:x[1])]
        self.y_train = y_train        
        
    def timetosec(self, data): # convert time to seconds
        """
        This function converts datatime object to seconds.
        :type data: array with the third column as datetime object
        :rtype: List(float)
        """
        convert_sec = lambda t:(datetime.strptime(t,'%Y-%m-%d %H:%M:%S.%f')-datetime(1970,1,1)).total_seconds()
        time = map(convert_sec ,data[:,2].tolist())
        return time
    
    def predict(self, X_test):
        '''
        This function uses Kernel method (Gaussian kernel) to fit non-parametric model for predicting house 
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
                dis = np.sqrt(np.sum(np.square(np.subtract(X_test[i][:2], self.X_train[j][:2]))))
                # add it to list of distances
                distances.append([dis, j])
        
            l = len(distances)
            if l == 0:
                y_test[i] = float('nan')   
            else:   
                dd = [d[0] for d in distances]
                # kernel method
                kernel = map(lambda t: norm.pdf(t/float(self.h)), dd)
                sum_y = 0
                for ll in range(l):
                    sum_y += kernel[ll] / float(sum(kernel)) * self.y_train[distances[ll][1]]
                y_test[i] = sum_y                     
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