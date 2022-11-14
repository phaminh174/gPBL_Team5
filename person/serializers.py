from rest_framework import serializers
from person.models import Person

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		table = 'person'
		fields = ('name', 'age', 'address')