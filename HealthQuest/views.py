from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import ListView, UpdateView
from .models import HealthQuests, physical_evaluation, payments
from .user import Users
from .payments import Payments
from .physical_evaluations import pe
# Create your views here.

class Index(LoginRequiredMixin, generic.TemplateView):
    template_name = 'HealthQuest/index.html'
    login_url = 'login'

def index(request):
    return render(request, 'HealthQuest/index.html')

class users_list(LoginRequiredMixin, ListView):
    model = HealthQuests
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class physical_evaluation_list_view(LoginRequiredMixin, ListView):
    model = physical_evaluation
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class payments_list(LoginRequiredMixin, ListView):
    model = payments
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def user_view(request):
    user = Users(request.POST or None)
    if user.is_valid():
        user.save()
        messages.success(request, 'Usuario guardado')
        user = Users()
    else:
        messages.error(request, 'Error')
    context = {'user': user}
    return render(request, 'HealthQuest/create_users.html', context)

def payments_view(request):
    payment = Payments(request.POST or None)
    if payment.is_valid():
        payment.save()
        messages.success(request, 'Guardado')
        payment = Payments()
    else:
        messages.error(request, 'Error')
    context = {'payment': payment}
    return render(request, 'HealthQuest/payments.html', context)

def physical_evaluation_view(request):
    physical_evaluations = pe(request.POST or None)
    if physical_evaluations.is_valid():
        physical_evaluations.save()
        messages.success(request, 'Usuario guardado')
        physical_evaluations = pe()
    else:
        messages.error(request, 'Error')
    context = {'physical_evaluations': physical_evaluations}
    return render(request, 'HealthQuest/physical_evaluations.html', context)

class updateuser(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = HealthQuests
    fields = '__all__'
    template_name = 'HealthQuest/update.html'
    success_message = 'Usuario actualizado'
    login_url = 'login'

    def uptd_user(self):
        return reverse('user_list')

class update_payments(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = payments
    fields = '__all__'
    template_name = 'HealthQuest/update_payments.html'
    success_message = 'Actualizado'
    login_url = 'login'

    def uptd_payments(self):
        return reverse('payments_list')

def deleteuser(request, pk):
    user = get_object_or_404(HealthQuests, id=pk)
    user.delete()

    return redirect('/users')

class update_pe(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = physical_evaluation
    fields = '__all__'
    template_name = 'HealthQuest/update_pe.html'
    success_message = 'Actualizado correctamente'
    login_url = 'login'

    def uptd_pe(self):
        return reverse('user_list')