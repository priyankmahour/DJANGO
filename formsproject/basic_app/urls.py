from django.conf.urls import url
from basic_app import views

app_name="basic_app"

urlpatterns=[
              url(r'^register/',views.register_view,name="register_view"),
]
