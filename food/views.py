from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from json import loads
from .models import Food
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class FoodCreateListView(View) :

    def post(self,request,*args,**kwargs):

        data = loads(request.body)
        Food.objects.create(**data)
        return JsonResponse({"meassge":"200 ok"})
    
    def get(self,request,*args,**kwargs) :

        data = list(Food.objects.values())

        return JsonResponse({"data" : data,"message" : "200 ok"})
    

@method_decorator(csrf_exempt,name="dispatch")    
class FoodRetrieveUpdateDeleteView(View) :

    def get(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        data = Food.objects.filter(id=id).values().first()

        return JsonResponse({"data" : data,"message" : "200 ok"})
    
    def put(self,request,*args,**kwargs) :

        id = kwargs.get("pk")

        data = loads(request.body)

        Food.objects.filter(id=id).update(**data)

        return JsonResponse({"message" : "200 ok"})
    
    def delete(self,request,*args,**kwargs) :

        id = kwargs.get("pk")

        Food.objects.get(id=id).delete()

        return JsonResponse({"message" : "Deleted 200 ok"})

    

