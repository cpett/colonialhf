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
	["Master", "Yoda", "password", "myoda", True, "yoda@theforce.com"],
	["Clark", "Kent", "hope", "BatmanSucks", False, "lasereyes@aol.com"],
	["Bruce", "Wayne", "bats", "LadyKiller", False , "bruce@wayne.com"],
	["Johnny", "Karate", "lasers", "BertMacklin", False, "brokenfist@me.com" ]
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
	["Scera", "State Street", "Orem", "UT", 12345],
	["Bates Motel", "Psycho St", "Lonely Grove", "CA", 66666],
	["Jedi Temple", "Corrisant", "Corrisant", "Corrisant", 12345]
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
	["Storm Tooper Helmet", "Helmet for gents", "25.00", "10.00"],
	["Breeches", "Breeches for gents", "20.00", "15.00"],
	["Jedi Cloak", "Cloak for gents", "50.00", "20.00"]
]:
	w = hmod.Item()
	w.name = data[0]
	w.description = data[1]
	w.value = data[2]
	w.standard_rental_price = data[3]
	w.save()


#Events
for data in [
	['2014-05-05', '2014-06-06', "Mapzoid", "Jedi Trials"],
	['2014-05-05', '2014-06-06', "Treasure Map", "Summer Solstice"],
	['2014-05-05', '2014-06-06', "Cool Map", "Grand Event"]
]:
	e = hmod.Event()
	e.name = data[3]
	e.start_date = data[0]
	e.end_date = data[1]
	e.map_file_name = data[2]
	e.save()

for data in[
	["Bonnet","Female head cover thingie","Clothing", 7.99],
	["Cloak","Body cover thingie","Clothing", 22.89],
	["Flag","Decoration thingie","Decoration", 50.43],
	["Hat","Male head cover thingie","Clothing", 15.89],
	["Sword","Sharp thingie","Weapons", 35.69]
]:
	pr = hmod.Product()
	pr.name = data[0]
	pr.description = data[1]
	pr.category = data[2]
	pr.current_price = data[3]
	pr.save()

#create groups
#initialize db