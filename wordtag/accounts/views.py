from django.shortcuts import render, redirect
from django.contrib.auth import views as auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .forms import ProfileForm

class AccountLoginView(auth.LoginView):
    template_name = 'accounts/login.html'

class AccountLogoutView(auth.LogoutView):
    def get(self, request, *args, **kwargs):
        super(AccountLogoutView, self).get(request, *args, **kwargs)
        return redirect('accounts:login')

class AccountProfileView(View):
    def get(self, request):
        return redirect('home')

class AccountProfileEditView(View):
    template_name = 'accounts/profile.html'
    form_class = ProfileForm

    def get(self, request, *args, **kwargs):
            form = self.form_class(instance=request.user.profile)
            return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:update')
        else:
            return render(request, self.template_name, {'form': form})

class AccountRegisterView(View):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            model = form.save()
            user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1']
                )
            login(request, user)
            return redirect('accounts:update')
        else:
            return render(request, self.template_name, {'form': form})
