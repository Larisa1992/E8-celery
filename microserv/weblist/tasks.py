from microserv.celery import app
from weblist.models import TaskPars, Results
import requests

@app.task
def parse_website_text(_id):
  task = TaskPars.objects.get(pk = _id)
  task.task_status = 2 # PENDING
  task.save()
  adr = task.address
  if not (adr.startswith('http') and  adr.startswith('https')):
    adr = 'http://' + adr
  res = requests.get(adr, timeout=10)
  words = 0
  if res.ok:
    all_words = res.text.split()
    words = all_words.count("Python")
  result = Results(address=adr, words_count=words, http_status_code=res.status_code)
  result.save()

  task = TaskPars.objects.get(pk = _id)
  task.task_status = 3 # FINISHED
  task.save()
