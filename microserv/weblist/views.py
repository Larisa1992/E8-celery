from django.shortcuts import render
from django.urls import reverse_lazy
from weblist.tasks import hello_world, parse_website_text
from weblist.models import Tasks
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

# def index(request):
#     if request.method == 'post':
#         url_adress = request.form.get('url_adress')
#         new_task = Tasks(address=url_adress, timestamp=datetime.now(), task_status='NOT_STARTED')
#         # db.session.add(new_task)
#         # db.session.commit()
#         hello_world.delay()
#     return render(request, "index.html")

def results(request):
    return render(request, "results.html")