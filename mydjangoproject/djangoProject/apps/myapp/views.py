from django.shortcuts import render, redirect
from .forms import registerForm
from .models import registrationModel
# Create your views here.

def homeview(request):
    form = registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                form.add_error('confirm_password', 'Password did not match')
            else:
                form.save()
                return redirect('/userdata/')
    return render(request, 'myapp/index.html', {'form': form})

def userdataview(request):
    formdata = registrationModel.objects.all()
    return render(request, 'myapp/userdata.html', {'form': formdata})