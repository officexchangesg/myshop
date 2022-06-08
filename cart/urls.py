from django.urls import path
from . import views
<<<<<<< HEAD

=======
>>>>>>> 25b485f6fc3721598feb5a080a8516f3d539e28f
app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, 
                                     name='cart_remove'),
]
<<<<<<< HEAD

=======
>>>>>>> 25b485f6fc3721598feb5a080a8516f3d539e28f
