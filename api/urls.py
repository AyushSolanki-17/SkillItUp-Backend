
from django.urls import path
from . import views

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'domains', views.DomainViewSet, basename='domains')
router.register(r'subdomains', views.SubDomainViewSet, basename='subdomains')
router.register(r'topics', views.TopicViewSet, basename='topics')
router.register(r'professions', views.ProfessionViewSet, basename='proffesions')
router.register(r'courses', views.CourseViewSet, basename='courses')
router.register(r'trendingtechit', views.TrendingTechITViewSet, basename='trendingtechit')
router.register(r'reccomendationtest', views.ReccomendationTestViewSet, basename='trendingtechit')
urlpatterns = router.urls
