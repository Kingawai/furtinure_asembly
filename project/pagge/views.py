from django.shortcuts import render
from .models import *


def home_page(reguest):
    return render(
        reguest,
        'pagge/index.html',
        context={
            "navigation": Navigation.objects.all(),
            "main": Main.objects.all(),
            "galary": Galary.objects.all(),
            "advantages": Advantage.objects.all(),
            "advantagebody": AdvantageBody.objects.all(),
            "introduction": introduction.objects.all(),
            "footer": contact.objects.all()
        }
    )
