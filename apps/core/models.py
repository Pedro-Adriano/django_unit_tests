from django.db import models


class People(models.Model):
    name = models.CharField("Name", max_length=200)
    years = models.PositiveIntegerField("Years")

    def __str__(self):
        return self.name
