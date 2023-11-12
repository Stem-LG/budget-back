from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getHello(request):
    if(request.method == "POST"):
        print("params:",request.body)
    return Response("hello mf, your name is: ")