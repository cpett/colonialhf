# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(verbose_name='username', unique=True, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=75)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('securtiy_question', models.TextField(max_length=150, blank=True, null=True)),
                ('creation_date', models.DateField(blank=True, null=True)),
                ('address1', models.TextField(max_length=30, blank=True, null=True)),
                ('address2', models.TextField(max_length=30, blank=True, null=True)),
                ('city', models.TextField(max_length=30, blank=True, null=True)),
                ('state', models.TextField(max_length=30, blank=True, null=True)),
                ('country', models.TextField(max_length=30, blank=True, null=True)),
                ('zip', models.TextField(max_length=30, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BulkDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, blank=True, max_digits=10, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('map_file_name', models.TextField(max_length=75, blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IndividualProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_made', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.TextField(max_length=30, blank=True, null=True)),
                ('description', models.TextField(max_length=30, blank=True, null=True)),
                ('value', models.DecimalField(decimal_places=2, blank=True, max_digits=10, null=True)),
                ('standard_rental_price', models.DecimalField(decimal_places=2, blank=True, max_digits=10, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LoginInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('password', models.TextField(max_length=30, blank=True, null=True)),
                ('security_question', models.TextField(max_length=30, blank=True, null=True)),
                ('sq_answer', models.TextField(max_length=30, blank=True, null=True)),
                ('role', models.TextField(max_length=30, blank=True, null=True)),
                ('record_creation_date', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('order_date', models.DateField(blank=True, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('date_picked', models.DateField(blank=True, null=True)),
                ('date_paid', models.DateField(blank=True, null=True)),
                ('date_shipped', models.DateField(blank=True, null=True)),
                ('tracking_number', models.IntegerField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, primary_key=True, auto_created=True, parent_link=True)),
                ('organization_type', models.TextField(max_length=30, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('homepage.user',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, primary_key=True, auto_created=True, parent_link=True)),
                ('family_name', models.TextField(max_length=30, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('homepage.user',),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('person_ptr', models.OneToOneField(to='homepage.Person', serialize=False, primary_key=True, auto_created=True, parent_link=True)),
                ('biographical_sketch', models.TextField(max_length=30, blank=True, null=True)),
                ('contact_relationship', models.TextField(max_length=30, blank=True, null=True)),
                ('photo_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('homepage.person',),
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('person_ptr', models.OneToOneField(to='homepage.Person', serialize=False, primary_key=True, auto_created=True, parent_link=True)),
                ('appointment_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('homepage.person',),
        ),
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('order_file', models.TextField(max_length=75, blank=True, null=True)),
                ('order', models.ForeignKey(to='homepage.Order', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('number', models.IntegerField(max_length=15, blank=True, null=True)),
                ('extension', models.TextField(max_length=30, blank=True, null=True)),
                ('type', models.TextField(max_length=30, blank=True, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photograph',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_taken', models.DateTimeField(blank=True, null=True)),
                ('place_taken', models.TextField(max_length=30, blank=True, null=True)),
                ('image', models.TextField(max_length=30, blank=True, null=True)),
                ('person', models.ForeignKey(to='homepage.Person', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhotographableThing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('current_price', models.DecimalField(decimal_places=2, blank=True, max_digits=10, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonalProduct',
            fields=[
                ('product_ptr', models.OneToOneField(to='homepage.Product', serialize=False, primary_key=True, auto_created=True, parent_link=True)),
                ('order_form_name', models.TextField(max_length=75, blank=True, null=True)),
                ('production_time', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=('homepage.product',),
        ),
        migrations.CreateModel(
            name='BulkProduct',
            fields=[
                ('product_ptr', models.OneToOneField(to='homepage.Product', serialize=False, primary_key=True, auto_created=True, parent_link=True)),
                ('quantity_ordered', models.IntegerField(blank=True, null=True)),
            ],
            options={
            },
            bases=('homepage.product',),
        ),
        migrations.CreateModel(
            name='ProductPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('picture', models.TextField(blank=True, null=True)),
                ('caption', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(to='homepage.Product', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RentableItem',
            fields=[
                ('item_ptr', models.OneToOneField(to='homepage.Item', serialize=False, primary_key=True, auto_created=True, parent_link=True)),
            ],
            options={
            },
            bases=('homepage.item',),
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('rental_time', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('discount_percent', models.IntegerField(max_length=15, blank=True, null=True)),
                ('organization', models.ForeignKey(to='homepage.Organization', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RentedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('condition', models.TextField(max_length=30, blank=True, null=True)),
                ('new_damage', models.TextField(max_length=30, blank=True, null=True)),
                ('damage_fee', models.DecimalField(decimal_places=2, blank=True, max_digits=10, null=True)),
                ('late_fee', models.DecimalField(decimal_places=2, blank=True, max_digits=10, null=True)),
                ('rentable_item', models.ForeignKey(to='homepage.RentableItem', null=True, blank=True)),
                ('rental', models.ForeignKey(to='homepage.Rental', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('return_time', models.DateField(blank=True, null=True)),
                ('fees_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('agent', models.ForeignKey(to='homepage.Agent', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WardrobeItem',
            fields=[
                ('item_ptr', models.OneToOneField(to='homepage.Item', serialize=False, primary_key=True, auto_created=True, parent_link=True)),
                ('size', models.TextField(max_length=30, blank=True, null=True)),
                ('size_modifier', models.TextField(max_length=30, blank=True, null=True)),
                ('gender', models.CharField(max_length=1, blank=True, choices=[('M', 'Male'), ('F', 'Female')], null=True)),
                ('color', models.TextField(max_length=30, blank=True, null=True)),
                ('pattern', models.TextField(max_length=30, blank=True, null=True)),
                ('start_year', models.DateField(blank=True, null=True)),
                ('end_year', models.DateField(blank=True, null=True)),
                ('note', models.TextField(max_length=30, blank=True, null=True)),
            ],
            options={
            },
            bases=('homepage.item',),
        ),
        migrations.AddField(
            model_name='renteditem',
            name='returns',
            field=models.ForeignKey(to='homepage.Return', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photograph',
            name='photographable_thing',
            field=models.ManyToManyField(to='homepage.PhotographableThing', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='personal_product',
            field=models.ForeignKey(to='homepage.PersonalProduct', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='supervisor',
            field=models.ForeignKey(to='homepage.Person', related_name='person_supervisor', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='agent',
            field=models.ForeignKey(to='homepage.Agent', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='logininfo',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='individualproduct',
            name='order',
            field=models.ForeignKey(to='homepage.Order', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bulkdetail',
            name='bulk_product',
            field=models.ForeignKey(to='homepage.BulkProduct', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bulkdetail',
            name='order',
            field=models.ForeignKey(to='homepage.Order', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_query_name='user', verbose_name='groups', blank=True, related_name='user_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', help_text='Specific permissions for this user.', related_query_name='user', verbose_name='user permissions', blank=True, related_name='user_set'),
            preserve_default=True,
        ),
    ]
