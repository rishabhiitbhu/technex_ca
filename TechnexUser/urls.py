from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from TechnexUser.views import *

app_name='technexuser'

urlpatterns = [

	#JsonResponse
	url(r'^api/login$', ApiLoginView, name= 'api_login'),
	#JsonResponse
	url(r'^api/register/$', ApiRegisterView, name='api_register'),

	# url(r'^collegejson/$', CollegeSearch, name='api_register'),

	url(r'^$', IndexView, name= 'index'),

	url(r'^login/$', LoginView, name= 'login'),

	url(r'^register/$', RegisterView, name='register'),

	url(r'^tech2ca/$', Tech2CA, name='tech2ca'),

	url(r'^fblogin/$', FbView, name='fblogin'),

	url(r'^dashboard/$', DashboardView, name='dashboard'),

	url(r'^events/$', EventView, name='event'),

	url(r'^logout/$', LogoutView, name='logout'),

]
