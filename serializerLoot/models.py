from django.db import models

# Create your models here.

class Loots( models.Model ):
	SIZE_LOOT = [
		('S','Маленький подарок'),
		('M','Большой подарок'),
		('B','Огромный подарок'),
	]
	name =	models.CharField(max_length=120, blank=False, null=False, unique=True, ) 
	slug = models.SlugField(max_length=120, blank=False, null=False, unique=True )
	img = models.ImageField(upload_to='img/', blank=False, null=False)
	size_loot = models.CharField( max_length=1, choices = SIZE_LOOT, default='S')
	descr = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2 )

	data = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-data']

	def __str__(self):
		return self.name 



class Ordering( models.Model ):
	f_name = models.CharField(max_length=120, blank=True, null=False, default='fast')
	s_name = models.CharField(max_length=120, blank=True, null=False, default='fast')
	phone = models.CharField(max_length =13 , blank=False, null=False)
	e_mail = models.EmailField(max_length=120, blank=True, null=False, default='fast@gmail.com')
	choose = models.ForeignKey(Loots, on_delete = models.CASCADE, blank=True, null=True)

	data = models.DateTimeField(auto_now_add=True )

	class Meta:
		ordering = ['-data']

	def __str__(self):
		return '{} {} - {}'.format(self.f_name, self.s_name, self.phone)
