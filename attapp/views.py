from django.shortcuts import render
import datetime
import pyrebase

x=datetime.datetime.now()
x=x.strftime("%y-%m-%d %H:%M:%S")

config = {
  "apiKey":"AIzaSyBx57UaFMBPjnuTJZoW34ZvzaxgC1pPKq4",
  "authDomain": "samhith-a9fb1.firebaseapp.com",
  "databaseURL": "https://samhith-a9fb1.firebaseio.com",
  "storageBucket": "samhith-a9fb1.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db=firebase.database()
# Create your views here.
def index(request):
    return render(request,'index.html')
def result(request):
    un=request.POST['nam']        
    up=request.POST['ph']
    uu=request.POST['uni']
    ur=request.POST['rn']
    data={'time':x,
            'name':un,
            'university':uu,
            'rollno':ur,
            "contact":up 
            }
    db.child("attendance_app").push(data)
    return render(request,'results.html',{'un':un,'time':x})

    