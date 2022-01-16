from django.db import models

class Review(models.Model):
    id_review = models.CharField(db_column='id_Review', primary_key=True, max_length=5)  # Field name made lowercase.
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    auth_user = models.ForeignKey('accounts.AuthUser', models.DO_NOTHING)
    store_id_store = models.ForeignKey('markets.Store', models.DO_NOTHING, db_column='Store_id_Store')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Review'
