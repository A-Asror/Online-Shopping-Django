from django.urls import path
from . import views
from .views import ProductCategoryView, ProductCategoryDetailView

urlpatterns = [
    path('category/detail/<int:pk>', ProductCategoryDetailView.as_view(), name='category-detail'),
    path('home', views.home_page, name='home'),
    path('', views.hone_page, name='home_page'),
    path('shop', views.ShopPageView.as_view(), name='shop'),
    path('blog', views.BlogPageView.as_view(), name='blog'),
    path('blogs', views.blog, name='blogs'),
    # path(),
    path('login', views.login_page, name='login_page'),
    path('registration', views.registration_page, name='registration'),
    path('logout', views.user_logout, name='logout'),
    path('contact', views.contact, name='contact'),
    path('cek-out', views.check, name='checkout'),
    path('filter/<int:id>', ProductCategoryView.as_view(), name='category_products'),  # '<int:id>'
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
    # path('cart', views.cart)

]
