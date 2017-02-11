from django.conf.urls import url 
from closetApp import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^add-clothes/', views.add_clothes, name="add-clothes"),
	url(r'^login/', views.user_login, name='login'),
	url(r'^logout/', views.user_logout, name='logout'),
	url(r'^register/', views.register, name='register'),
	]