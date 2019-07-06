from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class InputMessage(models.Model):

    name = models.CharField(max_length=50)
    body = models.CharField(max_length=100)
    channel = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %y')



