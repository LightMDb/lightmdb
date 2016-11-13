from django.db import models


class Movie(models.Model):

    imdb_id = models.CharField(
        blank=False, null=False, max_length=10
    )

    title = models.CharField(
        _("Movie Title"), blank=False, null=False, max_length=100
    )

    language = models.CharField(
        _("Movie Language"), blank=True, null=True, max_length=20
    )

    release_date = models.DateField(
        _("Release Date"), blank=True, null=True
    )

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

