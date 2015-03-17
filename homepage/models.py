from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	# Inherited from AbstractUser and AbstractBaseUser
	# password
	# last_login
	# first_name
	# last_name
	# email
	# is_staff
	# help_text
	# is_active
	# date_joined
	securtiy_question = models.TextField(max_length=150, null=True, blank=True)
	creation_date = models.DateField(null=True, blank=True)
	address1 = models.TextField(max_length=30, null=True, blank=True)
	address2 = models.TextField(max_length=30, null=True, blank=True)
	city = models.TextField(max_length=30, null=True, blank=True)
	state = models.TextField(max_length=30, null=True, blank=True)
	country = models.TextField(max_length=30, null=True, blank=True)
	zip = models.TextField(max_length=30, null=True, blank=True)
	#family_name = models.TextField(max_length=30, null=True, blank=True)
	pass

class Organization(User):
	organization_type = models.TextField(max_length=30, null=True, blank=True)
	pass

class PhotographableThing(models.Model):
	pass

class Person(User):
	family_name = models.TextField(max_length=30, null=True, blank=True)
	pass

class Photograph(models.Model):
	date_taken = models.DateTimeField(null=True, blank=True)
	place_taken = models.TextField(max_length=30, null=True, blank=True)
	image = models.TextField(max_length=30, null=True, blank=True)
	photographable_thing = models.ManyToManyField(PhotographableThing, null=True, blank=True)
	person = models.ForeignKey(Person, null=True, blank=True)

class LoginInfo(models.Model):
	password = models.TextField(max_length=30, null=True, blank=True)
	security_question = models.TextField(max_length=30, null=True, blank=True)
	sq_answer = models.TextField(max_length=30, null=True, blank=True)
	role = models.TextField(max_length=30, null=True, blank=True)
	record_creation_date = models.DateField(null=True, blank=True)
	user = models.ForeignKey(User, null=True, blank=True)

class Phone(models.Model):
	number = models.IntegerField(max_length=15, null=True, blank=True)
	extension = models.TextField(max_length=30, null=True, blank=True)
	type = models.TextField(max_length=30, null=True, blank=True)
	user = models.ForeignKey(User, null=True, blank=True)

class Item(models.Model):
	name = models.TextField(max_length=30, null=True, blank=True)
	description = models.TextField(max_length=30, null=True, blank=True)
	value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	standard_rental_price = models.DecimalField(max_digits = 10, decimal_places = 2, null=True, blank=True)
	user = models.ForeignKey(User, null=True, blank=True)

class WardrobeItem(Item):
	size = models.TextField(max_length=30, null=True, blank=True)
	size_modifier = models.TextField(max_length=30, null=True, blank=True)
	GENDER = (
	('M', 'Male'),
	('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER, null=True, blank=True)
	color = models.TextField(max_length=30, null=True, blank=True)
	pattern = models.TextField(max_length=30, null=True, blank=True)
	start_year = models.DateField(null=True, blank=True)
	end_year = models.DateField(null=True, blank=True)
	note = models.TextField(max_length=30, null=True, blank=True)

class RentableItem(Item):
	pass

class Rental(models.Model):
	rental_time = models.DateField(null=True, blank=True)
	due_date = models.DateField(null=True, blank=True)
	discount_percent = models.IntegerField(max_length=15, null=True, blank=True)
	organization = models.ForeignKey(Organization, null=True, blank=True)
	pass

class Agent(Person):
	appointment_date = models.DateField(null=True, blank=True)
	pass

class Return(models.Model):
	return_time = models.DateField(null=True, blank=True)
	fees_paid = models.DecimalField(max_digits=10, decimal_places=2)
	pass
	agent = models.ForeignKey(Agent, null=True, blank=True)

class RentedItem(models.Model):
	condition = models.TextField(max_length=30, null=True, blank=True)
	new_damage = models.TextField(max_length=30, null=True, blank=True)
	damage_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	late_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	rentable_item = models.ForeignKey(RentableItem, null=True, blank=True)
	rental = models.ForeignKey(Rental, null=True, blank=True)
	returns = models.ForeignKey(Return, null=True, blank=True)

class Participant(Person):
	biographical_sketch = models.TextField(max_length = 30, null=True, blank=True)
	contact_relationship = models.TextField(max_length = 30, null=True, blank=True)
	photo_id = models.IntegerField(null=True, blank=True)
	supervisor = models.ForeignKey(Person, related_name='person_supervisor', null=True, blank=True)

class Event(models.Model):
	name = models.TextField(null=True, blank=True)
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	map_file_name = models.TextField(max_length = 75, null=True, blank=True)

# class PublicEvent(models.Model):
# 	name = models.TextField(null=True, blank=True)
# 	description = models.TextField(null=True, blank=True)
# 	event = models.ForeignKey(Event, null=True, blank=True)

# class Area(models.Model):
# 	name = models.TextField(max_length = 75, null=True, blank=True)
# 	description = models.TextField(max_length = 200, null=True, blank=True)
# 	place_Number = models.IntegerField(null=True, blank=True)
# 	agent = models.ForeignKey(Agent, null=True, blank=True)
# 	event = models.ForeignKey(Event, null=True, blank=True)
# 	participant = models.ManyToManyField(Participant, null=True, blank=True)

# class SaleItem(models.Model):
# 	name = models.TextField(max_length = 75, null=True, blank=True)
# 	description = models.TextField(max_length = 200, null=True, blank=True)
# 	low_price = models.DecimalField(max_digits = 10, decimal_places = 2, null=True, blank=True)
# 	high_price = models.DecimalField(max_digits = 10, decimal_places = 2, null=True, blank=True)
# 	area = models.ForeignKey(Area, null=True, blank=True)

class Venue(models.Model):
	name = models.TextField(max_length = 75, null=True, blank=True)
	address = models.TextField(max_length = 100, null=True, blank=True)
	city = models.TextField(max_length = 50, null=True, blank=True)
	state = models.TextField(max_length = 2, null=True, blank=True)
	zip = models.IntegerField(null=True, blank=True)
	event = models.ForeignKey(Event, null=True, blank=True)

class Product(models.Model):
	name = models.TextField(null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	category = models.TextField(null=True, blank=True)
	current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	user = models.ForeignKey(User, null=True, blank=True)
	pass

class Order(models.Model):
	order_date = models.DateField(null=True, blank=True)
	phone = models.TextField(null=True, blank=True)
	date_picked = models.DateField(null=True, blank=True)
	date_paid = models.DateField(null=True, blank=True)
	date_shipped = models.DateField(null=True, blank=True)
	tracking_number = models.TextField(null=True, blank=True)
	agent = models.ForeignKey(Agent, null=True, blank=True)

class IndividualProduct(models.Model):
	date_made = models.DateField(null=True, blank=True)
	order = models.ForeignKey(Order, null=True, blank=True)

class BulkProduct(Product):
	quantity_ordered = models.IntegerField(null=True, blank=True)

class BulkDetail(models.Model):
	quantity = models.IntegerField(null=True, blank=True)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, null=True, blank=True)
	order = models.ForeignKey(Order, null=True, blank=True)
	bulk_product = models.ForeignKey(BulkProduct, null=True, blank=True)

class PersonalProduct(Product):
	order_form_name = models.TextField(max_length = 75, null=True, blank=True)
	production_time = models.DateField(null=True, blank=True)

class PersonalDetail(models.Model):
	order_file = models.TextField(max_length = 75, null=True, blank=True)
	order = models.ForeignKey(Order, null=True, blank=True)
	personal_product = models.ForeignKey(PersonalProduct, null=True, blank=True)

class ProductPicture(models.Model):
	picture = models.TextField(null=True, blank=True)
	caption = models.TextField(null=True, blank=True)
	product = models.ForeignKey(Product, null=True, blank=True)