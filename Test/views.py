from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_201_CREATED
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView   #For Class Based API


@api_view(['GET', 'POST'])
def index(request):
    # message = 'This is the test URL'
    if request.method == 'GET':
        return Response(data={'message': "Hello From Django App!"}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        return Response(data={'message': request.data}, status=status.HTTP_200_OK)
    else:
        return Response(data="Request Method Not Right!")

@login_required
@api_view(http_method_names = ['GET', 'POST'])
def test(request):
    print(request.user)
    print(request.auth)
    if request.method == 'GET':
        return Response(data={'message': 'Hello'}, status=HTTP_200_OK)
    elif request.method == 'POST':
        return Response(data={'message': request.data}, status=HTTP_200_OK)
    else:
        return Response(data="Request Method Not Right!")


class Message(APIView):
    def get(self, request):
        return Response(data="this is a class based View", status=status.HTTP_200_OK)
    def post(self, request):
        return Response(data=request.data, status=status.HTTP_201_CREATED)
