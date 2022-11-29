from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView

from .models import HealthQuests
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
    return render(request, 'create_users.html', context)

def physical_evaluation_view(request):
    physical_evaluations = pe(request.POST or None)
    if physical_evaluations.is_valid():
        physical_evaluations.save()
        messages.success(request, 'Usuario guardado')
        physical_evaluations = pe()
    else:
        messages.error(request, 'Error')
    context = {'physical_evaluations': physical_evaluations}
    return render(request, 'physical_evaluations.html', context)