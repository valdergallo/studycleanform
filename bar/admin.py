#!/usr/bin/env python
# encoding: utf-8
from django.contrib import admin
from bar.models import Categoria, Subcategoria, Produto


admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Produto)