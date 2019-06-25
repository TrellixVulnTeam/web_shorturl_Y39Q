from django.db import models
import random
import string

# Create your models here.

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    new_code = ''
    for _ in range(size):
        new_code += random.choice(chars)
    return new_code
    # or can use
    # return ''.join(random.choice(chars) for _ in range(size))

class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)   # manual entry for timestamp


    def save(self, *args, **kwargs):
        print('something')
        self.shortcode = code_generator()
        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        " replace self.url with self.id for auto gen ID, or name it string "
        return str(self.url)

    def __unicode__(self):
        return str(self.url)































"""
python manage.py makemigrations
python manage.py migrate

delete dbsqlite3 for reset then:
python manage.py createsuperuser
"""