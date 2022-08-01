from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(response):
    now = datetime.now()
    return render(response, "newyear/index.html", {
        "newyear" : now.month == 1 and now.day == 1,
        "now" :now
    })