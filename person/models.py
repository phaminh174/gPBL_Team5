from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(verbose_name='Name', max_length=255)
	age = models.PositiveIntegerField(verbose_name='Age')
	address = models.CharField(max_length=255, verbose_name='Address')
	phone_number = models.CharField(max_length=255, verbose_name='Phone number')
	email = models.EmailField(max_length=255, verbose_name='Email')
	id_company = models.CharField(max_length=255, verbose_name='Company code')
	created_at = models.DateTimeField(auto_now_add=True)
	# updated_at = models.DateTimeField()

	class Meta:
		__tablename__='person' 
		ordering=['created_at'] 
