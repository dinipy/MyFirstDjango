from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from dini.models import Login, Register

# Create your views here.
def load_home_page(request):
	return HttpResponse('welcome to my world')

def login(request):
	return render(request, 'login.html')

def registration_form(request):
	return render(request,'registraton.html')

def check_login(request):
	import pdb
	pdb.set_trace()
	#print request.GET.get('user')
	#print request.GET.get('pwd')
	fe_user = request.GET.get('user')
	fe_pwd = request.GET.get('pwd')
	try:
		obj = Login.objects.get(username=fe_user)
		if obj.passwoord == fe_pwd:
			return HttpResponse("Login Successful")
		else:
			return HttpResponse('Password Mismatch')
	except:
		return HttpResponse('User not available')

def registration(request):
	#return render(request,'registraton.html')
	fe_name=request.GET.get('username')
	fe_add=request.GET.get('address')
	fe_pwd1=request.GET.get('pwd1')
	fe_cpwd2=request.GET.get('pwd2')
	fe_mob = request.GET.get('mob')

	try:
		obj = Register.objects.get(username=fe_name)
		return HttpResponse('User already exist, so please try to login....................')
	except:
		if fe_pwd1 == fe_cpwd2:
			obj = Register.objects.create(username=fe_name, address=fe_add, password=fe_pwd1, cpassword=fe_cpwd2, mobile=fe_mob)
			obj.save()
			obj_login = Login.objects.create(username=fe_name, passwoord=fe_pwd1)
			obj_login.save()
			return HttpResponseRedirect('/login/')
		else:
			return HttpResponse("Incorrect Password")


def show_users(request):
	objs = Login.objects.all()
	return render_to_response('show_user.html', {'data': objs})

def sendmail(request):
	# For future pusrpose
	pass