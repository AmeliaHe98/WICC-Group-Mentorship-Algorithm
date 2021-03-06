import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing, model_selection
import pandas as pd

df = pd.read_excel('WICC Mentorship Responses.xlsx')
df.convert_objects(convert_numeric = True)
df.fillna(0, inplace = True)
df.drop(['Any mentors or mentees you really want to be in a group with? List as many or few as you like!',
         'Anything else you like us to know?',
         'School'],
        1, inplace = True)

def handle_non_numerical_data(df):
    columns = df.columns.values
    
    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]
        
        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x += 1
                    
            df[column] = list(map(convert_to_int, df[column]))
    
    return df

df = handle_non_numerical_data(df)
print(df.head())

x = np.array(df.drop(['Academic Interests in Computing'], 1).astype(float))
y = np.array(df['Academic Interests in Computing'])

clf = KMeans(n_clusters = 2)
clf.fit(x)

centroids = clf.cluster_centers_
labels = clf.labels_

colors = 10 * ["g.", "r.", "c.", "k."]

for i in range(len(x)):
    plt.plot(x[i][0], x[i][1], colors[labels[i]], markersize = 25)
plt.scatter(centroids[:, 0], centroids[:, 1], marker = 'x', s = 150, linewidth = 5)
plt.show()
