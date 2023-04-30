from django.urls import path
from .views import file_list,download_status,download_file_remote,url_download_page, download_local_file
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', url_download_page, name='download_from_link'),
    path('download_local_file/<int:pk>/', download_local_file, name='download_local_file'),
    path('download-list/', file_list, name='download_list'),
    path('download_status/<int:pk>/', download_status, name='download_status'),
    # path('download_from_link/', url_download_page, name='download_from_link'),
    path('download_file_remote/', download_file_remote, name='download_file_remote'),

]
