from django.urls import path , include

app_name='user'
urlpatterns = [
    #login url
    path('user/' , include ('django.contrib.auths.urls')),
    #registration url
    path('user/', views.register, name='register')

]
