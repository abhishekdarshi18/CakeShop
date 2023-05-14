from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from django.views import View
# from storeapp.middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator


class Index(View):
    def post(self, request, *args, **kwargs):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity==1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        
        request.session['cart'] = cart
        print('CART VALUE: ', request.session['cart'])
        # print(product)
        return redirect('index')

    def get(self, request, *args, **kwargs):
            cart = request.session.get('cart')
            if not cart:
                request.session['cart'] = {}
            product = None
            # request.session.get('cart').clear # THIS WILL CLEAR THE CART
            # products = Product.get_all_products()  # products is used as a dictionary value
            categories = Category.get_all_category_name()
            # print(products)
            # print(request.GET)
            categoryID = request.GET.get('category')
            if categoryID:
                products = Product.get_product_by_id(categoryID)
            else:
                products = Product.get_all_products()
            data = {}
            data['products'] = products
            data['categories'] = categories
            print('CUSTOMER SESSION EMAIL>>', request.session.get('email'))
            print('CUSTOMER SESSION ID>>', request.session.get('customer_id'))
            # print('CUSTOMER SESSION NAME>>', request.session.get('name'))
            return render(request, 'index.html', data)



# def index(request):
#     product = None
#     # products = Product.get_all_products()  # products is used as a dictionary value
#     categories = Category.get_all_category_name()
#     # print(products)
#     # print("LN 11",request.GET)
#     categoryID = request.GET.get('category')
#     if categoryID:
#         products = Product.get_product_by_id(categoryID)
#     else:
#         products = Product.get_all_products()
#     data = {}
#     data['products'] = products
#     data['categories'] = categories
#     print('CUSTOMER SESSION EMAIL>>',request.session.get('email'))
#     return render(request, 'index.html', data)


def signup(request):
    # print("LN 25", request.method)
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(name, phone, email, password)

        # VALIDATION
        value = {
            'name': name,
            'phone': phone,
            'email': email, 
        }

        error_message = None

        if not name:
            error_message = 'Name is required'

        elif name:
            if len(name) < 4:
                error_message = 'Name must be at least 4 characters long'

        elif not phone:
            error_message = 'Phone number is required'

        elif len(phone) < 10:
            error_message = 'Phone number must be at least 10 characters long'

        elif not email:
            error_message = 'Email is required'

        if Customer.objects.filter(email=email).exists():
            error_message = 'Email address already exists'

        elif len(password) < 4:
            error_message = 'Password must be at least 4 characters long'
        

        # VALIDATION END 

        # SAVING CUSTOMER DETAILS IF NO ERROR_MESSAGE
        if not error_message:
            customer = Customer(
                name=name,
                phone=phone,
                email=email,
                password=password
            )
            customer.password = make_password(customer.password)
            customer.save() # customer.register()/ customer.save() can also be called

            return redirect('index')
        else:
            data = {
                'error_message': error_message,
                'values': value,
            }
            return render(request,'signup.html', data)
        


########### LOGIN ###########

def login(request):
    # print("This is",request.method, "method")
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        # print(request.method)
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        # print(customer)
        # print(email,password)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                # request.session['name'] = customer.name
                return redirect('index')
            else:
                error_message = 'Email or Password is incorrect'
        else:
            error_message = "Email or Password is incorrect"
        return render(request,'login.html', {'error_message': error_message})
    


############ LOGOUT ###########

def logout(request):
    request.session.clear()
    return redirect('login')



############ CART #########
class Cart(View):
    def get(self, request, *args, **kwargs):
        print("Cart Items: ", request.session.get('cart').keys())
        id_lst = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(id_lst)
        # print(products)
        return render(request, 'cart.html', {'products': products})


################ CHECKOUT #################

class Checkout(View):
    def post(self, request, *args, **kwargs):
        # print(request.POST)
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        cart_id_lst = list(cart.keys())
        products = Product.get_products_by_id(cart_id_lst)
        print(address, phone, customer, cart, products)
        
    

        for product in products:
            order = Order(
                customer=Customer(id=customer),
                product = product,
                price = product.price,
                address = address,
                phone = phone,
                quantity = cart.get(str(product.id))
            )
            order.save()
        request.session['cart'] = {}

        return redirect('cart')
    


class Orders(View):
    # @method_decorator(auth_middleware) # ALTERNATE WAY TO USE MIDDLEWARE IS IN STOREAPP/URLS.PY
    def get(self, request, *args, **kwargs):
        customer = request.session.get('customer_id')
        print('Customer: ', customer)
        orders = Order.get_order_by_customer(customer)
        # print('ORDER DETAILS: ', orders)
        orders = orders.reverse()
        return render(request, 'orders.html', {'orders': orders})
                        


