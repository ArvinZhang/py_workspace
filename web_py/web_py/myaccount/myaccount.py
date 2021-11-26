#python3

from  django.http import HttpResponse


def mycount_info(reuqest):
    return  HttpResponse("this is myaccount ")

