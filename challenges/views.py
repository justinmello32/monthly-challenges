from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat not meat"
    elif month == "fabruary":
        challenge_text = "Something else"
    else:
        return HttpResponseNotFound("This month is not supported")

    return HttpResponse("Something")