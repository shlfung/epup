from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=1000, verbose_name="Project Title")
    reb_num = models.CharField(max_length=1000, verbose_name="REB Number")
    participant_expected_num = models.IntegerField(null=True, blank=True, default=0, verbose_name="Expected Number of Participants")
    expected_start_date = models.DateField(null=True, blank=True, default=None, verbose_name="Expected Start Date")
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Returns the url to access a particular project instance."""
        return reverse('project-detail', args=[str(self.id)])

