from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Farmer, Officer, Announcement, Feedback


def admin_home(request):
    data = Farmer.objects.all()
    dataO=Officer.objects.all()
    lenf=len(data)
    leno=len(dataO)
    return render(request, 'admin/dashboard.html',{'data2':lenf,'data1':leno})

def enquiry_view(request):
    f = Feedback.objects.all()
    return render(request, 'admin/enquiry_view.html', {'feedback': f})
def view_announce(request):
    content=Announcement.objects.all()
    return render(request,'admin/announce_view.html',{'content':content})


