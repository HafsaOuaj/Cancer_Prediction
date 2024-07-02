import pandas as pd
from sklearn.model_selection import train_test_split

def create_model(data):
    X,y=data.drop(['diagnosis'],axis=1),data['diagnosis']
    

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
    model=create_model(data)
    
    
if __name__=='__main__':
    main()