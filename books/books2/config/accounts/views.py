from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

from .forms import RegistrationForm
from .tokens import accounts_activation_token
from django.core.mail import EmailMessage



def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            user.save()

            current_site = get_current_site(request=request)
            subject = 'Активация аккаунта'
            message = render_to_string(template_name='accounts/activation_email.html', context={
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(user.pk),
                'token': accounts_activation_token.make_token(user=user)
            })
            email = EmailMessage(subject, message, to=[user.email])
            email.send()

            messages.success(request, 'Письмо с подтверждением отправлено на ваш Email')
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request=request, 
                  template_name='accounts/register.html', 
                  context={'form':form})






def activate_account(request, uidb64, token):
    return HttpResponse("Заглушка для активации")

def login_view(request):
    return HttpResponse("Заглушка для входа")

def logout_view(request):
    return HttpResponse("Заглушка для выхода")