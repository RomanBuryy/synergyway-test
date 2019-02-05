from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"