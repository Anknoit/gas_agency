# Generated by Django 4.2.3 on 2023-07-13 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('agency_id', models.AutoField(primary_key=True, serialize=False)),
                ('agency_name', models.CharField(max_length=100)),
                ('agency_owner', models.CharField(max_length=122)),
                ('agency_number', models.CharField(max_length=100)),
                ('agency_GSTIN', models.CharField(max_length=100)),
                ('agency_state', models.CharField(choices=[('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Odisha'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TG', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UK', 'Uttarakhand'), ('WB', 'West Bengal')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cus_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('cus_name', models.CharField(max_length=122)),
                ('cus_address', models.CharField(max_length=122)),
                ('cus_mob', models.CharField(max_length=20)),
                ('cus_city', models.CharField(max_length=100)),
                ('cus_state', models.CharField(choices=[('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Odisha'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TG', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UK', 'Uttarakhand'), ('WB', 'West Bengal')], max_length=2)),
                ('cus_pincode', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cylinder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cylinder_type', models.CharField(choices=[('S', '5 Kg'), ('M', '14.2 Kg'), ('L', '19Kg')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Defective_cylinder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defective_body', models.CharField(max_length=3)),
                ('defective_nossle', models.CharField(max_length=3)),
            ],
        ),
       
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=122)),
                ('designation', models.CharField(max_length=10)),
                ('emp_mob', models.CharField(max_length=20)),
                ('emp_address', models.CharField(max_length=225)),
                ('emp_gender', models.CharField(max_length=10)),
                ('emp_blood_grp', models.CharField(max_length=10)),
                ('emp_adhaar', models.CharField(max_length=20)),
                ('emp_city', models.CharField(max_length=100)),
                ('emp_state', models.CharField(choices=[('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Odisha'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TG', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UK', 'Uttarakhand'), ('WB', 'West Bengal')], max_length=2)),
                ('emp_feedback', models.CharField(max_length=225)),
            ],
        ),
        
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=10)),
                ('customer_name', models.CharField(max_length=100)),
                ('cylinder_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(choices=[('3W', 'Three Wheeler Tempo'), ('4W', 'Truck')], max_length=2)),
                ('vehicle_driver', models.CharField(max_length=100)),
                ('vehicle_num', models.CharField(max_length=100)),
            ],
        ),
    ]