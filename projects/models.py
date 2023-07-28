from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=1000, verbose_name="Project Title")
    reb_num = models.CharField(max_length=1000, verbose_name="REB Number")
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Returns the url to access a particular project instance."""
        return reverse('project-detail', args=[str(self.id)])

