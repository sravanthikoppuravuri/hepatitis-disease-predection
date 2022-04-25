import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
hepatitis_data=pd.read_csv('hepatitis.csv')
data=hepatitis_data.dropna(axis=0)
X=data.iloc[:,:-1]
Y=data.iloc[:,-1]
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
gn=GaussianNB()
gn.fit(X_train,Y_train)
#gn_test=gn.predict(X_test)
#'Confusion matrix:{0}'.format(metrics.confusion_matrix(Y_test,gn_test))
#metrics.classification_report(Y_test,gn_test)

pickle.dump(gn,open('model.pkl','wb'))
