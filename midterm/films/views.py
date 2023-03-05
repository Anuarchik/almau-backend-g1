from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from films.models import Film
from films.serializers import FilmSerializer
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def film1(request):
    if request.method == 'GET':
        categories = Film.objects.all()
        serializer = FilmSerializer(categories, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = FilmSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)


def get_film(pk):
    try:
        films = Film.objects.get(id=pk)
        return {
            'status': 200,
            'films': films
        }
    except Film.DoesNotExist as e:
        return {
            'status': 404,
            'films': None
        }


@csrf_exempt
def film2(request, pk):
    result = get_film(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'Films not found'}, status=404)

    films = result['films']

    if request.method == 'GET':
        serializer = FilmSerializer(films)
        return JsonResponse(serializer.data, status=200)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = FilmSerializer(data=data, instance=films)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data=serializer.errors, status=400)
    if request.method == 'DELETE':
        films.delete()
        return JsonResponse({'message': 'Films deleted successfully!'})
    return JsonResponse({'message': 'Request is not supported'}, status=400)

