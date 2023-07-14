from django.contrib import admin
from agency_app.models import User_login
from agency_app.models import Cylinder
from agency_app.models import Defective_cylinder
# from agency_app.models import Vehicle
from agency_app.models import Employee
from agency_app.models import Customer
from agency_app.models import Agency
from agency_app.models import Order
from agency_app.models import Inventory
from agency_app.models import Vehicle
from agency_app.models import Delivery





# Register your models here.

admin.site.register(User_login)
admin.site.register(Cylinder)
admin.site.register(Defective_cylinder)
admin.site.register(Vehicle)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Agency)
admin.site.register(Order)
admin.site.register(Inventory)
admin.site.register(Delivery)




