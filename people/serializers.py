from rest_framework import serializers
from .models import (
    Ethnicity,
    Religion,
    Profession,
    WrittenSource,
    OrdinaryPerson,
    UnordinaryPerson,
)


class EthnicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethnicity
        fields = ["id", "name"]


class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = ["id", "name"]


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ["id", "name"]


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrittenSource
        fields = ["id", "name"]


class OrdinarySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    ethnicity = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Ethnicity.objects.all()
    )
    religion = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Religion.objects.all()
    )
    profession = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Profession.objects.all()
    )
    sources = serializers.PrimaryKeyRelatedField(
        many=True, queryset=WrittenSource.objects.all()
    )

    class Meta:
        model = OrdinaryPerson
        fields = [
            "id",
            "name",
            "alternate_name",
            "birth_year",
            "death_year",
            "description",
            "probable_birth_date",
            "probable_death_date",
            "ethnicity",
            "religion",
            "profession",
            "sources",
            "religion_explanation",
            "profession_explanation",
            "interesting_feature",
            "interaction_with_ordinary_explanation",
            "interaction_with_unordinary_explanation",
            "biography",
            "description_in_the_source",
            "explanation_of_ethnicity",
        ]


class UnordinarySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    ethnicity = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Ethnicity.objects.all()
    )
    religion = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Religion.objects.all()
    )
    profession = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Profession.objects.all()
    )
    sources = serializers.PrimaryKeyRelatedField(
        many=True, queryset=WrittenSource.objects.all()
    )

    class Meta:
        model = UnordinaryPerson
        fields = [
            "id",
            "name",
            "alternate_name",
            "birth_year",
            "death_year",
            "description",
            "probable_birth_date",
            "probable_death_date",
            "ethnicity",
            "religion",
            "profession",
            "sources",
        ]
