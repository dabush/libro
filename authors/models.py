from django.db import models

class Author(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	date_of_birth = models.DateField(auto_now=False)
	country = models.CharField(max_length=100)
	date_added = models.DateField(auto_now_add=True)
	def __str__(self):
		return self.first_name + ' ' + self.last_name 
	