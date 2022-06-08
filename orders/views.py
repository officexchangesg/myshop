from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
<<<<<<< HEAD
=======
from .tasks import order_created

>>>>>>> 25b485f6fc3721598feb5a080a8516f3d539e28f
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
<<<<<<< HEAD
=======
            # launch asynchronous task
            order_created.delay(order.id)
>>>>>>> 25b485f6fc3721598feb5a080a8516f3d539e28f
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
<<<<<<< HEAD
=======

>>>>>>> 25b485f6fc3721598feb5a080a8516f3d539e28f
