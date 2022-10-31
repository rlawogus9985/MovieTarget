from django.db import models

class MovieBase(models.Model):
    movieCd = models.IntegerField()
    movieNm = models.TextField()
    openDt = models.DateTimeField()
    salesAcc = models.BigIntegerField()
    audiAcc = models.IntegerField()
    genre = models.TextField()
    director = models.TextField(null=True, blank=True)
    nations = models.TextField()
    actor1 = models.TextField(null=True, blank=True)
    actor2 = models.TextField(null=True, blank=True)
    actor3 = models.TextField(null=True, blank=True)
    audit = models.TextField()
