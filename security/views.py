
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .controller import createSecurityWithLoginController, readAllController, readOneControllerEmail, readOneControllerId, \
    updateOneControllerId, updateOneControllerEmail, deleteOneControllerId, deleteOneControllerEmail, \
    deleteAllController
from .models import SecurityModel
from .serializer import SecuritySerializer


# Create your views here.

@api_view(["POST"])
@permission_classes([AllowAny])
def create(request):
    res = createSecurityWithLoginController(request.data)
    return res


@api_view(["GET"])
@permission_classes([AllowAny])
def readAll(request):
    res = readAllController()
    return res


@api_view(["GET"])
@permission_classes([AllowAny])
def readOneByEmail(reqeust, email):
    res = readOneControllerEmail(email)
    return res


@api_view(["GET"])
@permission_classes([AllowAny])
def readOneById(request, id):
    res = readOneControllerId(id)
    return res


@api_view(["PUT"])
@permission_classes([AllowAny])
def updateOneById(request, id):
    res = updateOneControllerId(id, request.data)
    return res


@api_view(["PUT"])
@permission_classes([AllowAny])
def updateOneByEmail(request, email):
    res = updateOneControllerEmail(email, request.data)
    return res


@api_view(["DELETE"])
@permission_classes([AllowAny])
def deleteOneById(request, id):
    res = deleteOneControllerId(id)
    return res


@api_view(["DELETE"])
@permission_classes([AllowAny])
def deleteOneByEmail(request, email):
    res = deleteOneControllerEmail(email)
    return res


@api_view(["DELETE"])
@permission_classes([AllowAny])
def deleteAll(request):
    res = deleteAllController()
    return res
