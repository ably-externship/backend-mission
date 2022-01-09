from django.db import models

class Markets(models.Model):
    idx = models.IntegerField(db_column='Idx', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Markets'


class Onepiece(models.Model):
    id = models.IntegerField(primary_key=True)
    prodname = models.CharField(db_column='ProdName', max_length=20)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=20)  # Field name made lowercase.
    marketidx = models.IntegerField(db_column='MarketIdx')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnePiece'


class Outwear(models.Model):
    id = models.IntegerField(primary_key=True)
    prodname = models.CharField(db_column='ProdName', max_length=20)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=20)  # Field name made lowercase.
    marketidx = models.IntegerField(db_column='MarketIdx')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Outwear'


class Pants(models.Model):
    id = models.IntegerField(primary_key=True)
    prodname = models.CharField(db_column='ProdName', max_length=20)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=20)  # Field name made lowercase.
    marketidx = models.IntegerField(db_column='MarketIdx')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pants'


class Skirt(models.Model):
    id = models.IntegerField(primary_key=True)
    prodname = models.CharField(db_column='ProdName', max_length=20)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=20)  # Field name made lowercase.
    marketidx = models.IntegerField(db_column='MarketIdx')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Skirt'


class Top(models.Model):
    id = models.IntegerField(primary_key=True)
    prodname = models.CharField(db_column='ProdName', max_length=20)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=20)  # Field name made lowercase.
    marketidx = models.IntegerField(db_column='MarketIdx')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TOP'


class Qna(models.Model):
    category = models.CharField(db_column='Category', max_length=20)  # Field name made lowercase.
    prod_id = models.IntegerField()
    content = models.CharField(db_column='Content', max_length=300)  # Field name made lowercase.
    writer = models.CharField(max_length=20)
    title = models.CharField(db_column='Title', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QnA'