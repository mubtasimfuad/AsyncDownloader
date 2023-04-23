from django.urls import path
from .views import file_list, download_file,download_list,download_status


urlpatterns = [
    path('', file_list, name='file_list'),
    path('download/<int:pk>/', download_file, name='download'),
    path('download-list/', download_list, name='download_list'),
    path('download_status/<int:pk>/', download_status, name='download_status'),
]
