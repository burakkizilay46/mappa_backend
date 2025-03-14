from django.shortcuts import get_object_or_404
from people.models import OrdinaryPerson
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrdinarySerializer


# Create your views here.
@api_view(["GET"])
def get_ordinary_people(request):
    try:
        ordinaries = OrdinaryPerson.objects.all()
        serialized_ordinaries = OrdinarySerializer(ordinaries, many=True).data
        return Response(serialized_ordinaries, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(["GET"])
def get_ordinary_byid(request, id):
    try:
        person = OrdinaryPerson.objects.get(id=id)
        serialized_person = OrdinarySerializer(person, many=False).data
        return Response(serialized_person, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(["POST"])
def create_ordinary_person(request):
    try:
        serializer = OrdinarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(["DELETE"])
def delete_ordinary_person(request, id):
    person = get_object_or_404(OrdinaryPerson, id=id)
    person.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["PUT"])
def update_ordinary_person(request, id):
    person = get_object_or_404(OrdinaryPerson, id=id)
    serializer = OrdinarySerializer(instance=person, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
