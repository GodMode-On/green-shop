# -*- coding: utf-8 -*-

from django.db import models


class Post(models.Model):
    title = models.CharField("Назва", max_length=256)
    text = models.TextField("Текст")
    date_added = models.DateTimeField("Дата", auto_now_add=True)

    def __unicode__(self):
        return self.title
