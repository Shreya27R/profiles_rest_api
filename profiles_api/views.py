from rest_framework.views import APIView
from rest_framework.response import Response

#for http status code use this which can be used for post function handler
from rest_framework import status
from profiles_api import serializers

#For viewsets
from rest_framework import viewsets



class HelloApiView(APIView):
    """Test API VIEW"""
 ##added during seralizes this configures the serializer view
    serializer_class = serializers.HelloSerializer
    def get(self, request , format=None):
        """Returns a list of APIViews features"""
        an_apiview = [
             'Uses HTTP metthods as function (get,post,patch,put,delete)',
             'Is similar to a traditional Django View',
             'Gives you the most control over you application logic ',
             'Is mapped manually to URLS',

        ]
        return Response({'message': 'Hello','an_apiview':an_apiview})


        ##Adding post functionality to API view
    def post(self,request):
        """create a hello message with our name """
        serializer = self.serializer_class(data=request.data)
        #the serializer class comes with API view

        #This executes when input is valid
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        #Executes when input is not valid
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})


    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet """
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return hello message"""

        a_viewset = [
          'Uses actions(list,create,retrieve,update ,partial update)',
          'Automatic maps to URLS using Routers',
          'Provides more functionality',
        ]
        return Response ({'message':'Hello!', 'ViewSet':a_viewset})


    def create(self,request):
        """create a new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})

        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})
