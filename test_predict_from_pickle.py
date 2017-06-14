
from sklearn.externals import joblib
model_file_name = 'clfDT.pkl' 
clf = joblib.load(model_file_name)

print(clf.predict([[190,70,43]]))