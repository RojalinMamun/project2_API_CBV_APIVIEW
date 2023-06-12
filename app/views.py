from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response 
from rest_framework import status

class ProductCrud(APIView):
    def get(self,request,id):
        PQS=Product.objects.all()
        PJD=ProductSerializer(PQS,many=True)
        return Response(PJD.data)

    def post(self,request,id):
        PMSD=ProductSerializer(data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'message': 'Product is created'})

        return Response({'failed':'Product creation is failed' })

    def put(self,request,id):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        UPO=ProductSerializer(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'message': 'Product is Updated'})

        return Response({'failed':'Product is not Updated' })

    def patch(self,request,id):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        PO.Pname=request.data['Pname']
        PO.save()
        return Response({'Success':'Data is Partially Updated'})

    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({'Success':'Product is deleted'})


