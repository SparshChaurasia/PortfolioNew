from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render

from .models import ContactForm


def index(request):
    return render(request, "index.html")

def submit_contact_form(request):
    if request.method != "POST":
        return HttpResponse("Invalid request method")

    username = request.POST.get("username")
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    message = request.POST.get("message")

    if not all((username, email, message)):
        messages.error(request, "Missing required fields")
        return redirect("/#contact")

    form = ContactForm(
        Username=username,
        Email=email,
        Subject=subject,
        Message=message
    )
    form.save()
    messages.success(request, "Your form was successfully submitted")
    return redirect("/#contact")
