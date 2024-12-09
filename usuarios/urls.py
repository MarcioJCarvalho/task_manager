from django.urls import path
from django.contrib.auth import views
from django.urls import reverse_lazy
from .views import PerfilUpdate, UsuarioCreate

urlpatterns = [
    path("registrar/", UsuarioCreate.as_view(), name="registrar"),
    path("sign-in/", views.LoginView.as_view(
        template_name="usuarios/login.html",
        extra_context={
            'titulo': 'Autenticação de Usuários'
        }
    ), name='signin'),

    path("log-out/", views.LogoutView.as_view(), name='logout'),

    path("password/", views.PasswordChangeView.as_view(
        template_name="usuarios/form.html",
        success_url = reverse_lazy('index'),
        extra_context={
            'titulo': 'Autualizar senha'
        }
    ), name='password-change'),
    path('atualizar-dados/', PerfilUpdate.as_view(), name='atualizar-dados'),
]