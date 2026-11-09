from django.contrib import admin
from django.urls import path
from courses.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView, name='register'),
    path('courses/', RegisterView, name='courses'),
]
