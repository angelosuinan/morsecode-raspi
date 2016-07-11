from django.db import models

# Create your models here.

class Message(models.Model):
    message_text = models.CharField(max_length=200)
    entry_date = models.DateTimeField("Entry date")
    def __str__(self):
        return self.message_text
class Letter(models.Model):
    letter_text  = models.CharField(max_length=1)
    def __str__(self):
        return self.letter_text

