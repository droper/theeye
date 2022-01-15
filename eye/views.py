"""Eye views"""

from datetime import datetime
import logging

from django.http import HttpRequest, HttpResponse
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

from .models import Event, Session, Application
from .decorators import application_trusted

# Get an instance of a logger
logger = logging.getLogger(__name__)

@csrf_exempt
@application_trusted
def event(request, app):
    """Saves the event, if there is a problem send an 404 error"""

    if request.method == 'POST':
        app = Application.objects.get(id=app)
        # If the session does not exist, create it, if exists, use it.
        if not Session.objects.filter(session_id=request.POST['session_id']).exists():
            session = Session(session_id=request.POST['session_id'])
            session.save()
        else:
            session = Session.objects.get(session_id=request.POST['session_id'])
        timestamp = datetime.strptime(request.POST['timestamp'],
                                     "%Y-%m-%d %H:%M:%S.%f")
        # Create the event
        event = Event(category=request.POST['category'],
                      session=session,
                      application=app,
                      name=request.POST['name'],
                      payload=request.POST['data'],
                      timestamp=timestamp)
        event.save()
        logger.info('Payload: ' + request.POST['data'])
        logger.info('Timestamp: ' + request.POST['timestamp'])
        return HttpResponse('Event saved')
    return HttpResponseNotFound('Event not saved')






