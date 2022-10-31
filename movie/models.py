from django.db import models
from django.contrib.auth import models as auth_models

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
        managed = False
        db_table = 'target_base'

