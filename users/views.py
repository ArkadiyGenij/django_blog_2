import random
import string

from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView

from users.forms import UserRegisterForm, LoginUserForm, PasswordResetForm
from users.models import User


# Create your views here.

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        activation_url = reverse('users:activate', args=[user.pk, user.email])
        send_mail(
            'Подтвердите ваш email',
            f'Для активации вашего аккаунта пожалуйста перейдите по ссылке: {activation_url}',
            "arkasha.gongadze2@mail.ru",
            [user.email],
            fail_silently=False,
        )
        return redirect('users:login')


def activate(request, user_id, email):
    user = get_object_or_404(User, pk=user_id, email=email)
    user.is_active = True
    user.save()
    login(request, user)
    return redirect('users:login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    extra_context = {'title': 'Авторизация'}


class PasswordResetView(FormView):
    template_name = 'users/password_reset.html'
    form_class = PasswordResetForm
    success_url = 'users:login'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            user.password = make_password(new_password)
            user.save()
            send_mail(
                'Восстановление пароля',
                f'Ваш новый пароль: {new_password}',
                'arkasha.gongadze2@mail.ru',
                [email],
                fail_silently=False,
            )
            return super().form_valid(form)
        except User.DoesNotExist:
            form.add_error('email', 'Пользователь с таким адресом электронной почты не найден.')
            return self.form_invalid(form)
