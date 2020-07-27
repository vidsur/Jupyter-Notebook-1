#!/usr/bin/env python
# coding: utf-8

# In[106]:


import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[76]:


CreditOne = pd.read_csv(r"C:\Users\sures\OneDrive\Documents\VS\Course 5\default of credit card clients.csv", header =1)


# In[77]:


CreditOne.head()


# In[78]:


CreditOne.info()


# In[79]:


CreditOne.shape


# In[80]:


CreditOne


# In[ ]:





# In[85]:


features = CreditOne.iloc[:,1:24]
print('Summary of feature sample')
features.head()


# In[86]:


#dependent variable
depVar = CreditOne.loc[:,'default payment next month']
print('Summary of DepVar')
depVar.head()


# In[87]:


X= features
Y= depVar


# In[88]:


X.shape


# In[89]:


Y.shape


# In[90]:


from sklearn.model_selection import train_test_split


# In[91]:



X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)


# In[92]:



X_train.shape, Y_train.shape


# In[93]:


X_test.shape, Y_test.shape


# In[94]:


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF


# In[95]:


names = ["Nearest_Neighbors","Gradient_Boosting","Decision_Tree","Random_Forest"]

classifiers = [
    KNeighborsClassifier(7),
    GradientBoostingClassifier(n_estimators=50, learning_rate=1.0),
    DecisionTreeClassifier(max_depth=3),
    RandomForestClassifier(max_depth=3, n_estimators=100)]


# In[96]:


scores = []
for name, clf in zip(names, classifiers):
    clf.fit(X_train, Y_train)
    score = clf.score(X_test, Y_test)
    scores.append(score)


# In[97]:


scores


# In[98]:


df = pd.DataFrame()
df['name'] = names
df['score'] = scores
df


# In[99]:


cm = sns.light_palette("green", as_cmap=True)
s = df.style.background_gradient(cmap=cm)
s


# In[100]:


sns.set(style="whitegrid")
ax = sns.barplot(y="name", x="score", data=df)


# In[114]:


RF=RandomForestClassifier(max_depth=3, n_estimators=100)
RF.fit(X_train, Y_train)


# In[118]:


Y_Pred= RF.predict(X_test)


# In[119]:


from sklearn.metrics import accuracy_score
accuracy_score(Y_Pred, Y_test)


# In[121]:


Y_Pred, Y_test


# In[ ]:




