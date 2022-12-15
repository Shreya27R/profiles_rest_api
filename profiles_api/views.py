from rest_framework.views import APIView
from rest_framework.response import Response




class HelloApiView(APIView):
    """Test API VIEW"""

    def get(self, request , format=None):
        """Returns a list of APIViews features"""
        an_apiview = [
             'Uses HTTP metthods as function (get,post,patch,put,delete)',
             'Is similar to a traditional Django View',
             'Gives you the most control over you application logic ',
             'Is mapped manually to URLS',

        ]
        return Response({'message': 'Hello','an_apiview':an_apiview})
