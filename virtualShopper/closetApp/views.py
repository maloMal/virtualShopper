from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from models import ClothingType, UserProfile
from forms import ClothingForm, ContactForm, PasswordRecoveryForm, UserProfileForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime 

def index(request):
	#pictures = os.listdir(STATIC_PATH+"/images")
	context_dict = {}

	context_dict["clothes"] = ClothingType.objects.all()
	return render(request, 'index.html', context_dict)

def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)

			profile.user = user

			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserProfileForm()
		#profile_form = UserProfileForm()
	return render(request, 'register.html', {'user_form':user_form,
											#'profile_form':profile_form,
											'registered':registered})


def user_login(request):	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse('Youre not welcome here')
		else:
			print "invalid login details: {0}, {1}".format(username, password)
			return HttpResponse('Your login credentials were wrong')
	else:
		return render(request, 'loginPage.html', {})

def add_clothes(request):
	if request.method == 'POST':
		form = ClothingForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print form.errors
	else:
		form = ClothingForm()

	return render(request, 'add_category.html', {'form':form})
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')
# Create your views here.
