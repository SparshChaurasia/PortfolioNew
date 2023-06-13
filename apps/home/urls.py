from django.urls import path
from .views import index, submit_contact_form

urlpatterns = [
    path("", index),
    path("xbhgoriqtfnsmvbrtyfq", submit_contact_form, name="submit_contact_form")
]
