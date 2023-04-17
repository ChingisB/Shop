"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from products.views import ProductView, CategoryView, RatingView, liked_products
from products.views import VendorView, comment_view, like_view, ImageView
from user.views import LoginView, SignupView, StaffView
from user.views import LogoutView, UserInfoView, UserPaymentView
from cart.views import ShoppingSessionView
from order.views import OrderView

urlpatterns = [
    path('products/', ProductView.as_view(), name="products"),
    path('products/<int:product_id>/', ProductView.as_view()),
    path('products/<int:product_id>/likes', like_view),
    path('products/<int:product_id>/comments', comment_view, name="comment"),
    path('products/<int:product_id>/comments/<int:comment_id>', comment_view, name="comment"),
    path('products/<int:product_id>/rating', RatingView.as_view()),
    path('products/liked/', liked_products),
    path('category/', CategoryView.as_view(), name="categories"),
    path('category/<int:id>', CategoryView.as_view(), name="categories"),
    path('vendor/', VendorView.as_view(), name="vendor"),
    path('vendor/<int:id>', VendorView.as_view()),
    path('staff/', StaffView.as_view()),
    path('staff/<int:staff_id>', StaffView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('userinfo/', UserInfoView.as_view()),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('cart/', ShoppingSessionView.as_view()),
    path('api-auth-token/', obtain_auth_token, name='api_token_auth'),
    path('images/<int:product_id>', ImageView.as_view()),
    path('images/<int:id>', ImageView.as_view()),
    path('images/', ImageView.as_view()),
    path('payment_info/', UserPaymentView.as_view()),
    path('orders/', OrderView.as_view()),
    path('orders/<int:order_id>', OrderView.as_view()),
]
