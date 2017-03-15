from django.conf.urls import url, include
from reminder import views
from rest_framework.routers import DefaultRouter

#Create Router to automatically detect URL's and register ReminderViewSet with it.
router = DefaultRouter()
router.register(r'reminders', views.ReminderViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
