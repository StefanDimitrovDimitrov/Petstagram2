from django.contrib.auth import logout
from django.shortcuts import render, redirect

# Create your views here.
from Petstagram2.accounts.forms import SignUpForm
from Petstagram2.accounts.models import UserProfile


def user_profile(request, pk=None):
    pass


def signup_user(request):
    if request.method == 'GET':
        context = {
            'form': SignUpForm()
        }
        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user = user,
            )
            profile.save()
            return redirect('index')

        context = {
            'form': form
        }
        return render(request, 'accounts/signup.html', context)




def signout_user(request):
    logout(request)
    return redirect('index')