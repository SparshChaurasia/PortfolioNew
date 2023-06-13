from django.db import models


class ContactForm(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Subject = models.CharField(max_length=100, null=True)
    Message = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Username
