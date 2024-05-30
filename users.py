from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from myapps.models import Hotel, Comment
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from your_app.models import HotelOwner

user = User.objects.create_user('new_username', 'email@username.com', 'your_password')
user.is_staff = True  # Права staff для доступа к админ-панели
user.is_active = True  # Активный пользователь
user.save()

# Получение типов содержимого для моделей
hotel_content_type = ContentType.objects.get_for_model(Hotel)
comment_content_type = ContentType.objects.get_for_model(Comment)

group = Group.objects.create(name='HotelOwnersGroup')

# Получение типа содержимого для модели владельца отеля
content_type = ContentType.objects.get_for_model(HotelOwner)

# Создание разрешений для группы
permissions = [
    Permission.objects.get_or_create(codename='add_hotelowner', name='Can add hotel owner', content_type=content_type)[
        0],
    Permission.objects.get_or_create(codename='change_hotelowner', name='Can change hotel owner',
                                     content_type=content_type)[0],
    Permission.objects.get_or_create(codename='delete_hotelowner', name='Can delete hotel owner',
                                     content_type=content_type)[0],
    Permission.objects.get_or_create(codename='view_hotelowner', name='Can view hotel owner',
                                     content_type=content_type)[0],
]

# Добавление разрешений в группу
for perm in permissions:
    group.permissions.add(perm)
group.save()

# Назначение группы пользователю
user.groups.add(group)
user.save()
