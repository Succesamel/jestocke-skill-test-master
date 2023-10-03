from django.contrib import admin
from django.urls import path
from market_place.views import  storage_boxes_filter, StorageBoxListView, StorageBoxCreateView

app_name = "storage-boxes"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StorageBoxListView.as_view(), name='home'),
    path('list_storage-boxes/', StorageBoxListView.as_view(), name='storage_box_list'),
    path('filter-boxes/', storage_boxes_filter, name='filter_boxes'),
    path('create/', StorageBoxCreateView.as_view(), name='create_storage_box'),
]