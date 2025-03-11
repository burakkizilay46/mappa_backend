from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .models import WrittenSource,SecondarySource

from django.http import JsonResponse


# Create your views here.
@api_view(["GET"])
def getWrittenSources(request):
    try:
        sources = WrittenSource.objects.all()
        data = list(sources.values())
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@api_view(["GET"])
def getSecondarySources(request):
    try:
        sources = SecondarySource.objects.all()
        data = list(sources.values())
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
