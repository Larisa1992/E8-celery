from microserv.celery import app

# from celery import shared_task

from time import sleep


# @shared_task
@app.task
def hello_world():
  sleep(10) # поставим тут задержку в 10 сек для демонстрации ассинхрности
  print('Hello World')
  return('Hello celery')

@app.task
def parse_website_text(_id):
    task = Tasks.query.get(_id)
    task.task_status = 'PENDING'
    db.session.commit()
    address = task.address
    if not (address.startswith('http') and  address.startswith('https')):
        address = 'http://' + address
    with app.app_context():
        res = requests.get(address) 
        words_count=0
        if res.ok:
            words = res.text.split()
            words_count = words.count("Python")
            
        result = Results(address=address, words_count=words_count, http_status_code=res.status_code)
        task = Tasks.query.get(_id)
        task.task_status = 'FINISHED'
        db.session.add(result)
        db.session.commit()