from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "QUIT CONSUMING ADDED SUGAR",
    "february": "SET A LIMIT FOR YOUR SCREEN TIME AND STICK TO IT",
    "march": "KEEP A FOOD JOURNAL",
    "april": "AVOID ULTRA-PROCESSED SNACKS",
    "may": "EAT 5-6 SERVINGS OF FRUITS & VEGETABLES EVERY DAY",
    "june": "SLEEP FOR AT LEAST 7-8 HOURS EVERY DAY",
    "july": "TRY INTERMITTENT FASTING",
    "august": "WALK 5,000/8,000/10,000 STEPS A DAY",
    "september": "NO FAST FOOD OR TAKEAWAY",
    "october": "EAT AT LEAST ONE HOME COOKED MEAL A DAY",
    "november": "DRINK 8-10 GLASSES OF WATER A DAY",
    "december": None,
}


# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("This month is invalid !")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()