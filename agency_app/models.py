from django.db import models
PAYMENT_MODE = [
    ("CSH", "Cash"),
    ("ONL", "Online"),
    ("UPI", "UPI Payment")
]
STATE_CHOICES = [
            ("AP","Andhra Pradesh"),
            ("AR","Arunachal Pradesh"),
            ("AS","Assam"), 
            ("BR","Bihar"),
            ("CG","Chhattisgarh"),
            ("GA","Goa"),
            ("GJ","Gujarat"),
            ("HR","Haryana"),
            ("HP","Himachal Pradesh"),
            ("JH","Jharkhand"),
            ("KA","Karnataka"),
            ("KL","Kerala"),
            ("MP","Madhya Pradesh"),
            ("MH","Maharashtra"),
            ("MN","Manipur"),
            ("ML","Meghalaya"),
            ("MZ","Mizoram"),
            ("NL","Nagaland"),
            ("OR","Odisha"),
            ("PB","Punjab"),
            ("RJ","Rajasthan"),
            ("SK","Sikkim"),
            ("TN","Tamil Nadu"),
            ("TG","Telangana"),
            ("TR","Tripura"),
            ("UP","Uttar Pradesh"),
            ("UK","Uttarakhand"),
            ("WB","West Bengal"),
        ]
CYLINDER_CHOICES = [
    ("S", "5 Kg"),
    ("M", "14.2 Kg"),
    ("L", "19Kg")
]

VEHICLE_CHOICES = [
    ("3W", "Three Wheeler Tempo"),
    ("4W", "Truck")
]

CUSTOMER_COMPLAIN_CHOICES = [
    ("1", "Over Charging"),
    ("2", "Rude Behavior"),
    ("3", "Not Accepting Online Payment"),
    ("4", "Not Giving Invoice")
]
# Create your models here.
class User_login(models.Model):
    # Conditional (test_pass) login for giving specific state/city access
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    def __str__(self):
        return f"{self.username}"

class Cylinder(models.Model):
    cylinder_type = models.CharField(max_length=1, choices=CYLINDER_CHOICES)

class Defective_cylinder(models.Model):
    defective_body = models.CharField(max_length=3)
    defective_nossle = models.CharField(max_length=3)

class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=2, choices=VEHICLE_CHOICES)
    vehicle_num = models.CharField(max_length=100)
    vehicle_driver = models.CharField(max_length=100)

class Employee(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=100)
    emp_name = models.CharField(max_length=122)
    designation = models.CharField(max_length=10)
    emp_mob = models.CharField(max_length=20)
    emp_address = models.CharField(max_length=225)
    emp_gender = models.CharField(max_length=10)
    emp_blood_grp = models.CharField(max_length=10)
    emp_adhaar = models.CharField(max_length=20)
    emp_city = models.CharField(max_length=100)
    emp_state = models.CharField(max_length=2, choices=STATE_CHOICES)
    emp_feedback = models.CharField(max_length=225)

class Customer(models.Model):
    cus_id = models.CharField(primary_key=True, max_length=100)
    cus_name = models.CharField(max_length=122)
    cus_address = models.CharField(max_length=122)
    cus_mob = models.CharField(max_length=20)
    cus_city = models.CharField(max_length=100)
    cus_state = models.CharField(max_length=2, choices=STATE_CHOICES)
    cus_pincode = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.cus_name + self.cus_id}" #format to concate 2 strings together


class Agency(models.Model):
    agency_id = models.AutoField(primary_key=True)
    agency_name = models.CharField(max_length=100)
    agency_owner = models.CharField(max_length=122)
    agency_number = models.CharField(max_length=100)
    agency_GSTIN = models.CharField(max_length=100)
    agency_state = models.CharField(max_length=2, choices=STATE_CHOICES)

class Order(models.Model):
    customer_id = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=100)
    cylinder_type = models.CharField(max_length=100)


class Inventory(models.Model):
    cyl_rec = models.IntegerField()       #cylinder received to BPCL 
    cyl_ret = models.IntegerField()       #cylinder return to BPCL
    cyl_full = models.IntegerField()      #no. of full cylinders
    cyl_empty = models.IntegerField()     #no. of empty cylinders 
    cyl_defective = models.IntegerField() #no. of defective cylinders 
    cyl_delivered = models.IntegerField() #no. of cylinders delivered to customer
    cyl_received = models.IntegerField()  #no. of cylinders received from customer 
    total_cylinder = models.IntegerField()#overall cylinder count 

class Delivery(models.Model):
    date = models.DateField()
    time = models.TimeField()
    del_amt = models.IntegerField()
    del_pay_mode = models.CharField(max_length=3, choices=PAYMENT_MODE)