from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from person.models import Person
from person.serializers import PersonSerializer

class ListCreatePersonView(ListCreateAPIView):
    model = Person
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = PersonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Person successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Person unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeletePersonView(RetrieveUpdateDestroyAPIView):
    model = Person
    serializer_class = PersonSerializer
    
    def get_queryset(self):
        return Person.objects.all()

    def put(self, request, pk, *args, **kwargs):
        person = get_object_or_404(Person, id=pk)
        serializer = PersonSerializer(instance=person, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Person successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Person unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        person = get_object_or_404(Person, id=kwargs.get('pk'))
        person.delete()

        return JsonResponse({
            'message': 'Delete Person successful!'
        }, status=status.HTTP_200_OK)
