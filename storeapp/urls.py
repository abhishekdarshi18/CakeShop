from django.urls import path, include
from .views import signup, login, logout
from .views import Index, Cart, Checkout, Orders
from .middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator

urlpatterns = [
    # path('', index, name='index'),
    path('', Index.as_view(), name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', Checkout.as_view(), name='checkout'),
    path('orders', auth_middleware(Orders.as_view()), name='orders'),
]