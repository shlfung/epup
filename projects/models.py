from django.db import models
from django.conf import settings


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=1000, verbose_name="Project Title")
    reb_num = models.CharField(max_length=1000, verbose_name="REB Number")
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

