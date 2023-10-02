

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import PatientDetails

def homepage(request):
    return render(request, 'homepage.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']
        
        if pass1 != pass2:
            return HttpResponse('password and conform password is incorrect')
        else:
            my_user = User.objects.create_user(username, email, pass1)
            my_user.first_name = first_name
            my_user.last_name = last_name

            my_user.save()
            return redirect('loginpage')

    return render(request, 'signup.html')

def loginpage(request):
    if request.method == 'POST':

        username = request.POST['username']
        password1 = request.POST['password']       

        user = authenticate(username=username, password=password1)
        

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'patientpage.html', {'fname':fname})
        else:
           return HttpResponse('not matched')
        
        

    return render(request, 'loginpage.html')

def patientpage(request):
    return render(request, 'patientpage.html')

def patientpage1(request):
    return render(request, 'patientpage1.html')

def patientpage2(request):
    return render(request, 'patientpage2.html')

def patientdetails(request):
    if request.method == 'GET':
        return render(request, 'patientdetails.html')
    else:

        PatientDetails(

            Name = request.POST.get('name'),
            Age = request.POST.get('age'),
            Gender = request.POST.get('gender'),
            Mobile = request.POST.get('mobile'),
            Address = request.POST.get('address'),
            Problem = request.POST.get('problem'),
            DoctorName = request.POST.get('dname')           
        ).save()
                
        data = PatientDetails.objects.all()
        return render(request, 'adminpage.html', {'data':data})
    
 
    
'''def adminpage(request):
    data = PatientDetails.objects.all()
    return render(request, 'adminpage.html', {'data':data})'''

