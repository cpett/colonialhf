from django.contrib.auth.models import Group, Permission, ContentType
from django.contrib.auth.decorators import permission_required





permission = Permission()
permission.codename = 'jedi_level'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'Has Jedi Privileges'
permission.save()

group = Group()
group.name = "Jedis"
group.save()
group.permissions.add(permission)
group.user_set.add(UserObjectHere)