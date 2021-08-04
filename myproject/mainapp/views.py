from unicodedata import category

from cart.cart import Cart
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, FormView
from .forms import *
from .models import *


@login_required(login_url='registration')
def home_page(request):
    brands = None
    categories = Category.objects.all()
    if request.method == 'POST' and request.POST.get('category_id'):
        products = Products.objects.filter(category=request.POST.get('category_id'))
        brands = Brand.objects.all()

    elif request.method == 'POST' and request.POST.get('brand_id'):
        products = Products.objects.filter(brand=request.POST.get('brand_id'))
        print(products)
        if products == '<QuerySet []>':
            redirect('home_page')
    else:
        return redirect('home_page')

    context = {
        'products': products,
        'categories': categories,
        'brands': brands,
    }
    return render(request, 'mainapp/index.html', context)


def login_page(request):
    # if request.user.is_authenticated:
    #     return redirect('home_page')
    # else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                print('Вход в Страницу')
                return redirect('home_page')
            else:
                messages.info(request, 'ERROR')

        context = {}
        return render(request, 'mainapp/login.html', context)


@login_required(login_url='registration')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    return render(request, 'mainapp/contact-us.html')


def registration_page(request):
    # if request.user.is_authenticated:
    #     redirect('home_page')
    # else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            print('Запрос есть')
            if form.is_valid():
                print('Сохранение')
                form.save()
                return redirect('login_page')
            else:
                if request.method == 'POST':
                    messages.error(request, 'Ваш пароль не достаточно сложно')

        context = {
            'form': form
        }
        return render(request, 'mainapp/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login_page')


# @login_required(login_url='registration')
class ShopPageView(TemplateView):
    template_name = 'mainapp/shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Products.objects.all()
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        return context


# @login_required(login_url='registration')
class BlogPageView(TemplateView):
    template_name = 'mainapp/blog-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['messages'] = Blog.objects.all()
        return context


# @login_required(login_url='registration')
# class HomePageView(TemplateView):
#     template_name = 'mainapp/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = Products.objects.all()
#         context['categories'] = Category.objects.all()
#         return context

@login_required(login_url='registration')
def  hone_page(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    print(45665465646546)
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'mainapp/index.html', context)


class ProductCategoryView(ListView, LoginRequiredMixin):
    template_name = 'mainapp/index.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['products'] = Products.objects.all()
        context['categories'] = Category.objects.all()
        context['bool'] = True
        return context


class ProductCategoryDetailView(TemplateView, LoginRequiredMixin):
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['products'] = Products.objects.filter(category=self.kwargs['pk'])
        print(context['products'])
        context['categories'] = Category.objects.all()
        context['bool'] = True
        return context


@login_required(login_url='registration')
def check(request):
    if request.method == 'POST':
        form = CheckForm(request.POST)
        print('Есть ПОСТ ЗАПРОС')
        print(form)
        if form.is_valid():
            print('РОШЕЛ ВАЛИДАЦИЮ')
            form.save()
            return redirect('home_page')
    return render(request, 'mainapp/checkout.html')


@login_required(login_url='registration')
def blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        print('456123456')
        print(form)
        if form.is_valid():
            print('РОШЕЛ ВАЛИДАЦИЮ')
            form.save()
            return redirect('blog')
    return render(request, 'mainapp/blog-single.html')


@login_required(login_url='registration')
def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url='registration')
def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url='registration')
def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url='registration')
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url='registration')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url='registration')
def cart_detail(request):
    return render(request, 'mainapp/cart.html')