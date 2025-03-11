from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse


from people.models import OrdinaryPerson, UnordinaryPerson


# Create your views here.
@api_view(["GET"])
def getOrdinaryPeople(request):
    try:
        people = OrdinaryPerson.objects.all()
        data = list(people.values())
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)



@api_view(["GET"])
def getUnordinaryPeople(request):
    try:
        people = UnordinaryPerson.objects.all()
        data = list(people.values())
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
