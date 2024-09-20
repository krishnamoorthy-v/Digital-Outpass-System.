import json
from .controller import insertOne, getOneByEmail, updateOneById, deleteOneById, getAll, filter_Dpt_Wise
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.

@api_view(["POST"])
@permission_classes((AllowAny,))
def setStudent(request):
    '''
    To insert the data into data base
    :param request:
    :return: status of the insert data
    '''
    res = insertOne(json.loads(request.body))
    return res


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getStudent(request, email):
    '''
    To get one student who's matching the given email id
    :param request:
    :param email:
    :return: json values
    '''
    res = getOneByEmail(email)
    return res


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateStudent(request, pk):
    '''
    To update student info based on the id
    :param request:
    :param pk:
    :return: updated info
    '''
    data = json.loads(request.body)
    res = updateOneById(pk, data)
    return res


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteStudent(request, pk):
    '''
    To delete the student infor based on the id
    :param request:
    :param pk:
    :return: status info
    '''
    res = deleteOneById(pk)
    return res


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getAllStudent(request):
    '''
    to get list of all student from the db
    :param request:
    :return: list of json
    '''
    res = getAll()
    return res


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getAllFromDpt(request, dpt):
    '''
    To get all student based on dept
    :param request:
    :param dpt:
    :return: list of the json
    '''
    res = filter_Dpt_Wise(dpt)
    return res
