from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth import views as auth_views

class TargetBase(models.Model):
    moviecd = models.IntegerField(db_column='movieCd', primary_key=True)  # Field name made lowercase.
    movienm = models.TextField(db_column='movieNm', blank=True, null=True)  # Field name made lowercase.
    opendt = models.DateTimeField(db_column='openDt', blank=True, null=True)  # Field name made lowercase.
    salesacc = models.BigIntegerField(db_column='salesAcc', blank=True, null=True)  # Field name made lowercase.
    audiacc = models.IntegerField(db_column='audiAcc', blank=True, null=True)  # Field name made lowercase.
    genre = models.TextField(blank=True, null=True)
    director = models.TextField(blank=True, null=True)
    nations = models.TextField(blank=True, null=True)
    actor1 = models.TextField(blank=True, null=True)
    actor2 = models.TextField(blank=True, null=True)
    actor3 = models.TextField(blank=True, null=True)
    audit = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        # db_table = 'target_bases'

class SelectedBase(models.Model):
    director = models.TextField(blank=True, null=True)
    genre = models.TextField(blank=True, null=True)
    nations = models.TextField(blank=True, null=True)
    audit = models.TextField(blank=True, null=True)
    actor1 = models.TextField(blank=True, null=True)
    actor2 = models.TextField(blank=True, null=True)
    actor3 = models.TextField(blank=True, null=True)
    opendt = models.TextField(blank=True, null=True)
    writer = models.ForeignKey(auth_views.UserModel, on_delete=models.CASCADE)


class Actorlist(models.Model):
    actor1 = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'actorlist'
