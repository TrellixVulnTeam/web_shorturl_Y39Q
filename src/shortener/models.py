from django.db import models
from .utils import code_generator, create_shortcode

# Create your models here.

class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = KirrURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):    # checking if the instance type from items is int
            qs = qs.order_by('-id')[:items]     # reverse order by id, or can do -url as well.

        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)                          #print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class KirrURL(models.Model):
    url         = models.CharField(max_length=220, )
    shortcode   = models.CharField(max_length=15, unique=True, blank=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    active      = models.BooleanField(default=True)
    # empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)   # manual entry for timestamp

    objects = KirrURLManager()


    def save(self, *args, **kwargs):    #overriding the save method from models
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)

    # class Meta:
    #     ordering = '-id'


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