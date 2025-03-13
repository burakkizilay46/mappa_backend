from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from people.models import OrdinaryPerson, UnordinaryPerson
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from source.models import WrittenSource
from .models import Ethnicity, Gender, Profession, Religion


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
def getOrdinaryPeopleById(request, id):
    print(request)
    try:
        ordinary_person = OrdinaryPerson.objects.get(id=id)
        data = {
            "name": ordinary_person.name,
            "alternate_name": ordinary_person.alternate_name,
            "birth_year": ordinary_person.birth_year,
            "death_year": ordinary_person.death_year,
            "description": ordinary_person.description,
            "probable_birth_date": ordinary_person.probable_birth_date,
            "probable_death_date": ordinary_person.probable_death_date,
            "religion_explanation": ordinary_person.religion_explanation,
            "profession_explanation": ordinary_person.profession_explanation,
        }
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@api_view(["POST"])
def createOrdinaryPeople(request):
    try:
        # Extract data from the request
        data = {
            "name": request.data["name"],
            "alternate_name": request.data["alternate_name"],
            "birth_year": request.data["birth_year"],
            "death_year": request.data["death_year"],
            "description": request.data["description"],
            "probable_birth_date": request.data["probable_birth_date"],
            "probable_death_date": request.data["probable_death_date"],
            "religion_explanation": request.data["religion_explanation"],
            "profession_explanation": request.data["profession_explanation"],
        }

        # Handle ForeignKey and ManyToMany relationships
        ethnicity_id = request.data.get("ethnicity")
        religion_ids = request.data.get("religion", [])
        gender_id = request.data.get("gender")
        profession_id = request.data.get("profession")
        source_id = request.data.get("sources")

        # Handle the ForeignKey and ManyToMany relationships
        if ethnicity_id:
            data["ethnicity"] = Ethnicity.objects.get(id=ethnicity_id)
        if religion_ids:
            data["religion"] = Religion.objects.filter(id__in=religion_ids)
        if gender_id:
            data["gender"] = Gender.objects.get(id=gender_id)
        if profession_id:
            data["profession"] = Profession.objects.get(id=profession_id)
        if source_id:
            data["sources"] = WrittenSource.objects.get(id=source_id)

        # Create the OrdinaryPerson instance
        ordinary_person = OrdinaryPerson.objects.create(**data)

        # Return the response with the ID of the created OrdinaryPerson
        return JsonResponse({"id": ordinary_person.id}, status=201)

    except KeyError as e:
        return JsonResponse({"error": f"Missing required field: {str(e)}"}, status=400)
    except Ethnicity.DoesNotExist:
        return JsonResponse({"error": "Ethnicity not found"}, status=400)
    except Religion.DoesNotExist:
        return JsonResponse({"error": "Religion not found"}, status=400)
    except Gender.DoesNotExist:
        return JsonResponse({"error": "Gender not found"}, status=400)
    except Profession.DoesNotExist:
        return JsonResponse({"error": "Profession not found"}, status=400)
    except WrittenSource.DoesNotExist:
        return JsonResponse({"error": "WrittenSource not found"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@api_view(["DELETE"])
def deleteOrdinaryPeople(request, id):
    try:
        ordinary_person = get_object_or_404(OrdinaryPerson, id=id)
        ordinary_person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
def updateOrdinaryPeople(request, id):
    try:
        person = get_object_or_404(OrdinaryPerson, id=id)
        data = request.data.copy()

        # Zorunlu alan kontrolü
        required_fields = ["name", "birth_year"]
        missing = [field for field in required_fields if field not in data]
        if missing:
            return JsonResponse({"error": f"Eksik alanlar: {missing}"}, status=400)

        # Nullable alanlar
        nullable_fields = ["death_year", "probable_death_date"]
        for field in nullable_fields:
            if field in data and data[field] is None:
                setattr(person, field, None)

        # Güncelleme
        for field, value in data.items():
            setattr(person, field, value)

        person.save()

        return JsonResponse({"id": person.id, "message": "Güncellendi"}, status=200)

    except Exception as e:
        return JsonResponse(
            {"error": "Sunucu hatası. Detaylar için logları kontrol edin."}, status=500
        )


@api_view(["GET"])
def getUnordinaryPeople(request):
    try:
        people = UnordinaryPerson.objects.all()
        data = list(people.values())
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@api_view(["GET"])
def getUnordinaryPeopleById(request, id):
    try:
        unordinary_person = UnordinaryPerson.objects.get(id=id)
        data = {
            "name": unordinary_person.name,
            "alternate_name": unordinary_person.alternate_name,
            "birth_year": unordinary_person.birth_year,
            "death_year": unordinary_person.death_year,
            "description": unordinary_person.description,
            "probable_birth_date": unordinary_person.probable_birth_date,
            "probable_death_date": unordinary_person.probable_death_date,
            "interesting_feature": unordinary_person.interesting_feature,
            "interaction_with_ordinary_explanation": unordinary_person.interaction_with_ordinary_explanation,
            "interaction_with_unordinary_explanation": unordinary_person.interaction_with_unordinary_explanation,
            "biography": unordinary_person.biography,
            "description_in_the_source": unordinary_person.description_in_the_source,
            "explanation_of_ethnicity": unordinary_person.explanation,
        }
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@api_view(["POST"])
def createUnordinaryPeople(request):
    try:
        # Collect basic fields, using get() for optional ones
        data = {
            "name": request.data["name"],  # Required field
            "alternate_name": request.data.get("alternate_name", ""),
            "birth_year": request.data.get("birth_year"),
            "death_year": request.data.get("death_year"),
            "description": request.data.get("description", ""),
            "probable_birth_date": request.data.get("probable_birth_date"),
            "probable_death_date": request.data.get("probable_death_date"),
        }

        # Handle ForeignKey relationships
        gender_id = request.data.get("gender")
        ethnicity_id = request.data.get("ethnicity")
        profession_id = request.data.get("profession")
        source_id = request.data.get("sources")

        if gender_id:
            data["gender"] = Gender.objects.get(id=gender_id)
        if ethnicity_id:
            data["ethnicity"] = Ethnicity.objects.get(id=ethnicity_id)
        if profession_id:
            data["profession"] = Profession.objects.get(id=profession_id)
        if source_id:
            data["sources"] = WrittenSource.objects.get(id=source_id)

        # Create the UnordinaryPerson instance without ManyToMany fields
        person = UnordinaryPerson.objects.create(**data)

        # Handle ManyToMany field for religion
        religion_ids = request.data.get("religion", [])
        if religion_ids:
            if not isinstance(religion_ids, list):
                return JsonResponse(
                    {"error": "Religion must be a list of IDs"}, status=400
                )
            religions = Religion.objects.filter(id__in=religion_ids)
            person.religion.set(religions)

        # Return a proper dictionary with the ID
        return JsonResponse({"id": person.id}, status=201)

    except KeyError as e:
        return JsonResponse({"error": f"Missing required field: {str(e)}"}, status=400)
    except (
        Gender.DoesNotExist,
        Ethnicity.DoesNotExist,
        Profession.DoesNotExist,
        WrittenSource.DoesNotExist,
        Religion.DoesNotExist,
    ) as e:
        return JsonResponse(
            {"error": f"Related object not found: {str(e)}"}, status=404
        )
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@api_view(["DELETE"])
def deleteUnordinaryPeople(request, id):
    try:
        person = get_object_or_404(UnordinaryPerson, id=id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
