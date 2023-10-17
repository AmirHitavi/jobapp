from django.shortcuts import render, redirect
from django.urls import reverse
from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm

# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    if request.method == "POST":
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            return redirect(reverse("thanks"))
    return render(request, "subscribe/subscribe.html", {"form": subscribe_form})

def thanks(request):
    return render(request, "subscribe/thanks.html", {})