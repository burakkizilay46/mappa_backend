from django.shortcuts import get_object_or_404
from people.models import OrdinaryPerson, UnordinaryPerson
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrdinarySerializer, UnordinarySerializer


# Create your views here.
@api_view(["GET"])
def get_ordinary_people(request):
    try:
        ordinaries = OrdinaryPerson.objects.all()
        serialized_ordinaries = OrdinarySerializer(ordinaries, many=True).data
        return Response(serialized_ordinaries, status=201)
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


@api_view(["GET", "DELETE", "PUT", "PATCH"])
def ordinary_person_detail(request, id):
    person = get_object_or_404(OrdinaryPerson, id=id)
    if request.method == "GET":
        serializer = OrdinarySerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method in ["PUT", "PATCH"]:
        serializer = OrdinarySerializer(
            instance=person, data=request.data, partial=(request.method == "PATCH")
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_unordinary_people(request):
    try:
        unordinaries = UnordinaryPerson.objects.all()
        serialized_unordinaries = UnordinarySerializer(unordinaries, many=True).data
        return Response(serialized_unordinaries, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(["POST"])
def create_unordinary_person(request):
    try:
        serializer = UnordinarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET", "DELETE", "PUT", "PATCH"])
def unordinary_person_detail(request, id):
    unordinary_person = get_object_or_404(UnordinaryPerson, id=id)
    if request.method == "GET":
        serializer = UnordinarySerializer(unordinary_person)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        unordinary_person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method in ["PUT", "PATCH"]:
        serializer = UnordinarySerializer(
            instance=unordinary_person,
            data=request.data,
            partial=(request.method == "PATCH"),
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
