from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50, blank=False)
    created = models.DateField(auto_now_add=True)
    group = models.ForeignKey('Group', blank=True, null=True, on_delete=models.PROTECT)



    def __str__(self):
        return f"{self.username}"
