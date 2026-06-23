from django.db import models

# Create your models here.
class Features(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name
