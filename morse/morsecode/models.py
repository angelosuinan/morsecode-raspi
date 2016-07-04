from django.db import models

# Create your models here.

class Message(models.Model):
    message_text = models.CharField(max_length=200)
    entry_date = models.DateTimeField("Entry date")
    def __str__(self):
        return self.message_text
class Letters(models.Model):
    m= Message()
    message = models.ForeignKey(Message,on_delete=models.CASCADE)
    letter_text  = models.CharField(max_length=1)
    def __str__(self):
        return self.letter_text

