# Generated by Django 4.2.13 on 2024-06-23 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='team',
            name='designation',
            field=models.CharField(max_length=255, verbose_name='Designation'),
        ),
        migrations.AlterField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='first_name',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Firstname'),
        ),
        migrations.AlterField(
            model_name='team',
            name='google_link',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='last_name',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Lastname'),
        ),
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter_link',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]
