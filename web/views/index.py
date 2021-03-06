from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.models import User


def get_user(email=None, username=None):
    try:
        if email:
            return User.objects.get(email=email.lower())
        else:
            return User.objects.get(username=username.lower())
    except User.DoesNotExist:
        return None


def index(request):
    """Index Page."""
    return render(request, "web/index.html", {})


def login_page(request):
    if user.is_authenticated():
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.POST['next']
        if not username or not password:
            return render(request, 'web/login.html', {'error': _('Missing Fields')})
        if '@' in username:
            _user = get_user(email=username)
        else:
            _user = get_user(username=username)
        if not _user:
            return render(request, 'web/login.html', {'error': _('User not found')})
        username = _user.username
        _user = authenticate(username=username, password=password)
        if _user:
            if _user.is_active:
                login(request, _user)
                return redirect(next_url)
            else:
                return render(request, 'web/login.html', {'error': _('Account Disabled')})
        else:
            return render(request, 'web/login.html', {'error': _('Invalid login credentials')})
    return render(request, 'web/login.html', {})


def register_page(request):
    if user.is_authenticated():
        return redirect('index')


def logout_page(request):
    pass
