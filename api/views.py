from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response  ## instead of jsonresponse
from rest_framework.decorators import api_view ## decorators
from . models import Notes ## we are going to query the data from the database.
from . serialisers import NoteSerialiser ## serialiser file created to convert objects to json format

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Notes.objects.all() ## this returns a list of all the python objects of Notes, which cannot be passed in response.
    ## therefore we will use serialiser to convert objects into json format.

    serialiser = NoteSerialiser(notes,many=True) ## this in it self will give an object

    return Response(serialiser.data)

@api_view(['GET']) ## this is to get a single note
def getNote(request,pk):
    notes = Notes.objects.get(id=pk) 

    serialiser = NoteSerialiser(notes,many=False) 

    return Response(serialiser.data)