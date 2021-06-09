from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "This is something here",
    "february": "This is something here",
    "march": "Something here",
    "april": "Something here",
    "may": "Something here",
    "june": "Something here",
    "july": "Something here",
    "august": "Something here",
    "september": "Something here",
    "october": "Something here",
    "november": "Something here",
    "december": "Something here",
}

# Create your views here.
def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponse("This month is not supported")