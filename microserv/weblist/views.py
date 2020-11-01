from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from weblist.tasks import hello_world
# , parse_website_text
from weblist.models import TaskPars
from datetime import datetime

# def index(request):
#     return render(request, 'index.html')

from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"

    #     parse_website_text.delay()
    # отправить в очередь в celety

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        # context["latest_articles"] = Article.objects.all()

def index(request):
    if request.method == 'post':
        url_adress = request.form.get('url_adress')
        new_task = TaskPars(address=url_adress, timestamp=datetime.now(), task_status='NOT_STARTED')
        new_task.save()

         # db.session.add(new_task)
         # db.session.commit()
        hello_world.delay()
        print('index post')
        data = {'tt': 'index post' }
        # return render(request, "index.html", context= data)
        redirect('/index/')
    data = {'tt': 'index get' }
    return render(request, "index.html", context= data)

def results(request):
    object_list = TaskPars.objects.all()

    return render(request, "results.html", context = {"object_list": object_list })