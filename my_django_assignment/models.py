from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Teachers(models.Model):
    name = models.CharField(max_length = 30)
    course = models.CharField(max_length = 30)
    description = models.TextField()
    availability = models.CharField(max_length = 30)
    
    def __unicode__(self):
        return self.author
