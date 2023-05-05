# from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.query import QuerySet
from cms_app.serializer import UserSerializer\
                        ,PostSerializer\
                        ,LikeSerializer
from cms_app.models import User,Post,Like
from django.forms.models import model_to_dict
from django.db.models import Q,Count
# Create your views here.

class UserClass(APIView):
    def get(self,request):
        data = get_user(request.query_params.get('user_id'))
        if isinstance(data,User):
            return Response({"Response" : {"User_data" : model_to_dict(data)}})
        
        return Response({"Response" : {"User_data" : data}})
    
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"User Inserted":serializer.data})
    
    def put(self,request):
        user_obj = get_user(request.query_params.get('user_id'))
        
        if not isinstance(user_obj,User):
            return Response({"Response" : " User not found" })
        
        serializer = UserSerializer(user_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"User Updated":serializer.data})
        
    def delete(self,request):
        user_obj = get_user(request.query_params.get('user_id'))
        
        if not isinstance(user_obj,User):
            return Response({"Response" : " User not found" })
        
        user_obj.delete()
        return Response({"Response" : " User deleted" })
    


class PostClass(APIView):
    
    def get(self,request):
        data = get_post(user_id = request.query_params.get('user_id'))
        return Response({"Response" : {"Post data" :data}})
    
    def post(self,request):
        try:
            exist = get_user(request.data['user_id'])
            
            if not isinstance(exist,User):
                return Response({"Response":exist})
            
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Response" :{"Post Inserted":serializer.data}})
            
        except Exception as exc:
            return Response({"Response":{"Exception":str(exc)}})
    
    def put(self,request):
        try:
            post_obj = get_post(post_id = request.query_params.get('post_id'))
            if not isinstance(post_obj,Post):
                return Response({"Response" : " Post not found" })
            
            user_object = get_user(request.query_params.get('user_id'))
            if not isinstance(user_object,User):
                return Response({"Response" : "User not found"})
                
            if str(post_obj.user_id.user_id) != str(request.query_params.get('user_id')):
                return Response({"Response":"Invaild user"})
            
            
            serializer = PostSerializer(post_obj,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Response" :{"Post Updated":serializer.data}})
            
            return Response({"Response":{"Post Updated":serializer.data}})
        except Exception as exc:
            return Response({"Response":{"Exception":str(exc)}})
        
        
    def delete(self,request):
        post_obj = get_post(post_id = request.query_params.get('post_id'))
        if not isinstance(post_obj,Post):
            return Response({"Response" : " Post not found" })
        
        user_object = get_user(request.query_params.get('user_id'))
        if not isinstance(user_object,User):
            return Response({"Response" : "User not found"})
        
        if str(post_obj.user_id.user_id) != str(request.query_params.get('user_id')):
                return Response({"Response":"Invaild user"})
            
        post_obj.delete()
        return Response({"Response" : "Post deleted" })

class LikeClass(APIView):
    
    def get(self,request):
        data = get_like()
        
        #check query output
        if isinstance(data,QuerySet):
            return Response({"Response" : {"Post data" :data.values()}})
        
        #Return the response with exception
        return Response({"Response" : {"Post data" :data}})
    
    def post(self,request):
        try:
            user_obj = get_user(request.data['user_id'])
            if not isinstance(user_obj,User):
                return Response({"Response":user_obj})
            post_obj = get_post(post_id = request.data['post_id'])
            if not isinstance(post_obj,Post):
                return Response({"Response" : " Post not found" })
            serializer = LikeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Response" :{"Like Inserted":serializer.data}})
            
        except Exception as exc:
            return Response({"Response":{"Exception":str(exc)}})
    
    def put(self,request):
        try:
            
            like_obj = get_like(like_id =request.query_params.get('like_id'))
            if not isinstance(like_obj,Like):
                return Response({"Response" : " Like not found" })
        
            user_object = get_user(request.data['user_id'])
            if not isinstance(user_object,User):
                return Response({"Response" : "User not found"})
                
            if str(like_obj.user_id.user_id) != str(request.data['user_id']):
                return Response({"Response":"Invaild user"})
            
            
            serializer = PostSerializer(like_obj,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Response" :{"Post Updated":serializer.data}})
            return Response({"Response":{"Post Updated":serializer.data}})
        except Exception as exc:
            return Response({"Response":{"Exception":str(exc)}})
        
        
    def delete(self,request):
        like_obj = get_like(request.query_params.get('like_id'))
        if not isinstance(like_obj,Like):
            return Response({"Response" : " Like not found" })
        
        user_object = get_user(request.query_params.get('user_id'))
        if not isinstance(user_object,User):
            return Response({"Response" : "User not found"})

        if str(like_obj.user_id.user_id) != str(request.query_params.get('user_id')):
                return Response({"Response":"Invaild user"})
            
        like_obj.delete()
        return Response({"Response" : "Like deleted" })

def get_post(post_id = None,user_id =None):
    try:
        if not user_id:
            return Post.objects.get(post_id=post_id)
        post  = Post.objects.all().filter(Q(user_id=user_id)|Q(is_public=True)).values()
        post_data = []
        for post_value in post:
            count = Like.objects.filter(post_id=post_value['post_id']).count()
            post_value['total_like'] = max(count, 0)
            post_data.append(post_value)
        return post_data

    except Exception as exc:
        return "Post Not found"
    
def get_user(user_id):
    try:
        #Get the single record ased on the user id
        return User.objects.get(user_id=user_id)
    except Exception:
        return "User Not found"

def get_like(like_id = None):
    try:
        #Get the single record ased on the user id
        
        return Like.objects.get(like_id=like_id) if like_id else Like.objects.all()
    except Exception:
        return "User Not found"

    


