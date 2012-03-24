#!/usr/bin/env python
# encoding: utf-8
from django import forms
from bar.models import Categoria, Subcategoria, Produto


class BaseSimplesForm(forms.BaseForm):
   pass   
 
class BaseSoParaMaioresForm(forms.BaseForm):
    def clean_user(self):
        user = self.cleaned_data.get('user')
        if user:
            user.get_profile.age < 18:
            raise forms.ValidateErros(u"É proibida a venda de bebidas para menores de 18 anos no Brasil")
            

class RefrigeranteForm(forms.ModelForm, BaseNoLimitForm):
    class Meta:
        model = Venda
 