from django.db import models


# Create your models here.
class Flames(models.Model):
    name1 = models.CharField(max_length=50, null=True)
    name2 = models.CharField(max_length=50, null=True)
    result = models.CharField(max_length=20, null=True)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Flames"