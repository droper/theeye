from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from models import Event, Session, Application


def event(request, app):

    if HttpRequest.method == 'POST':
        app = Application.models.get(id=app)
        session = Session(request.POST['session_id'])
        session.save()
        event = Event(category=request.POST['category'],
                      session=session,
                      application = app,
                      name = request.POST['name'],
                      payload=request.POST['data'],
                      timestamp=datetime.timestamp(request.POST['timestamp']))
        event.save()





