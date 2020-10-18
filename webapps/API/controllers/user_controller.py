from core.presentation.user import display_user_json, display_user_xml, display_users_json,display_user_login_json
from infrastructure.django_repository.user import UserRecords

from webapps.API.views import *
from datetime import datetime
from rest_framework.authtoken.models import Token


from rest_framework_jwt.settings import api_settings

from webapps.API.signals import send_email_token_bbva

class UserView(APIView):
    @api_view(['GET'])
    def index(request):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        message = 'server is live current time is '
        return Response(data=message + date , status= status.HTTP_200_OK)

 
	#Controlador para solicitar la recuperación de la password
    @api_view(['POST'])
    @permission_classes((permissions.AllowAny,))
    def send_email(request):

        since = datetime.strptime(request.data['since'], '%d/%m/%Y')
        user    = UserRecords.create(request.data['fullname'],since,
                                    request.data['weeks'],request.data['adult'],request.data['children'],
                                    request.data['email'],request.data['dir_ip'])                
        if user is None:
            return Response({'success':False,'messages':'No existe email'})
        else:
          
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            send_email_token_bbva(        token=token,        email= request.data['email'])
            return Response({'success':True})

	 

	
    @api_view(['POST'])   
    def function(request):
	    user = UserRecords.get_by_id(request.data['user_id'])
	    if user is  None:
	    	raise NotFound(detail='No hay datos del usuario')
	    return Response(display_user_json(user))


	#Controlador para listar Usuarios
    @api_view(['GET'])        
    def users(request):  
        if request.query_params.get('filter_value') is None:
            filter_value=''
        else:
            filter_value= request.query_params.get('filter_value')
        user            = UserRecords.list_users(filter_value,0)         
        return Response(display_users_json(user))


	
	#Controlador para validar si existe número de documento
    @api_view(['GET'])
    @permission_classes((permissions.AllowAny,))
    def email_user(request,email):           
        user = UserRecords.get_by_email(email) 
        if user is None:
            return  Response({'success':False})
        else:            
            return  Response({'success':True})


    #API para agregar nuevo usuario
    @api_view(['POST'])    
    def add_user(request):
        if UserRecords.get_by_username_all(request.data['username']) is None:  
            if UserRecords.get_by_email(request.data['email']) is None:
                if UserRecords.get_by_document(request.data['document_n'],request.data['document_type_id']) is None:
                    user =  UserRecords.create(request.data['username'], request.data['first_name'],
												    		request.data['last_name'], request.data['email'],
												    		request.data['profile_id'], request.data['document_type_id'],
												    		request.data['document_n'],  datetime.strptime(request.data['birthday'], '%Y-%m-%d').date() ,
												    		request.data['gender'], request.data['passw'],
												    		request.data['user_create']) 
                    if user > 0:
                        return HttpResponseRedirect(reverse('add_access_profile' ,  args=(), kwargs={'user':user,'profile':request.data['profile_id'] ,'user_create':request.data['user_create']}  ))
                    else:
                       return Response({'success':False,'message':'No se pudo crear usuario'})  
                else:
                    return Response({'success':False,'message':'El número documento ya ha sido registrado'}) 
            else:
                return Response({'success':False,'message':'El email ya se encuentra en uso'}) 
        else:        
            return  Response({'success':False,'message':'El nombre de usuario ya se encuentra en uso'}) 




    #API para modificar  usuario
    @api_view(['POST'])    
    def update_user(request):
    	user =  UserRecords.update(request.data['user_id'],  request.data['username'],request.data['first_name'],
									    		request.data['last_name'], request.data['email'],
									    		request.data['profile_id'], request.data['document_type_id'],
									    		request.data['document_n'], datetime.strptime(request.data['birthday'], '%Y-%m-%d').date() ,
									    		request.data['gender'],   request.data['user_update']) 
    	return Response({'success':'success'})





	    
