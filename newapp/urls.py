from django.conf.urls.static import static
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from project_exel import settings
from . import views

router = DefaultRouter()
router.register(r'employees', views.EmployeeModelViewSet, basename='employees')
# router.register(r'occurrences', views.OccurrenceModelViewSet, basename='occurrences')

urlpatterns = [
                  path('rest-auth/', include('rest_auth.urls')),
                  path('rest-auth/logout/', views.LogoutViewEx.as_view(), name='rest_logout'),
                  # path('rest-auth/test_auth/', views.EmployeeModelViewSet.i, name='test_auth', ),
                  path('upload/', views.FileUploadView.as_view(), name='upload'),
                  path('', views.HomeTemplateView.as_view(), name='home'),

              ] + static(settings.STATIC_URL)

urlpatterns += router.urls
