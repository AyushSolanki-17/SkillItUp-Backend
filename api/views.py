
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# Create your views here.
from skillitupcore.MLToDBMapper import MLToDBMapper
from api import mlpred
from api.serializers import *
from skillitupcore.models import *


class DomainViewSet(ViewSet):
    permission_classes = [AllowAny]
    queryset = Domain.objects.all()

    def list(self, request):
        try:
            serializer = DomainSerializer(self.queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"Error": "Domains not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = DomainSerializer(item)
            return Response(serializer.data)
        except:
            return Response({"Error": "Specified Domain not found"})


class SubDomainViewSet(ViewSet):
    queryset = SubDomain.objects.all()

    def list(self, request):
        try:
            serializer = SubDomainSerializer(self.queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"Error": "SubDomains not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = SubDomainSerializer(item)
            return Response(serializer.data)
        except:
            return Response({"Error": "Specified SubDomain not found"})


class TopicViewSet(ViewSet):
    queryset = Topic.objects.all()

    def list(self, request):
        try:
            serializer = TopicSerializer(self.queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"Error": "Topics not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = TopicSerializer(item)
            return Response(serializer.data)
        except:
            return Response({"Error": "Specified Topic not found"})


class ProfessionViewSet(ViewSet):
    queryset = Profession.objects.all()

    def list(self, request):
        try:
            serializer = ProfessionSerializer(self.queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"Error": "Professions not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = ProfessionSerializer(item)
            return Response(serializer.data)
        except:
            return Response({"Error": "Specified Profession not found"})


class CourseViewSet(ViewSet):
    queryset = Courses.objects.all()

    def list(self, request):
        try:
            self.queryset = self.queryset.all().order_by("-rating")
            serializer = CourseSerializer(self.queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"Error": "Courses not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = CourseSerializer(item)
            return Response(serializer.data)
        except:
            return Response({"Error": "Specified Course not found"})


class TrendingTechITViewSet(ViewSet):
    queryset = TrendingTechIT.objects.all()

    def list(self, request):
        try:
            self.queryset = self.queryset.all().order_by("popularity")
            serializer = TrendingTechITSerializer(self.queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"Error": "Trending Technologies not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = TrendingTechITSerializer(item)
            return Response(serializer.data)
        except:
            return Response({"Error": "Specified Technology not found"})


class ReccomendationTestViewSet(ViewSet):

    queryset = ReccomendationTest.objects.all()

    def list(self, request):
        try:
            self.queryset = self.queryset.all().order_by("date")
            serializer = ReccomendationTestSerializer(self.queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({"Error": "Records not found"})

    def retrieve(self, request, pk=None):
        try:
            item = get_object_or_404(self.queryset, pk=pk)
            serializer = ReccomendationTestSerializer(item)
            return Response(serializer.data)
        except:
            return Response({"Error": "Record not found"})

    def create(self, request):

        try:
            serializer = ReccomendationTestSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            pred = mlpred.model1predict(request.data)
            dbid = MLToDBMapper.mltodb(pred)
            profession = get_object_or_404(Profession.objects.all(), pk=dbid)
            serializer.validated_data["profession"] = profession
            serializer.save()
            pserializer = ProfessionSerializer(profession)
            data = {"suggested_job_id": dbid, "suggested_job": pserializer.data}
            return Response(data)
        except:
            return Response({"Error": "Data Integrity Error",})
