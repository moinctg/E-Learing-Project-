from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.form import UserRegisterForm ,UserUpdateForm , ProfileUpdateForm


def register(request):  # user register 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been Created! Now you can able to login ')
            return redirect ('login')
    else:
        form = UserRegisterForm()
    return render (request, 'accounts/register.html', {'form': form } )
    
@login_required
def profile(request):  # update profile 
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been Updated! ')
            return redirect ('profile')              
    else:
         u_form = UserUpdateForm(instance=request.user)
         p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html', context)