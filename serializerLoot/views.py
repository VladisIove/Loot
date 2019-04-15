from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import permissions 

from .models import Loots, Ordering
from .serializers import LootsSerializer,OrderingSerializers
# Create your views here.

class LootsView(APIView):
	def get(self, request):
		loots = Loots.objects.all()
		serializer = LootsSerializer(loots, many=True)
		return Response({"data": serializer.data})


class OrderingView(APIView):
	def get(self, request):
		order = Ordering.objects.all()
		serializer = OrderingSerializers(order, many=True)
		return Response({"data": serializer.data})


	def post(self, request):
		order = OrderingSerializers(data = request.data)
		if order.is_valid():
			order.save()
			return Response({"status": "Add"})
		else:
			return Response({"status": "Error"})
