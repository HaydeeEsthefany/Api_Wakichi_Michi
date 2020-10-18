# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from core.entities.user import UserEntity

def display_user_login_json(user,token):
    return {'id':user.id,                'username': user.username,      'fullname': user.fullname,         'children':user.children_format,      'email':user.email,
            'since':user.since,           'weeks':user.weeks,            'dir_ip':user.dir_ip,              
            'is_active':user.is_active,    'date_create':user.date_format, 'updated_at':user.updated_at,         
            'adult':user.adult,'token':token }



def display_user_json(user):
    return {'id':user.id,                'username': user.username,      'fullname': user.fullname,         'children':user.children_format,      'email':user.email,
    		'since':user.since,          'weeks':user.weeks,               'username_format':user.username_format,'dir_ip':user.dir_ip,           
    		'is_active':user.is_active,    'date_create':user.date_format, 'updated_at':user.updated_at,          'document':user.weeks,
            'adult':user.adult,   'languweeks': user.languweeks}


def display_user_xml(user):
    return ET.tostring(ET.Element("user", username=user.username,
                                  fullname=user.fullname,children=user.children))

def display_users_json(users):
    content = []
    for user in users:
        data=UserEntity( 
                    id              = user.id,
                    username        = user.username,
                    fullname        = user.fullname,
                    since           = user.since,
                    weeks           = user.weeks, 
                    email           = user.email,
                    children        = user.children,
                    dir_ip          = user.dir_ip, 
                    is_active       = user.is_active,  
                    created_at      = user.created_at
                )
        elem =  display_user_json(data)
        content.append(elem)
    return {'content': content}


