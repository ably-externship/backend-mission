from django.db import models


class Qa(models.Model):
    id_qa = models.CharField(primary_key=True, max_length=5)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    auth_user = models.ForeignKey('accounts.AuthUser', models.DO_NOTHING)
    store_id_store = models.ForeignKey('markets.Store', models.DO_NOTHING, db_column='Store_id_Store')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QA'

