from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=30)
    trusted = models.BooleanField()

class Session(models.Model):
    session_id = models.model(unique=True)

class Event(models.Model):
    order = models.Autofield()
    category = models.CharField(max_length=30)
    session = models.ForeignKey(Session)
    application = models.ForeignKey(Application)
    name = models.CharField(max_length=30)
    payload = models.JSONField()
    timestamp = models.DateTime()



