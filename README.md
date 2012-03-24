#Reutilizando métodos clean para vários forms com Django


###Como fazer validação de negócios de todo o sistema em Django?

	O Django possui algumas particularidades. No Model deve ficar a lógica de negócio e os Forms devem validar as regras de negocio.

#### Qual a diferença entre lógica de negócio e regra de negócio

	Vou tocar nesse tópico apenas porque notei uma grande dificuldades nessa separação durante um tempo nos profissionais que tive contato.


1. Qual é a Lógica de negocio de um Bar ?
--------------------------------------------------------
Produtos divididos por categorias e subcategoria, com descrição e valor de compra e valor de venda. 

		 1. Bebidas 
				1.1 Refrigerante 1L
					1.1.1 Coca Cola
					1.1.2 Sprite
					1.1.3 Fanta
				1.2 Refrigerantes 300ml
					1.2.1 Coca Cola
					1.2.2 Sprite
					1.2.3 Fanta 	

Como eu poderia fazer algo assim em Django ?

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
--------------------------------------------------------

2. Quais são as Regras de negocio do Bar ?
--------------------------------------------------------
	Agora pense que vc possui uma regra para vender refrigerante, cerveja, cigarro, lanches e salgados.

	- Refrigerantes - pode ser vendido para todos
	- Cerveja - pode ser vendido apenas para maiores de 18 anos e gelada
	- Cigarro - pode ser vendido apenas para maiores de 18 anos
	- Salgado - Pode ser vendido para qualquer um
	- Lanche - pode ser vendido para qualquer um 

	Essas regras devem estar definidas no Form do Django. Mas eu tenho regras em comum, entre meus produtos e gostaria de centralizar essas regras para facilitar a reutilização do meu código. E também pode acontecer de eu montar um bar em outro pais essas regras podem mudar de acordo com o estado ou pais.  Sendo assim, eu não posso colocar essas definições no model.
--------------------------------------------------------

Como ficaria em Django

	class BaseSoParaMaioresForm(forms.BaseForm):
   		def clean_user(self):
        	user = self.cleaned_data.get('user')
        	if user:
            	user.get_profile.age < 18:
            	raise forms.ValidateErros(u"É proibida a venda de bebidas para menores de 18 anos no Brasil")


	class CervejaForm(forms.ModelForm, BaseSoParaMaioresForm):
   		class Meta:
       	model = Venda

		def __init__(self):
			self.fields['produto'] = Produto.objects.filter(categoria__nome='Bebidas', subcategoria__nome='Cerveja')

	class CigarroForm(forms.ModelForm, BaseSoParaMaioresForm):
   		class Meta:
       	model = Venda

		def __init__(self):
			self.fields['produto'] = Produto.objects.filter(categoria__nome='Outros', subcategoria__nome='Cigarro')