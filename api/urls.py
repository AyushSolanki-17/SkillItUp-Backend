
from django.urls import path
from . import views

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'domains', views.DomainViewSet, basename='domains')
router.register(r'subdomains', views.SubDomainViewSet, basename='subdomains')
router.register(r'topics', views.SubDomainViewSet, basename='subdomains')
router.register(r'', views.SubDomainViewSet, basename='subdomains')
urlpatterns = router.urls
