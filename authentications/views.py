from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .forms import RegisteForm, Edit_RegisteForm
from django.contrib.auth.views import PasswordChangeForm,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,\
    PasswordResetCompleteView

# Create your views here.

def home(request):
    return render(request,'home/home.html')


def about(request):
    return render(request,'home/about.html')

def login_user(request):
    if request.method == 'POST':
       username=request.POST['username']
       password=request.POST['password']
       user=authenticate(request,username=username,password=password)
       if user is not None:
          login(request,user)
          messages.success(request,'Login Successfully')
          return redirect('home')
       else:
           messages.success(request, 'Try Agin')
           return redirect('login')
    else:
        return render(request,'auths/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully Logout')
    return redirect('login')

def register_view(request):
    if request.method == "POST":
        form=RegisteForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Create an Account')
            return redirect('home')
    else:
        form = RegisteForm()
    contex={
        "form":form
    }
    return render(request,'register/register.html',contex)

def edit_register_view(request):
    if request.method == "POST":
        form=Edit_RegisteForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Update Successfully')
            return redirect('home')
    else:
        form = Edit_RegisteForm(instance=request.user)
    contex={
        "form":form
    }
    return render(request,'register/edit_register.html',contex)

def change_passwrod(request):
    if request.method == "POST":
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request, 'Change Password')
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    contex={
        "form":form
    }
    return render(request, 'password/change_passwrod.html', contex)

class RestPassword(PasswordResetView):
    template_name ='password/password_reset.html'

class RestPasswordDone(PasswordResetDoneView):
    template_name ='password/password_reset_done.html'

class RestPasswordConfirm(PasswordResetConfirmView):
    template_name ='password/password_reset_confirm.html'

class RestPasswordComplete(PasswordResetCompleteView):
    template_name ='password/password_reset_complete.html'