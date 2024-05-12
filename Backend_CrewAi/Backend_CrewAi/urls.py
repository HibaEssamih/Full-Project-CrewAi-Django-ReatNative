from django.urls import path
from .App.views import legal_assistance_check_view, simple_query_analysis_view, complex_tasks_view

urlpatterns = [
    path('api/legal_assistance_check/', legal_assistance_check_view, name='legal_assistance_check'),
    path('api/simple_query_analysis/', simple_query_analysis_view, name='simple_query_analysis'),
    path('api/complex_tasks/', complex_tasks_view, name='complex_tasks'),
]
