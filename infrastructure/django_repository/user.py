from django.core.exceptions import ObjectDoesNotExist
from infrastructure.models import  User
from core.entities.user import UserEntity
from django.db.models import Q
import hashlib
from datetime import datetime

class UserRecords:  

    @staticmethod
    def get_by_username(username):
        try: 
            user_orm = User.objects.get(username=username,is_active=True)
            return UserEntity( 
                    id             = user_orm.id,
                    fullname       = user_orm.first_name,
                    last_name      = user_orm.last_name,
                    document_n     = user_orm.document_n,
                    document_id    = user_orm.document_type.id,
                    email          = user_orm.email,
                    birthday       = user_orm.birthday,
                    gender         = user_orm.gender,
                    password       = user_orm.password,
                    access_nivel   = user_orm.access_nivel,
                    language       = user_orm.language,
                    is_active      = user_orm.is_active, 
                    created_at     = user_orm.created_at
                )
        except ObjectDoesNotExist:
            return 

    @staticmethod
    def get_by_username_in(username):
        try: 
            user_orm = User.objects.filter(username=username).first()
            return user_orm
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_by_username_all(username):
        try:
            user_orm = User.objects.get(username=username)
            return user_orm
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_by_id(id):
        try:
            user_orm = User.objects.filter(id=id).first()
            return UserEntity( 
                    id             = user_orm.id,
                    username       = user_orm.username,
                    first_name     = user_orm.first_name,
                    last_name      = user_orm.last_name,
                    document_n     = user_orm.document_n,
                    document_id    = user_orm.document_type.id,
                    email          = user_orm.email,
                    birthday       = user_orm.birthday,
                    gender         = user_orm.gender,
                    password       = user_orm.password,
                    access_nivel   = user_orm.access_nivel,
                    language       = user_orm.language,
                    is_active      = user_orm.is_active, 
                    created_at     = user_orm.created_at
                )
        except ObjectDoesNotExist:
            return None

        
 

    @staticmethod  
    def all_user():
        try:
            user_orm = User.objects.filter(is_active=True)
            return user_orm
        except ObjectDoesNotExist:
            return None
        

 

    @staticmethod
    def get_by_email(email):
        try:
            user_orm = User.objects.filter(email=email).first()
            if user_orm is not None:
                return UserEntity( 
                        id              = user_orm.id,
                        username        = user_orm.username,
                        first_name      = user_orm.first_name,
                        last_name       = user_orm.last_name,
                        document_n      = user_orm.document_n,
                        document_id     = user_orm.document_type.id,
                        email           = user_orm.email,
                        birthday        = user_orm.birthday,
                        gender          = user_orm.gender,
                        password        = user_orm.password,
                        access_nivel    = user_orm.access_nivel,
                        language        = user_orm.language,
                        is_active       = user_orm.is_active, 
                        created_at      = user_orm.created_at
                    )
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_by_document(document_n,document_type_id):
        try:
            user_orm = User.objects.filter(document_n=document_n,document_type_id=document_type_id).first()
            return user_orm
        except ObjectDoesNotExist:
            return None
        
    @staticmethod
    def get_by_token(token):
        try:
            user_orm = User.objects.filter(token=token).first()
            return user_orm
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def list_users():
        try:
            user_orm = User.objects.order_by()
            return user_orm
        except ObjectDoesNotExist:
            return None

 
    @staticmethod
    def new_password(user_id,password):
        user_orm = User.objects.get(id=user_id)
        user_orm.password = hashlib.md5(password.encode('utf-8')).hexdigest()
        user_orm.save()

    @staticmethod
    def create(fullname, since,weeks,adult,children,   email,dir_ip ):
       
        user_orm = User.objects.create(fullname=fullname, username=email,since=since, weeks=weeks,adult=adult,children=children, dir_ip=dir_ip, email=email)
         
        print('gaaa')
        if user_orm is None:
            return 0
        else:
            return user_orm

    @staticmethod
    def desactive(user_id,user_updated):
        user = User.objects.get(id=user_updated)
        user_orm = User.objects.filter(id=user_id).first()
        user_orm.is_active    = False
        user_orm.user_updated = user
        user_orm.save()

    @staticmethod
    def active(user_id,user_updated):
        user = User.objects.get(id=user_updated)
        user_orm = User.objects.filter(id=user_id).first()
        user_orm.is_active    = True
        user_orm.user_updated = user
        user_orm.save()


    @staticmethod
    def update(user_id, username,first_name,last_name, email, profile_id,document_type_id,document_n,birthday,gender,user_updated):
        user = User.objects.get(id=user_updated) 
        user_orm = User.objects.filter(id=user_id).first()
        user_orm.username           = username
        user_orm.first_name         = first_name
        user_orm.last_name          = last_name
        user_orm.email              = email
   
        user_orm.document_type_id   = document_type_id
        user_orm.document_n         = document_n
        user_orm.birthday           = birthday
        user_orm.gender             = gender
        user_orm.user_updated       = user 
        user_orm.updated_at        = datetime.now()
        user_orm.save()



    @staticmethod
    def update_validate(email,access):
        user_orm = User.objects.filter(email=email).first()    
        user_orm.access_nivel = access
        user_orm.save()



