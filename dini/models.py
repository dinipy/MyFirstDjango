from django.db import models

class Person(models.Model):
	
	Country_Name=[('IND','india'),
	              ('China','chaina'), 
	              ('USA','usa')
	              ]



	name = models.CharField(max_length=20,unique=True)
	age = models.IntegerField()
	email =models.CharField(max_length=20,unique=True)
	phone =models.CharField(max_length=20,unique=True)
	gender=models.CharField(max_length=6)
	location=models.CharField(max_length=20)
	marital_status=models.CharField(max_length=5)
	country=models.CharField(max_length=20,choices=Country_Name)
	
	def __unicode__(self):
		return self.name
class Employer(models.Model):

	company =models.CharField(max_length=20)
	emp_id =models.CharField(max_length=10)
	salary =models.IntegerField()
	personal_details=models.CharField(max_length=20)
 	
 	person = models.ForeignKey(Person)

 	def __unicode__(self):
		return self.company

class Login(models.Model):
	username = models.CharField(max_length=20, unique=True)
	passwoord = models.CharField(max_length=20)

	def __unicode__(self):
		return self.username

class Register(models.Model):
	username = models.CharField(max_length=20,unique=True)
	address = models.CharField(max_length=500)
	password = models.CharField(max_length=20)
	cpassword = models.CharField(max_length=20)
	mobile = models.CharField(max_length=10)

	def __unicode__(self):
		return self.username, self.address
 