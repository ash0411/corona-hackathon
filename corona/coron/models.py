from django.db import models

# Create your models here.
class location(models.Model):
    ENTRY_CHOICES = (
        ('country','country'),
        ('city','city'),
        ('state','state'),
        ('ip','ip'),
        ('GPS','GPS')
    )
    FACILITY_CHOICES = (
        ('hotels','hotels'),
        ('restaurants','restaurants'),
        ('hospitals','hospitals'),
        ('grocery','grocery')
    )
    type_of_location = models.CharField(max_length = 7 , choices=ENTRY_CHOICES)
    location = models.CharField(max_length = 200,default='india')
    facility = models.CharField(max_length=30,default="restaurants")
    def _str_(self):
        return '{}, {}'.format(self.type_of_locatioin, self.location)