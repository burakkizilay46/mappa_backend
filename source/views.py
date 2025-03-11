from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .models import WrittenSources,SecondarySources

from django.http import JsonResponse


# Create your views here.
@api_view(["GET"])
def getWrittenSources(request):
    try:
        sources = WrittenSources.objects.all()
        data = list(sources.values())
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@api_view(["GET"])
def getSecondarySources(request):
    try:
        sources = SecondarySources.objects.all()
        data = list(sources.values())
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
