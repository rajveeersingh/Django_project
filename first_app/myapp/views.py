from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

#first example of show content on web page 
# def home(request):
    # return HttpResponse("hello word!")

def home(request):
    return render(request,'Crime Analysis.html',{'name':'Friends'})

def chart(request):
    return render(request,'visualization.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'Aboutme.html')


from .models import Analysis
import time
def graph(request):
    if request.method == 'GET':
            return render(request,'Graph.html')
    elif request.method == 'POST':
            x = int(request.POST['graph'])
            Analysis(x)#.selection(x)
            time.sleep(5)
            return render(request,'Images.html' )

def tableau(request):
    return render(request,'graphanimated.html')

def dataflow(request):
    return render(request,'dataflowchart.html')


# Machine learning project code

# from Analysis import Analysis
from .models import Linear
from datetime import datetime as dt
def prediction(request):
    if request.method == 'GET':
        return render(request,'prediction.html')
    else :
        value = int(request.POST['value'])
        predicted = str(Linear().model(value))
        yr = dt.now().year
        print(type(dt.now().time()),type(yr),type(predicted),type(value)) 
        return render(request,'predict.html',{"data" : predicted,"yr" : str(yr), "year" : str(value)})


#Data base
from .models import Database
from django.contrib import messages
def cont(request):
        if request.method == 'POST':
            name = request.POST['firstname']
            s_name = request.POST['lastname']
            nation = request.POST['nation']
            state = request.POST['state']
            cmmnt = request.POST['subject']
            email = request.POST['email']
            # print(name,s_name,nation,state,cmmnt,email)
            db = Database()
            test = db.execute(f"insert into project (name,s_name,nation,state,cmmnt,emailid) values ('{name}','{s_name}','{nation}','{state}','{cmmnt}','{email}')")   
            
            messages.success(request,f'Thankyou {name} for visiting us, Your entry is successfull!'.title())
            return HttpResponseRedirect('/Contact')
        else:
            return render(request,'contact.html')