"""
Titanic dataset 'titanic.xls'
Can K-means find clusters for passanger based on their
    - Passenger Class (pClass): 1st Class, 2nd Class, 3rd Class
    - Sex (sex): Gender male or female
    - Age (age): Float, how old
    - Siblings (sibsp): Number of siblings/spouses aboard
    - Children (parch): Number of parents/chlidren aboard
    - Home Destination: Destination of each passenger
    - Cabin Number: Passenger cabin number
    - Embarked Location: Ship embarked location

Each cluster will represent an indicvidual that will
Surviver (1) or Not Survive (0) the event. K-means has no information
prior to the sift setting sail

Steps of analysis:
- Fill missing data
- Quantify freatures used for training
- Scale Data
- Train KMeans
- Use survival data to determine accuracy
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
import matplotlib.pyplot as plt
from matplotlib import style

def read_excel(filename):
    df = pd.read_excel(filename)
    # Drop 'body' column due to high NaN
    # Drop 'name' and 'ticket' as they might not be useful
    df.drop(['body','name','ticket'],1,inplace=True)
    df.fillna(0,inplace=True)
    return df
# Similar to preprocessing.LabelEncoder()
def quantify_data(df):
    columns = df.columns.values

    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]
        # Check each column for ints or float
        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+=1
            df[column] = list(map(convert_to_int, df[column]))
    return df

df = quantify_data(read_excel('titanic.xls'))

# Freatures
X = np.array(df.drop(['survived'],1).astype(float))
# Scale the values to be between -1 and 1
X = preprocessing.scale(X)
y = np.array(df['survived'])

# Create and fit the model
clf = KMeans(n_clusters=2).fit(X)
clf.labels_

correct = 0
for i in range(len(X)):
    # Using each row of X determine it's cluster centroid
    predict_me = np.array(X[i])
    predict_me = predict_me.reshape(-1, len(predict_me))
    # Make prediction using the known s
    prediction = clf.predict(predict_me)
    if prediction[0] == y[i]:
        correct+=1

# Since K-means doesn't know what the values represent
prob_survive = correct/len(X)
if prob_survive < 0.5:
    prob_survive=1-prob_survive
prob_survive = int(prob_survive*100)

print('Before getting on the ship, there is a {}% change of survival'.format(prob_survive))

"""
It's very interesting how K-means is capiable of making two clusters that
label those who will survive and who will not at ~70% sucess rate
"""
