from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from .forms import ProductForm


# Create your views here.


def all_products(request):
    """ A view to return the all the flowers, including sorting and searches """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to return the individual product details  """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Adding new products to the admin view """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()

    template = 'products/add_products.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def update_product(request, product_id):
    """ Admin can update products """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('product_detail', args=[product.id]))
    form = ProductForm(instance=product)

    template = 'products/update_products.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
