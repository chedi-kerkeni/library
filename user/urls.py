from django.urls import path , include
from . import views
app_name='user'
urlpatterns = [
    #login url, needs a template
    path('user/' , include ('django.contrib.auth.urls')),
    #registration url
    path('user/', views.register, name='register'),

]
