from django.shortcuts import render, redirect
from pyqrcode import QRCode
from django.contrib import messages
import os


# Create your views here.


def home(request):


    
    return render(request, 'home.html',)


def qrmaker(request):
    
    if request.method == "GET":

        urls = request.GET['url']
        names = request.GET['save']
        messages.success(request, 'Your qrcode image has been saved on your device')
    else:
        return redirect('home')

    QRstring = urls
    url = QRCode(QRstring)
    os.chdir('/home/pako/Pictures')
    img = url.png(names, scale=8)
    print(os.listdir('/home/pako/Pictures'))
    

   

    return render(request, 'result.html', )
