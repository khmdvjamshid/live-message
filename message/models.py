from django.db import models

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.message