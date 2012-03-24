#!/usr/bin/env python
# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
	nome = models.CharField(max_length=100)
	
	def __unicode__(self):
	    return self.nome


class Subcategoria(models.Model):
	categoria = models.ForeignKey(Categoria)
	nome = models.CharField(max_length=100)

	def __unicode__(self):
	    return self.nome


class Produto(models.Model):
	categoria = models.ForeignKey(Categoria)
	subcategoria = models.ForeignKey(Subcategoria)
	nome = models.CharField(max_length=255)
	descricao = models.TextField(null=True, blank=True)
	custo = models.DecimalField(max_digits=5, decimal_places=2)
	valor = models.DecimalField(max_digits=5, decimal_places=2)

	def __unicode__(self):
	    return "%s | %s - %s" % (self.categoria, self.subcategoria, self.nome)
	    
	    
class Venda(models.Model):
    comprador = models.ForeignKey(User)
    produto = models.ForeignKey(Produto)
    data_de_venda = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return '%s - %s - %s' % (self.comprador, self.produto, self.data_de_venda) 