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
