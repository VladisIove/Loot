from rest_framework import serializers 

from .models import Loots, Ordering, FastOrdering


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
		fields = ('f_name', 's_name', 'phone','choose')

class FastOrderingSerializers(serializers.ModelSerializer ):
	""" Сериализация заказа """

	class Meta:
		model = FastOrdering 
		fields = ('phone',)