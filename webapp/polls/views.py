import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.warning('Error demo1', exc_info=True)
    kwargs = {'a': 2, 'b': 1, 'c': 7}

    logger.debug("a = {a}, b = {b}".format(**kwargs))
    logger.info("Hypotenuse of {a}, {b} is {c}".format(**kwargs))
    logger.warning("a={a} and b={b} are equal".format(**kwargs))
    logger.error("a={a} and b={b} cannot be negative".format(**kwargs))
    logger.critical("Hypotenuse of {a}, {b} is {c}".format(**kwargs))
    return HttpResponse("Hello, world. You're at the polls index.")