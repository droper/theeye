from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

class Application(models.Model):
    name = models.CharField(max_length=30)
    trusted = models.BooleanField()

class Session(models.Model):
    pass

class Event(models.Model):
    order = models.IntegerField()
    category = models.ForeignKey(Category)
    session = models.ForeignKey(Session)
    application = models.ForeignKey(Application)
    name = models.CharField(max_length=30)
    payload = models.JSONField()



