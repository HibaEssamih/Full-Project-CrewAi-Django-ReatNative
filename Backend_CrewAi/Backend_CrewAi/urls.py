from django.urls import path
from .App.views import legal_query_view

urlpatterns = [
    path('api/legal_query/', legal_query_view, name='legal_query'),
]
