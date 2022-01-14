from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=30)
    trusted = models.BooleanField()

class Session(models.Model):
    session_id = models.CharField(max_length=100, unique=True)

class Event(models.Model):
    category = models.CharField(max_length=30)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    payload = models.JSONField()
    timestamp = models.DateTimeField()



