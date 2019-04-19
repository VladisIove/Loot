from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import permissions 
from django.utils.decorators import method_decorator



from .models import Loots, Ordering, FastOrdering
from .serializers import LootsSerializer,OrderingSerializers, FastOrderingSerializers
# Create your views here.

class LootsView(APIView):
	def get(self, request):
		loots = Loots.objects.all()
		serializer = LootsSerializer(loots, many=True)
		return Response({"data": serializer.data})


class OrderingView(APIView):
	permission_classes = (permissions.AllowAny, )

	def post(self, request):
		order = OrderingSerializers(data = request.data)
		print()
		print(order.is_valid())
		print()
		if order.is_valid():
			order.save()
			return Response({"status": "Add"})
		else:
			return Response({"status": "Error"})



class FastOrderingView(APIView):
	permission_classes = (permissions.AllowAny, )

	def post(self, request):
		order = FastOrderingSerializers(data = request.data)
		print()
		print(order.is_valid())
		print()
		if order.is_valid():
			order.save()
			return Response({"status": "Add"})
		else:
			return Response({"status": "Error"})