import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report
import pickle

def create_model(data):
    X,y=data.drop(['diagnosis'],axis=1),data['diagnosis']
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)
    scaler=StandardScaler()

    scaler.fit_transform(X_train)

    X_train=scaler.transform(X_train)
    X_test=scaler.transform(X_test)

    model=LogisticRegression()

    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    print("Accuracy of the model: ",accuracy_score(y_test,y_pred))
    print("Classification repport: ",classification_report(y_test,y_pred))

    return model,scaler



def get_clean_data():
    data=pd.read_csv("data/data.csv")
    data=data.drop(["Unnamed: 32","id"],axis=1)
    data["diagnosis"]= data["diagnosis"].map(
        {'M':1,'B':0}
    )
    
    print(data.info())
    return data
    
def main():
    data=get_clean_data()
    model,scaler=create_model(data)

    with open('model/model.pkl','wb') as f:
        pickle.dump(model,f)

    with open('model/scaler.pkl','wb') as f:
        pickle.dump(scaler,f)

if __name__=='__main__':
    main()