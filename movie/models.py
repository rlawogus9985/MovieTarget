from django.db import models
from django.contrib.auth import models as auth_models

class MovieBase(models.Model):
    movieCd = models.IntegerField(null=True)
    movieNm = models.TextField(null=True)
    openDt = models.DateTimeField(null=True)
    salesAcc = models.BigIntegerField(null=True)
    audiAcc = models.IntegerField(null=True)
    genre = models.TextField(null=True)
    director = models.TextField(null=True, blank=True)
    nations = models.TextField(null=True)
    actor1 = models.TextField(null=True, blank=True)
    actor2 = models.TextField(null=True, blank=True)
    actor3 = models.TextField(null=True, blank=True)
    audit = models.TextField(null=True)