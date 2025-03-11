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

from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import OrdinaryPerson, Ethnicity, Religion, Gender, Profession
from source.models import WrittenSource

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
            "explanation_of_ethnicity": unordinary_person.explanation
        }
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
