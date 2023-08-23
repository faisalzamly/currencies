from tableapp import views
from django.urls import path

urlpatterns = [
    path("", views.index ,name='index'),
    path("login", views.login1 ,name='login'),
    path("Change_password", views.Change_password ,name='Change_password'),
    path("control", views.control ,name='control'),
    path("Form1", views.Form1 ,name='Form1'),
    path("Form2", views.Form2 ,name='Form2'),
    path("Form3", views.Form3 ,name='Form3'),
    path("Form4", views.Form4 ,name='Form4'),
    path("Form5", views.Form5 ,name='Form5'),
    # path("table1", views.num_table_price_market ,name='table1'),
    path('logout/',views.Logout, name="logout"),

]
