# ADding value in DB has separate URL function
# Displaying values of DB has separate URL separate function

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from agency_app.models import User_login
from agency_app.models import Customer
from agency_app.models import Order


customer_fetch = Customer.objects.all()
context = {
            'customer_fetch' : customer_fetch
            }


def index(request):
    return render(request, 'index.html')  

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("logged in")
            return redirect('/dashboard')
        else:
            return render(request, 'index.html')    
    return render(request, 'index.html')    

# def admin_dashboard(request):
#     if request.user.is_authenticated:
#         return render(request, 'dashboard.html')
#     else:
#         return render(request, 'error404.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', context)
    else:
        return render(request, 'index.html')
def signout(request):
    logout(request)
    return redirect('index')


def customer_register(request):

    if request.method == 'POST':
        cus_id = request.POST.get('cus_id')
        cus_name = request.POST.get('cus_name')
        cus_address = request.POST.get('cus_address')
        cus_mob = request.POST.get('cus_mob')
        cus_city = request.POST.get('cus_city')
        
        cus_state = request.POST.get('cus_state')
        cus_pincode = request.POST.get('cus_pincode')
        customer = Customer(cus_id=cus_id, cus_name=cus_name, cus_address=cus_address,
        cus_mob=cus_mob, cus_city=cus_city, cus_state=cus_state, cus_pincode=cus_pincode)

        customer.save()
        
        # for customer in customer_fetch:
        #     print(customer.cus_name, customer.cus_id)
        print("registered")
        # print(type(customer_fetch))
        message = messages.success(request, "Customer registered successfully!")
        return redirect('/customer_list') 
    return redirect('/dashboard')

def customer_list(request):    
    if request.method == 'POST':
        return render(request, 'customer_panel.html', context) # When passing context, render the page for creating context values on the page
    return render(request, 'customer_panel.html', context)
def new_order(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        # customer_name = request.POST.get('customer_name')
        # customer name - Generate from entering customer_ID
        cylinder_type = request.POST.get('cylinder_type')
        order = Order(customer_id=customer_id, cylinder_type=cylinder_type)
        order.save()
        print("Order Placed!")
        return render(request, 'order.html')
    return render(request, 'dashboard.html')

def order_list(request):
    if request.method == 'POST':
        return render(request, 'order.html')
    

def agency_list(request):
    return render(request, 'new_agency_list.html')