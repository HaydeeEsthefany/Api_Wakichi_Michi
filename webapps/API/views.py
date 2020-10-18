from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.status import HTTP_201_CREATED, HTTP_503_SERVICE_UNAVAILABLE
from rest_framework.exceptions import NotFound, ValidationError, APIException
from rest_framework.permissions import IsAuthenticated  #

from django.http import  HttpResponseRedirect
from django.shortcuts import reverse

class HTTPAPIException(APIException):
    permission_classes = (IsAuthenticated,) 
    status_code = HTTP_503_SERVICE_UNAVAILABLE
    default_detail = 'Internal API call to euro-dollar API failed'
    default_code = 'Internal API call to euro-dollar API failed'

def bad_request():
    return      {        'success': False     }  



def accepted():
    return      {        'success': True      }  
 
