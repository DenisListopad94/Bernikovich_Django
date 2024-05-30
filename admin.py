from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from myapp.models import MyModel  # Импортируйте свою модель

# Создание нового пользователя
new_user = User.objects.create_user('username', 'email@username.com', 'password')
new_user.save()

# Создание или получение группы
group, created = Group.objects.get_or_create(name='SuperusersAdmin')

# Получение типа содержимого для модели
content_type = ContentType.objects.get_for_model(MyModel)

# Получение или создание разрешений
view_permission = Permission.objects.get(
    codename='view_mymodel',
    content_type=content_type,
)
change_permission = Permission.objects.get(
    codename='change_mymodel',
    content_type=content_type,
)

# Добавление разрешений в группу
group.permissions.add(view_permission, change_permission)
permissions = [
    Permission.objects.get_or_create(codename='add_hotel', name='Can add hotel', content_type=hotel_content_type)[0],
    Permission.objects.get_or_create(codename='view_hotel', name='Can view hotel', content_type=hotel_content_type)[0],
    Permission.objects.get_or_create(codename='add_comment', name='Can add comment', content_type=comment_content_type)[
        0],
    Permission.objects.get_or_create(codename='view_comment', name='Can view comment',
                                     content_type=comment_content_type)[0],
]

# Добавление пользователя в группу
new_user.groups.add(group)

# Назначение разрешений пользователю
user.user_permissions.set(permissions)
user.save()
