from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=1000)
    reb_num = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)