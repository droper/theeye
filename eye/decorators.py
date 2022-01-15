"""Django decorators"""

from django.http import HttpResponseNotFound

from .models import Application


def application_trusted(function=None):
    """
    If the application exists and is trusted, go to the function
    :param application_id: Application id
    :param function: function to be decorated
    :return: the function or 404
    """
    def func(request, application_id, *args, **kwargs):
        if (application_id and function and
                Application.objects.filter(id=application_id, trusted=True).exists()):
            return function(request, application_id, *args, **kwargs)
        return HttpResponseNotFound("Application does not exists or is not trusted")
    return func
