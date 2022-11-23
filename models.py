# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Capstone(models.Model):
    musicname_artist = models.TextField(db_column='musicname & artist', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    length = models.IntegerField(blank=True, null=True)
    rms_mean = models.FloatField(blank=True, null=True)
    rms_var = models.FloatField(blank=True, null=True)
    bpm = models.FloatField(blank=True, null=True)
    zero_crossing_rate_mean = models.FloatField(blank=True, null=True)
    zero_crossing_rate_var = models.FloatField(blank=True, null=True)
    harmony_mean = models.FloatField(blank=True, null=True)
    harmony_var = models.FloatField(blank=True, null=True)
    percussive_mean = models.FloatField(blank=True, null=True)
    percussive_var = models.FloatField(blank=True, null=True)
    spectral_centroid_mean = models.FloatField(blank=True, null=True)
    spectral_centroid_var = models.FloatField(blank=True, null=True)
    spectral_bandwidth_mean = models.FloatField(blank=True, null=True)
    spectral_bandwidth_var = models.FloatField(blank=True, null=True)
    spectral_rolloff_mean = models.FloatField(blank=True, null=True)
    spectral_rolloff_var = models.FloatField(blank=True, null=True)
    chroma_frequencies_mean = models.FloatField(blank=True, null=True)
    chroma_frequencies_var = models.FloatField(blank=True, null=True)
    mfcc1_mean = models.FloatField(blank=True, null=True)
    mfcc1_var = models.FloatField(blank=True, null=True)
    mfcc2_mean = models.FloatField(blank=True, null=True)
    mfcc2_var = models.FloatField(blank=True, null=True)
    mfcc3_mean = models.FloatField(blank=True, null=True)
    mfcc3_var = models.FloatField(blank=True, null=True)
    mfcc4_mean = models.FloatField(blank=True, null=True)
    mfcc4_var = models.FloatField(blank=True, null=True)
    mfcc5_mean = models.FloatField(blank=True, null=True)
    mfcc5_var = models.FloatField(blank=True, null=True)
    mfcc6_mean = models.FloatField(blank=True, null=True)
    mfcc6_var = models.FloatField(blank=True, null=True)
    mfcc7_mean = models.FloatField(blank=True, null=True)
    mfcc7_var = models.FloatField(blank=True, null=True)
    mfcc8_mean = models.FloatField(blank=True, null=True)
    mfcc8_var = models.FloatField(blank=True, null=True)
    mfcc9_mean = models.FloatField(blank=True, null=True)
    mfcc9_var = models.FloatField(blank=True, null=True)
    mfcc10_mean = models.FloatField(blank=True, null=True)
    mfcc10_var = models.FloatField(blank=True, null=True)
    mfcc11_mean = models.FloatField(blank=True, null=True)
    mfcc11_var = models.FloatField(blank=True, null=True)
    mfcc12_mean = models.FloatField(blank=True, null=True)
    mfcc12_var = models.FloatField(blank=True, null=True)
    mfcc13_mean = models.FloatField(blank=True, null=True)
    mfcc13_var = models.FloatField(blank=True, null=True)
    mfcc14_mean = models.FloatField(blank=True, null=True)
    mfcc14_var = models.FloatField(blank=True, null=True)
    mfcc15_mean = models.FloatField(blank=True, null=True)
    mfcc15_var = models.FloatField(blank=True, null=True)
    mfcc16_mean = models.FloatField(blank=True, null=True)
    mfcc16_var = models.FloatField(blank=True, null=True)
    mfcc17_mean = models.FloatField(blank=True, null=True)
    mfcc17_var = models.FloatField(blank=True, null=True)
    mfcc18_mean = models.FloatField(blank=True, null=True)
    mfcc18_var = models.FloatField(blank=True, null=True)
    mfcc19_mean = models.FloatField(blank=True, null=True)
    mfcc19_var = models.FloatField(blank=True, null=True)
    mfcc20_mean = models.FloatField(blank=True, null=True)
    mfcc20_var = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'capstone'


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


class SimilarmusicDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    uploadedfile = models.CharField(db_column='uploadedFile', max_length=100)  # Field name made lowercase.
    datetimeofupload = models.DateTimeField(db_column='dateTimeOfUpload')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'similarmusic_document'


class SimilarmusicMusic(models.Model):
    id = models.BigAutoField(primary_key=True)
    music_title = models.CharField(max_length=300)
    audio_file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'similarmusic_music'