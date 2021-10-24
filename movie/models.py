from django.db import models
from django.core.files import File
import urllib
import os
# Create your models here.


# class Person(models.Model):
#    UNSPECIFIED = 'X'
#    FEMALE = 'F'
#    MALE = 'M'
#
#    GENDER_CHOICES = (
#        (FEMALE, 'Female'),
#        (MALE, 'Male'),
#        (UNSPECIFIED, 'Unknown')
#    )
#    first_name = models.CharField(max_length=200, blank=True)
#    last_name = models.CharField(max_length=200, blank=True)
#    gender = models.CharField(
#        max_length=1, choices=GENDER_CHOICES, default=UNSPECIFIED)
#
#    def __str__(self):
#       return '{} {}'.format(self.first_name, self.last_name)


class Movie(models.Model):
    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_PG13 = 3
    RATED_NC16 = 4
    RATED_M18 = 5
    RATED_R21 = 6
    RATINGS = (
        (NOT_RATED, 'NR - Not Rate'),
        (RATED_G, 'G - General Audiences'),
        (RATED_PG, 'PG – Parental Guidance Suggested'),
        (RATED_PG13, 'PG-13 – Parents Strongly Cautioned'),
        (RATED_NC16, 'NC-16 – No Children under 16'),
        (RATED_M18, 'M-18 – Restricted to persons 18 years and above'),
        (RATED_R21, 'R21 – Strictly for adults aged 21 and above')
    )
    movie_title = models.CharField(max_length=200, blank=True)
    release_date = models.DateField(blank=True)
    rating = models.IntegerField(
        choices=RATINGS, default=NOT_RATED)
    poster_url = models.URLField()
    synoposis = models.TextField()
    cast = models.TextField()
    #cast = models.ManyToManyField(to='Person', blank=True)

    def get_remote_image(self):
        if self.image_url:
            result = urllib.urlretrieve(self.image_url)
            self.image_file.save(
                os.path.basename(self.image_url),
                File(open(result[0]))
            )
            self.save()

    class Meta:
        ordering = ('release_date', 'movie_title')

    def __str__(self):
        return '{} {}'.format(self.movie_title, self.release_date)
