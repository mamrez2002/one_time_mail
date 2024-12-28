from django.urls import path
from .views import write_mail , index

urlpatterns = [
    path('', index , name='index' ),
    path('otm/', write_mail, name='write_mail' ),
]