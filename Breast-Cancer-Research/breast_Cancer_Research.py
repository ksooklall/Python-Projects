"""
Breast cancer is cancer that develops from breast tissue.
Signs of breast cancer may include a lump in the breast, a change in breast
shape, adhesion of the skin, and many more.

Data pulled from UC Irvine is analyzed with three different supervised
machine learning techniques, K Nearest neighbors, Naive Bayes Classifier
and Logistic Regression.

The data is fit to each ML technique and the best performing is used to make
a prediction.

Results are:
    0 -> benign (good)
    1 -> malignant(bad)

Nine freatures were examined
Freatures: Clump thickness, uniformity of cell size, uniformity of cell shape,
Marginal Adhesion, Single epithelial Cell Size, Bare Nuclei, Bland Chromatin,
Normal Nucleoli, Mitoses
"""

import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation, neighbors
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression

# Array for the scores
scores = np.array([])
    
# Import the data from the downloaded data set
def get_data():
    df = pd.read_csv('breast-cancer-wisconsin.data.txt')

    # Replace missing data with -99999 (it will become an outliar)
    # missing data in this data set is '?'
    df.replace('?',-99999, inplace=True)
    # Remove id column as it is not a freature for tumor classification
    df.drop(['id'],1,inplace=True)
    return df

# Using the data create a training and testing set
def create_data_set(df):
    # Define freature and labels
    X = np.array(df.drop('labels',1))
    y = np.array(df['labels'])

    # Cross validation- Shuffel and partitioning the data into training and testing sets
    X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y,test_size=0.2)
    return X_train,X_test,y_train,y_test

# Determine the best model for the data
def best_model(model='KNN_model'):
    X_train,X_test,y_train,y_test = create_data_set(get_data())

    # Create the model for KNN and fit the training data to it
    KNN_model = neighbors.KNeighborsClassifier().fit(X_train,y_train)
    Naive_Bayes_model = GaussianNB().fit(X_train,y_train)
    LogisticRegression_model = LogisticRegression().fit(X_train,y_train)
    SVM_model = SVC().fit(X_train,y_train)

    clf_models = [KNN_model, Naive_Bayes_model,
                  LogisticRegression_model, SVM_model]

    # Determine model accuracy with testing data
    KNN_acc = KNN_model.score(X_test, y_test)
    Naive_Bayes_acc = Naive_Bayes_model.score(X_test,y_test)
    LogisticRegression_acc = LogisticRegression_model.score(X_test,y_test)
    SVM_acc = SVM_model.score(X_test,y_test)

    scores = [KNN_acc,Naive_Bayes_acc,LogisticRegression_acc,SVM_acc]

    models = ['K Nearest Neighbors', 'Naive Bayes','Logistic Regression',
              'Support Vector Machine']
    print('KNN acc:{}, NB acc:{},\nLG acc: {}, SVM acc:{}'.format(KNN_acc,
                                                                 Naive_Bayes_acc,
                                                     LogisticRegression_acc,
                                                                 SVM_acc))
    # Geth the model with the highest score
    value, idx = max([val,idx] for idx,val in enumerate(scores))
    print('{} is the best classifier'.format(models[idx]))
    return clf_models[idx]

# Use the model to predict if you have a tumor
def predict(ct,ucsi,ucsh,ma,secs,bn,bc,nn,m):
    clump_thickness = ct
    unif_cell_size = ucsi
    unif_cell_shape = ucsh
    marg_adhesion = ma
    single_epith_cell_size = secs
    bare_nuclei = bn
    bland_chrom = bc
    norm_nucleoli = nn
    mitoses = m
    X_predict = np.array([clump_thickness,unif_cell_size,unif_cell_shape,
                      marg_adhesion,single_epith_cell_size,bare_nuclei,bland_chrom,
                      norm_nucleoli,mitoses])
    predict = best_model().predict(X_predict.reshape(1,9))
    
    return 'Congrats its benign:{}'.format(predict%2) if predict%2==0 else 'Sorry its malignant:{}'.format(predict%2)

print(predict(4,2,2,2,3,2,4,2,2))
