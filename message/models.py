from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class InputMessage(models.Model):

    name = models.CharField(max_length=50)
    body = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default='2000-09-04 06:00:00.000000')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %y')
