from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        uform = UserForm(data=request.POST)
        pform = UserProfileForm(data=request.POST)
        if uform.is_valid() and pform.is_valid():
            user = uform.save()
            userprofile = UserProfileForm(
                request.POST, request.FILES, instance=user.userprofile)
            userprofile.save()
            return redirect('/')
    else:
        uform = UserForm()
        pform = UserProfileForm()
    return render(request, 'users/register.html', context={
        'pform': pform,
        'uform': uform
    })

