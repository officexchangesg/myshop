from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import os
app_name = 'shop'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=os.path.join(settings.BASE_DIR,app_name,settings.MEDIA_ROOT))