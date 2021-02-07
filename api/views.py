from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import *
from api.serializers import *

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'api overview' : '',
		'create [POST]' : '/memes/',
		'list [GET]' : '/memes/',
		'list one [GET]' : '/memes/<int:id>',
	}

	return Response(api_urls)

@api_view(['GET','POST'])
def Memes(request):
	if request.method == "POST":
		serializer = memeSerializer(data = request.data)

		if serializer.is_valid():
			serializer.save()

		lastId = Meme.objects.latest('id')	
		jsonResp = {'id':lastId.pk}
		return JsonResponse(jsonResp)

	elif request.method == "GET":	
		allMemes = Meme.objects.all().order_by('-pk')[:100]
		serializer = memeSerializer(allMemes, many = True)
		return Response(serializer.data)

	else:
		return HttpResponse("")		

@api_view(['GET'])
def oneMeme(request, pk):	
	oneMeme = Meme.objects.get(pk=pk)
	serializer = memeSerializer(oneMeme, many = False)
	return Response(serializer.data)	


