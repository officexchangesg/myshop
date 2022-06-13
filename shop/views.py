from django.shortcuts import render, get_object_or_404
from .models import Category, Product
#view to list all the products or filter products by a given category
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        #category = get_object_or_404(Category, slug=category_slug)
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category,
                             translations__language_code=language,
                             translations__slug=category_slug)

        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})
#view to retrieve and display a single product

#Add the functionality to retrieve a maximum of four recommended products
from .recommender import Recommender
def product_detail(request, id, slug):
    # product = get_object_or_404(Product,
    #                             id=id,
    #                             slug=slug,
    #                             available=True)
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product,
                                id=id,
                                translations__language_code=language,
                                translations__slug=slug,
                                available=True)

    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'recommended_products': recommended_products})