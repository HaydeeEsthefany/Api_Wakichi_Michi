import hashlib
import datetime


class UserEntity:
    def __init__(self,id,username,fullname, since,weeks,adult,children,	email,dir_ip, 
    		     	is_active  ,created_at	,updated_at  ):
        self.__id              = id
        self.__username        = username
        self.__fullname        = fullname
        self.__since           = since    	
        self.__weeks           = weeks
        self.__adult           = adult
        self.__email           = email 
        self.__children        = children
        self.__dir_ip          = dir_ip
        self.__is_active       = is_active
        self.__updated_at      = updated_at
        self.__created_at      = created_at
      
    @property
    def id(self):
        return self.__id   
    
    @property
    def pk(self):
        return self.__id   

    @property
    def username(self):
        return self.__username   

    @property
    def fullname(self):
        return self.__fullname

    @property
    def since(self):
        return self.__since


    @property
    def weeks(self):
        return self.__weeks

    @property
    def adult(self):
        return self.__adult

    @property
    def email(self):
        return self.__email

    @property
    def dir_ip(self):
        return self.__dir_ip

    @property
    def children(self):
        return self.__children


    @property
    def is_active(self):
        return self.__is_active



    @property
    def updated_at(self):
        return self.__updated_at

    @property
    def created_at(self):
        return self.__created_at


   

    @property
    def since_format(self):
        return self.__since.strftime('%Y-%m-%d')
    
    
    @property
    def date_format(self):
        return self.__created_at.strftime('%d/%m/%Y')


        