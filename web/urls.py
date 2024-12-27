from django.urls import path
from .views import write_mail

urlpatterns = [
    path('wm/', write_mail, name='write_name' ),
    path(r'writemail/', write_mail , name='wm'),
]