from django.urls import path
from .views import IndexView, SobreView, UmlView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('uml/', UmlView.as_view(), name='uml'),
]