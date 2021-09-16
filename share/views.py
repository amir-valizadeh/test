from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET', 'POST'])
def snippet_list(request):

    if request.method == 'GET':

        return Response({
    "webcredentials": {
        "apps": [ "G7ZD9Z4RX9.com.pantryon.pantry" ]
    }
})
