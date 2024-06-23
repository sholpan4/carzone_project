from django.db import models


class Team(models.Model):
    first_name = models.CharField(max_length=255, db_index=True, verbose_name='Firstname')
    last_name = models.CharField(max_length=255, db_index=True, verbose_name='Lastname')
    designation = models.CharField(max_length=255, verbose_name='Designation')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True, verbose_name='Photo')
    facebook_link = models.URLField(max_length=100, blank=True, null=True)
    twitter_link = models.URLField(max_length=100, blank=True, null=True)
    google_link = models.URLField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created Date')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
