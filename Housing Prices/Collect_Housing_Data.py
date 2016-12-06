import pandas as pd
import numpy as np
from sklearn import svm, preprocessing, cross_validation
from sklearn.linear_model import LogisticRegression

def label(our_hpi,future_hpi):
    return 1 if future_hpi > our_hpi else 0

def training():
    
    housing_data = pd.read_pickle('HPI.pickle')
    housing_data = housing_data.pct_change()
    housing_data.replace([np.inf,-np.inf],np.nan, inplace=True)
    housing_data.dropna(inplace = True)
    housing_data['US_HPI_Future']= housing_data['United States'].shift(-1)
    housing_data['label']=list(map(label,housing_data['United States'],
                                   housing_data['US_HPI_Future']))

    # Collect the data
    X = np.array(housing_data.drop(['label','US_HPI_Future'],1))
    X = preprocessing.scale(X)
    y = np.array(housing_data['label'])

    # Apply train test split
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y, test_size=0.2)

    # Train the models
    svm_model = svm.SVC(kernel='linear').fit(X_train,y_train)
    log_model = LogisticRegression().fit(X_train,y_train)
    
    svm_score = svm_model.score(X_test,y_test)
    log_score = log_model.score(X_test,y_test)
    
    print('SVM:{}\nLogistic:{}'.format(svm_score,log_score))

if __name__=='__main__':
    training()    
    
    
