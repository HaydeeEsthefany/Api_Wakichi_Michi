from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

from webapps.API.controllers.user_controller import  UserView
from django.contrib import admin
from django.urls import path
schema_view = get_swagger_view(title='API')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('checkserver/', UserView.index, name='index'),
    path('auth/', include('webapps.API.urls')),
    url(r'^api/docs/$', schema_view),
    url(r'^api/', include('webapps.API.urls')),

 #   path('api/', include(('webapps.API.urls', 'users'), namespace='users')),
]
