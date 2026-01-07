from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from ..forms import UserRegisterForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user
        return context


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registrar_usuario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        return super().form_valid(form)
