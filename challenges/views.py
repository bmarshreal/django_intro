import challenges
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the whole month!",
    "february": "Walk 10,000 steps/day!",
    "march": "Learn Django 20min every day!",
    "april": "Eat no meat for the whole month!",
    "may": "Walk 10,000 steps/day!",
    "june": "Learn Django 20min every day!",
    "july": "Eat no meat for the whole month!",
    "august": "Walk 10,000 steps/day!",
    "september": "Learn Django 20min every day!",
    "october": "Eat no meat for the whole month!",
    "november": "Walk 10,000 steps/day!",
    "december": "Learn Django 20min every day!",
}


test_data = {
    "Kaiden": "SugarBear!",
    "Brittany": "Mom",
    "Blake": "Dad",
    "Bane": "BlackCat",
    "Olivia": "OrangeCat"
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("INVALID MONTH")
    redirect_month = months[month - 1]
    # /challenge/ january
    # redirect_path using the reverse() function, will redirect the client to the path...
    # ...that we named "month-challenge" which is the path /challenges/<month>
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported!")


def monthly_challenge_list(request):
    try:
        list_items = ""
        months = list(monthly_challenges.keys())
        for month in months:
            capitalized_month = month.capitalize()
            month_path = reverse("month-challenge", args=[month])
            list_items += f"<li><a href = {month_path}> {capitalized_month}</a></li>"

        response_data = f"<ul>{list_items}</ul>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("Page not found!")
