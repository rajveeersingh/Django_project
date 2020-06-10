from django.db import models

# Create your models here.


###Databases config.


from django.db import connection

class Database:
    def __init__(self):
        pass


    def select(self, query):
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def execute(self, query):
        with connection.cursor() as cursor:
           cursor.execute(query)
           return connection.commit()

    def __del__(self):
        pass





#machine learning model
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import math
import locale
## its a linear regression model
class Linear:
    def clean(self):
        df = pd.read_csv('/home/superadmin/DBDA/django_1st_app/first_app/myapp/Crime_visual/Predict.csv',usecols=['crime_type','year'])
        Nd = pd.DataFrame(df['crime_type'].groupby(df['year']).agg('count').reset_index(name="crime_count"))
        x = Nd.iloc[:, [0]].values
        y = Nd.iloc[:, [1]].values   
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1234)
        print(x_test,y_test)
        del x_test, y_test
        print(x_test,y_test)
        return x_train,y_train
    # prediction model
    def model(self,value):
        x_train,y_train = Linear().clean()
        regression = LinearRegression()
        regression.fit(x_train, y_train)
        prediction = regression.predict([[value]])
        print(prediction[0][0])
        z = prediction[0][0] % 1
        if z >= 0.5:  
            pred = math.ceil(prediction[0][0])
            print(f"prdiction1 is {pred}")
        else:
            pred = math.floor(prediction[0][0])
            print(f"prdiction 2is {pred}")
        return locale.format("%d", pred, grouping=True)

## its a Decision tree
class DecisionTree:
    def __init__(self):
        self.df = pd.read_csv('/home/superadmin/DBDA/django_1st_app/first_app/myapp/Crime_visual/Prediction.csv')
        
        
    def clean(self):
        
        x = self.df.iloc[:, 2:8].values
        y = self.df.iloc[:, 1].values
        from sklearn.preprocessing import LabelEncoder  
        encoder = LabelEncoder()
        x[:,0] = encoder.fit_transform(x[:,0])
        y = encoder.fit_transform(y)
        from sklearn.model_selection import train_test_split
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.8,random_state=123)
        return x_train,x_test,y_train,y_test
    def accuracy(self,predictions,y_test):
        # create the confusion matrix
        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(y_test, predictions)

        accuracy = (cm[0][0] + cm[1][1]) / (cm[0][0] + cm[0][1] + cm[1][0] + cm[1][1])
        print(round((accuracy*100),2),"%")

    def decis(self,x_train,x_test,y_train):
        # x_train,x_test,y_train,y_test = clean()
        from sklearn.tree import DecisionTreeClassifier
        classifier = DecisionTreeClassifier()
        classifier = classifier.fit(x_train, y_train)
        predictions = classifier.predict(x_test)
        print(predictions)
        return predictions


## data visualization code


from matplotlib import pyplot as plt
from wordcloud import WordCloud
from datetime import datetime as dt
import seaborn as sns


class Analysis:
    def __init__ (self,x=0):
        self.x = x
        if x == 1:
            Analysis().pie()
        elif x== 2:
            Analysis().bar_chart()
        elif x == 3:
            Analysis().wordcloud()
        elif x == 4:
            Analysis().countpl()
        elif x == 5:
            Analysis().line()

    def pie(self):
        df = pd.read_csv('/home/superadmin/DBDA/project/My_Project/Crime_new.csv',usecols=['crime_type','Area_name'],nrows=500000)
        pf =df.groupby([ 'Area_name']).count().reset_index("Area_name").sort_values(ascending=False,by='crime_type').iloc[:6]
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = tuple(pf['Area_name'])
        sizes = tuple(pf['crime_type'])
        explode = ( 0.1,0.1,0.1,0.1,0.1,0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
        fig1, ax1 = plt.subplots(figsize=(5, 4))
        x,y,z =ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=70, textprops=dict(color="black"))
        # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Top 10 Area with higest crime percentage',size=15)
        plt.setp(z, size=8, weight="bold",color="white")
        plt.tight_layout()
        plt.savefig('/home/superadmin/DBDA/django_1st_app/first_app/myapp/static/arr.png')
        # plt.show()
        print("piechart")


    # ploting the wordcloud
    def wordcloud(self):
        #load the data set
        df = pd.read_csv('/home/superadmin/DBDA/project/My_Project/Crime_new.csv',usecols=['crime_type'],nrows=1000000)
        # critaria = 'crime_type'
        # df = pd.DataFrame(execute1(critaria))
        wc = df['crime_type']
        WC = WordCloud(background_color = 'white',width = 1000,height = 400).generate(" ".join((str(v)for v in wc)))
        plt.figure(figsize=(15,10))
        plt.imshow(WC)
        plt.title('Types of crime in chicago\n',size=20)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig('/home/superadmin/DBDA/django_1st_app/first_app/myapp/static/arr.png')

    def line(self):
        df = pd.read_csv('/home/superadmin/DBDA/project/My_Project/Predict.csv',usecols=['crime_type','year'])
        df =pd.DataFrame(df['crime_type'].groupby(df['year']).agg('count').reset_index(name="crime_count"))
        x = df['crime_count']
        y = df['year']
        fig, ax = plt.subplots(figsize=(10,5))
        ax.plot(y, x)
        ax.set_xticks(y)
        # ax.legend()
        plt.title('Crimes over the year\n',size=20)
        plt.tight_layout()
        # plt.show()
        plt.savefig('/home/superadmin/DBDA/django_1st_app/first_app/myapp/static/arr.png')


    def bar_chart(self):
        #load the data set
        df = pd.read_csv('/home/superadmin/DBDA/project/My_Project/Crime_new.csv',usecols=['crime_type','Arrest'],nrows=1000000)
        # critaria = 'crime_type'
        # critaria2 = 'Arrest'
        # df = pd.DataFrame(Testmongo().execute(critaria,critaria2))
        Arrest = df.groupby('Arrest')
        plt.figure(figsize=(10,5))
        Arrest.size().sort_values(ascending=False).plot.bar()
        # plt.bar(crime_type,year)
        plt.xticks(rotation=50)
        plt.xlabel("Criminal arrested",fontsize = 15)
        plt.ylabel("Numer of criminal arrested",fontsize=15)
        plt.title('Arrest Record',loc='center',fontsize=15)
        plt.tight_layout()
        plt.savefig('/home/superadmin/DBDA/django_1st_app/first_app/myapp/static/arr.png')
    def countpl(self):
        #load the data set
        df = pd.read_csv('/home/superadmin/DBDA/project/My_Project/Crime_new.csv',usecols=['Area_name','crime_type'],nrows=1000000)
        # # critaria = 'crime_type'
        # critaria2 = 'Area_name'
        # df = pd.DataFrame(execute(critaria,critaria2))
        Y = df['Area_name']
        # plt.figure(figsize=(15, 20))
        sns.countplot(y=Y,  data=df['crime_type'],order=pd.value_counts(df['Area_name']).iloc[:15].index)
        plt.title('Highest crime in area',fontsize = 15)
        plt.tight_layout()
        plt.savefig("/home/superadmin/DBDA/django_1st_app/first_app/myapp/static/arr.png")
        #  plt.xlabel('location',fontsize = 5)
        #  plt.show()


