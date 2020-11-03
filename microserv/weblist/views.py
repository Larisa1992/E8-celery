from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from weblist.tasks import parse_website_text
from weblist.models import TaskPars, Results
from django.utils import timezone
from django.views.generic.base import TemplateView

def index(request):
    if request.method == 'POST':
        url_adress = request.POST['url_adress']
        new_task = TaskPars(address=url_adress, timestamp=timezone.now(), task_status=1)
        new_task.save()
        parse_website_text.delay(new_task.pk)
        data = {'tt': 'index post' }
    data = {'tt': 'index get' }
    return render(request, "index.html", context= data)

def results(request):
    object_list = Results.objects.all()
    return render(request, "results.html", context = {"object_list": object_list })