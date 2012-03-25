#forms.FormBase is very powerful to use common clean_fields on differents Django Forms

#### How i can recycle my clean_field on differents Forms?

	class BaseBurnForm(forms.BaseForm):
    	"""
    	I will need this cleans on all my project
    	"""
		def clean_char_null(self):
       		char_null = self.cleaned_data.get('char_null')
        		if len(char_null):
            		raise forms.ValidationError('This Field must be null')
        	return self.cleaned_data

    	def clean_char_50(self):
       		char_50 = self.cleaned_data.get('char_50')
       		if len(char_50) <= 10:
           		raise forms.ValidationError('This Field must have more than 10 char')
       		return self.cleaned_data

    	def clean_char_255(self):
       		char_255 = self.cleaned_data.get('char_255')
       		if len(char_255) <= 10:
           		raise forms.ValidationError('This Field must have more than 10 char')
        	return self.cleaned_data


	class BurnTextModelForm(forms.ModelForm, BaseBurnForm):
    	"""
    	char_255 = models.CharField(max_length=255, null=True, blank=True)
    	char_50 = models.CharField(max_length=50, null=True, blank=True)
    	"""
    	class Meta:
       		model = BurnTextNull


	class BurnTextForm(forms.Form, BaseBurnForm):
    	"""
    	One Simple Django Form with 2 fields
    	"""
    	char_null = forms.CharField(required=False)
    	char_50 = forms.CharField(max_length=50)

Easy and powerful :P