from django.urls import path
from .views import write_mail

urlpatterns = [
    path(r'wm/', write_mail, name='write_name' ),
]