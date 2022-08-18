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
        model = Topic
        fields = '__all__'


class EducationalInstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalInstitute
        fields = '__all__'


class TrendingTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendingTech
        fields = '__all__'


class TrendingToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendingTool
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class RecommendationTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationTest
        fields = "__all__"


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = "__all__"

