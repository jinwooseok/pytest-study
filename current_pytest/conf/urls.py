from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app1 import urls as app1_urls

router = routers.DefaultRouter()

for router_list in app1_urls.route_list:
    router.register(router_list[0], router_list[1]) 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]