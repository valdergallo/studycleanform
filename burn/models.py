#!/usr/bin/env python
# encoding: utf-8
from django.db import models


class BurnTextNull(models.Model):
    char_255 = models.CharField(max_length=255, null=True, blank=True)
    char_50 = models.CharField(max_length=50, null=True, blank=True)
