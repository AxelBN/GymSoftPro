from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, UpdateView, DeleteView
from django.http import request
from .models import HealthQuests, physical_evaluation
from .user import Users
from .physical_evaluations import pe
# Create your views here.

def index(request):
    return render(request, 'HealthQuest/index.html')

class users_list(ListView):
    model = HealthQuests
    paginate_by = 100

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

class updateuser(UpdateView, SuccessMessageMixin):
    model = HealthQuests
    fields = '__all__'
    template_name = 'HealthQuest/update.html'
    success_message = 'Usuario actualizado'

    def uptd_user(self):
        return reverse('user_list')


def deleteuser(request, pk):
    user = get_object_or_404(HealthQuests, id=pk)
    user.delete()

    return redirect('/users')

class update_pe(UpdateView, SuccessMessageMixin):
    model = physical_evaluation
    fields = '__all__'
    template_name = 'HealthQuest/update_pe.html'
    success_message = 'Actualizado correctamente'

    def uptd_pe(self):
        return reverse('user_list')