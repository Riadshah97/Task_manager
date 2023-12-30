
from django.urls import path
from .import views
#from .views import HomeView

urlpatterns = [
    path('', views.HomeView.as_view(), name= '')
    #path('myapi/', views.BlogList.as_view()),

]
