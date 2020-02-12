# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import os
from django.db import models


def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # change filename to take Title of Product
    print(instance)
    print(filename)
    new_filename = random.randint(1, 342341242)
    name, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)

    def active(self):
        return self.filter(active=True)


class ProductManager(models.Manager):
    def get_query_set(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_query_set().active()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def features(self):
        return self.get_queryset().featured()


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)  #blank means its not required in django admin
    # upload to path is MEDIA_ROOT/products/ where MEDIA_ROOT is mentioned in settings
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = ProductManager()

    def __str__(self):
        return self.title