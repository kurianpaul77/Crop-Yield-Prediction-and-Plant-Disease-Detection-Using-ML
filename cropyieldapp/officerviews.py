from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import LoginRegister, OfficerRegister, Announcementform
from .models import Officer, Login, Feedback, Announcement


def officer_home(request):
    return render(request,'officer/home.html')





def officer_register(request):
    user_form = LoginRegister()
    officer_form = OfficerRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        officer_form = OfficerRegister(request.POST, request.FILES)
        if user_form.is_valid() and officer_form.is_valid():
            user = user_form.save(commit=False)
            user.is_officer = True
            user.save()
            officer = officer_form.save(commit=False)
            officer.user = user
            officer.save()
            messages.info(request, 'Registered Successfully')
            return redirect('view_officer')
    return render(request, 'officer/reg.html', {'user_form': user_form, 'officer_form': officer_form})

@login_required(login_url='login')
def view_officer(request):
    data = Officer.objects.all()
    return render(request, 'officer/officers.html', {'data': data})


def remove_officer(request, id):
    data1 = Officer.objects.get(id=id)
    data = Login.objects.get(officer=data1)
    if request.method == 'POST':
        data.delete()
        return redirect('view_officer')
    else:
        return redirect('view_officer')


def enquiry_view(request):
    f = Feedback.objects.all()
    return render(request, 'officer/enquiry_view.html', {'feedback': f})


def announce(request):
    form = Announcementform()
    if request.method == 'POST':
        form = Announcementform(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = Officer.objects.get(user=request.user)
            obj.save()
            messages.info(request, 'Announcement added Successfully')
            return redirect('view_announce')
    return render(request,'officer/announce_add.html',{'form':form})


def view_announce(request):
    content=Announcement.objects.all()
    return render(request,'officer/announce_view.html',{'content':content})


def reply_enquiry(request, id):
    f = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        f.reply = r
        f.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('enquiry_view_of')
    return render(request, 'officer/reply_enquiry.html', {'feedback': f})


