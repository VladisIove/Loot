


from rest_framework import serializers 

from .models import Loots, Ordering


class LootsSerializer(serializers.ModelSerializer ):
	"""Сериализация лута"""

	class Meta:
		model = Loots 
		fields = ('name',
							'slug',
							'img',
							'size_loot',
							'descr',
							'price')

class OrderingSerializers(serializers.ModelSerializer ):
	""" Сериализация заказа """

	class Meta:
		model = Ordering 
		fields = ('f_name',
							's_name',
							'phone',
							'e_mail',
							'choose')