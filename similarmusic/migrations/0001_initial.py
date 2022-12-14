# Generated by Django 4.0.4 on 2022-05-29 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('musicname_artist', models.CharField(blank=True, db_column='musicname & artist', max_length=255, null=True)),
                ('length', models.CharField(blank=True, max_length=255, null=True)),
                ('rms_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('rms_var', models.CharField(blank=True, max_length=255, null=True)),
                ('bpm', models.CharField(blank=True, max_length=255, null=True)),
                ('zero_crossing_rate_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('zero_crossing_rate_var', models.CharField(blank=True, max_length=255, null=True)),
                ('harmony_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('harmony_var', models.CharField(blank=True, max_length=255, null=True)),
                ('percussive_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('percussive_var', models.CharField(blank=True, max_length=255, null=True)),
                ('spectral_centroid_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('spectral_centroid_var', models.CharField(blank=True, max_length=255, null=True)),
                ('spectral_bandwidth_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('spectral_bandwidth_var', models.CharField(blank=True, max_length=255, null=True)),
                ('spectral_rolloff_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('spectral_rolloff_var', models.CharField(blank=True, max_length=255, null=True)),
                ('chroma_frequencies_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('chroma_frequencies_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc1_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc1_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc2_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc2_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc3_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc3_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc4_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc4_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc5_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc5_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc6_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc6_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc7_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc7_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc8_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc8_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc9_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc9_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc10_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc10_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc11_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc11_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc12_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc12_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc13_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc13_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc14_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc14_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc15_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc15_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc16_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc16_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc17_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc17_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc18_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc18_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc19_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc19_var', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc20_mean', models.CharField(blank=True, max_length=255, null=True)),
                ('mfcc20_var', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'project dataset',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('uploadedFile', models.FileField(upload_to='Uploaded Files/')),
                ('dateTimeOfUpload', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_title', models.CharField(max_length=300)),
                ('audio_file', models.FileField(upload_to='')),
            ],
        ),
    ]
