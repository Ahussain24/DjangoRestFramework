from django.db import models

# Create your models here.


class IPTables(models.Model):

    camID = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    protocol = models.CharField(max_length=10, blank=True)
    port = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=100, blank=False)

    verbose_name = "IPTables"
