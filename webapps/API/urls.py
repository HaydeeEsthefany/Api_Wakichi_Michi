# -*- coding: utf-8 -*-
from django.conf.urls import url


from django.urls import path, include
 

from . import views 
from .controllers import user_controller,capturar_rostro



urlpatterns = [
 
    #User
    url(r'^user/id/(?P<user_id>\w+)/$',                             user_controller.UserView.as_view(),        name='user'),
    url(r'^user/edit/$',                                            user_controller.UserView.update_user,      name='update_user'),
    url(r'^user/new/$',                                             user_controller.UserView.add_user,         name='add_user'),
    url(r'^user/email/(?P<email>.*)/$',                             user_controller.UserView.email_user,       name='add_user'),
    url(r'^user/list/$',                                            user_controller.UserView.users,            name='users'),
    url(r'^user/send/email/$',                                      user_controller.UserView.send_email,       name='send_email'),
    url(r'^capture/image/$',                                        capturar_rostro.CaptureView.capture,       name='capture'),
    


]
