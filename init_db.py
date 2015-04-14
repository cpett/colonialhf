#!/usr/bin/env python3

# initialize django
import sys
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'colonialHF.settings'
import django
django.setup()
import homepage.models as hmod



from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess

##### DROP DATABASE, RECREATE IT, THEN MIGRATE IT #################

cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])

##### CREATE PERMISSIONS/GROUPS #####################
# Permission.objects.all().delete()
# Group.objects.all().delete()

# permission = Permission()
# permission.codename = 'manager_rights'
# permission.content_type = ContentType.objects.get(id=7)
# permission.name = 'Has Manager Rights'
# permission.save()

# for data in [
# 	["Guests"],
# 	["Managers"],
# 	["Administrators"]
# ]:

# 	group = Group()
# 	group.name = data[0]
# 	group.save()
# 	group.permissions.add(permission)

# print('permissions initialized')

# create data that we want to insert into database

#Users
hmod.User.objects.all().delete()

for data in [
	["Cody", "Pettit", "password", "cpettit", False, "cpett26@gmail.com"],
	["Jordan", "Rader", "password", "jrader", False, "jdavisrader@gmail.com"],
	["Josh", "Haws", "password", "jhaws", True , "joshhaws0@gmail.com"],
	["Tanner", "Sawyer", "password", "tsawyer", False, "tanner.sawyer@gmail.com" ],
	["Conan", "Albrecht", "password", "calbrecht", False, "conan.albrecht@test.com" ]
]:
	u = hmod.User()
	u.first_name = data[0]
	u.last_name = data[1]
	u.set_password(data[2])
	u.username = data[3]
	u.is_superuser = data[4]
	u.email = data[5]
	u.save()

# Venue
for data in [
	["Scera Park", "600 S. State Street", "Orem", "UT", 84058],
	["President's Park", "1600 Pennsylvania Ave SW", "Washington", "DC", 20500],
	["Lexington and Concord", "Middlesex County", "Lexington/Concord", "Massachusetts", 51431]
]:
	u = hmod.Venue()
	u.name = data[0]
	u.address = data[1]
	u.city = data[2]
	u.state = data[3]
	u.zip = data[4]
	#u.event = data[5]
	u.save()

#Wardrobe
# for data in [
# 	["Storm Tooper Helmet", "L", "Big", "M", "White", "None"],
# 	["Breeches", "XL", "Gove", "M", "Brown", "Plain"],
# 	["Jedi Cloak", "XXXL", "Jedi", "M", "Black", "None"]
# ]:
# 	w = hmod.WardrobeItem()
# 	w.name = data[0]
# 	w.size = data[1]
# 	w.size_modifier = data[2]
# 	w.gender = data[3]
# 	w.color = data[4]
# 	w.pattern = data[5]
# 	w.save()

#Item
for data in [
	["Musket", "Replica colonial era musket (not actual gun)", "25.00", "10.00"],
	["Breeches", "Colonial era breeches for gentlemen", "20.00", "15.00"],
	["Waistcoat", "Typical colonial wear for gentleman", "50.00", "20.00"],
	["Brunswick", "A three-quarter length jacket worn with a petticoat", "30.00", "15.00"]
]:
	w = hmod.Item()
	w.name = data[0]
	w.description = data[1]
	w.value = data[2]
	w.standard_rental_price = data[3]
	w.save()


#Events
for data in [
	['2015-05-05', '2015-05-08', "Mapzoid", "Colonial Heritage Festival"],
	['2015-06-05', '2015-06-08', "Treasure Map", "Summer Solstice Festival"],
	['2015-07-05', '2014-07-08', "Cool Map", "War Commencement Festival"]
]:
	e = hmod.Event()
	e.name = data[3]
	e.start_date = data[0]
	e.end_date = data[1]
	e.map_file_name = data[2]
	e.save()

for data in[
	["Cap","A practical piece that allowed the head to be dressed without styling the hair","Clothing", 7.99],
	["Cloak","A long, loose, unfitted, protective outer garment that was usually made from thick wool","Clothing", 22.89],
	["Flag","Colonial Era Flag","Decoration", 50.43],
	["Hat","Typical style of hat worn by men from the colonial era","Clothing", 15.89],
	["Sword","A sword indicated rank and stature in battles. Usually a mounted officer directed his men with the sword.","Weapons", 35.69]
]:
	pr = hmod.Product()
	pr.name = data[0]
	pr.description = data[1]
	pr.category = data[2]
	pr.current_price = data[3]
	pr.save()

#create groups
#initialize db