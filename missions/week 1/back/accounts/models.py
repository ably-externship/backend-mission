from django.db import models


class Item(models.Model):
    id_item = models.CharField(db_column='id_Item', primary_key=True, max_length=5)  # Field name made lowercase.
    색상 = models.CharField(max_length=45, blank=True, null=True)
    사이즈 = models.CharField(max_length=5, blank=True, null=True)
    사진 = models.TextField(blank=True, null=True)
    이름 = models.CharField(max_length=45, blank=True, null=True)
    가격 = models.IntegerField(blank=True, null=True)
    재고 = models.CharField(max_length=45, blank=True, null=True)
    id_store = models.ForeignKey('Store', models.DO_NOTHING, db_column='id_Store')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Item'


class QA(models.Model):
    idq_a = models.CharField(db_column='idQ&A', primary_key=True, max_length=5)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    제목 = models.CharField(max_length=45, blank=True, null=True)
    내용 = models.CharField(max_length=100, blank=True, null=True)
    날짜 = models.DateField(blank=True, null=True)
    댓글 = models.CharField(max_length=50, blank=True, null=True)
    쇼핑몰_id쇼핑몰 = models.ForeignKey('Store', models.DO_NOTHING, db_column='쇼핑몰_id쇼핑몰')
    유저_id유저 = models.ForeignKey('User', models.DO_NOTHING, db_column='유저_id유저')

    class Meta:
        managed = False
        db_table = 'Q&A'


class Review(models.Model):
    id_review = models.CharField(db_column='id_Review', primary_key=True, max_length=5)  # Field name made lowercase.
    제목 = models.CharField(max_length=45, blank=True, null=True)
    내용 = models.CharField(max_length=100, blank=True, null=True)
    날짜 = models.DateField(blank=True, null=True)
    id_store = models.ForeignKey('Store', models.DO_NOTHING, db_column='id_Store')  # Field name made lowercase.
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_User')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Review'


class Store(models.Model):
    id_store = models.CharField(db_column='id_Store', primary_key=True, max_length=5)  # Field name made lowercase.
    이름 = models.CharField(max_length=45, blank=True, null=True)
    설명 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Store'


class User(models.Model):
    id_user = models.CharField(db_column='id_User', primary_key=True, max_length=15)  # Field name made lowercase.
    이메일 = models.CharField(max_length=100, blank=True, null=True)
    패스워드 = models.CharField(max_length=40, blank=True, null=True)
    주소 = models.CharField(max_length=120, blank=True, null=True)
    닉네임 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'