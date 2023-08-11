from tableapp import views
from django.urls import path

urlpatterns = [
    path("", views.index ,name='index'),
    # path("save/", views.save ,name='save'),
    # path("excel_download/", views.excel_download ,name='excel_download'),
]
