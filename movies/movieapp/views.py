from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.views import APIView,Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions,authentication
from .models import Film,Review
from .serializers import UserModelSerializer,FilmModelSer,ReviewSerializer


# Create your views here.

class UserView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            new_user=UserModelSerializer(data=request.data)
            if new_user.is_valid():
                new_user.save()
                return Response({"msg":"ok"})
            else:
                return Response({"msg":new_user.errors},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"msg":"failed"},status=status.HTTP_404_NOT_FOUND)
        


class FilmView(ModelViewSet):
    serializer_class=FilmModelSer
    queryset=Film.objects.all()
    model=Film    
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]  

    @action(detail=True,methods=['post'])
    def add_review(self,request,*args,**kwargs):
        did=kwargs.get('pk')
        film=Film.objects.get(id=did)
        user=request.user
        ser=ReviewSerializer(data=request.data,context={"user":user,"film":film})
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        else:
            return Response({"msg":"failed"},status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=True,methods=['get'])
    def get_review(self,request,*args,**kwargs):
        did=kwargs.get('pk')
        film=Film.objects.get(id=did)
        qs=Review.objects.filter(film=film)
        ser=ReviewSerializer(qs,many=True)
        return Response(data=ser.data)
    