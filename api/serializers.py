from rest_framework import serializers

from skillitupcore.models import *


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'


class SubDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDomain
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDomain
        fields = '__all__'


class EducationalInstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalInstitute
        fields = '__all__'


class TrendingTechITSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendingTechIT
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
