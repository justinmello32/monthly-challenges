from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "This is something for January",
    "february": "This is something for February",
    "march": "This is something for March",
    "april": "This is something for April",
    "may": "This is something for May",
    "june": "This is something for June",
    "july": "This is something for July",
    "august": "This is something for August",
    "september": "This is something for September",
    "october": "This is something for October",
    "november": "This is something for November",
    "december": "This is something for December",
}

# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")