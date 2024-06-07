from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from myapp.models import MyModel
from django.utils.html import format_html
from django.contrib import admin
from models import UserProfile, Hotel


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_avatar')

    def display_avatar(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.avatar.url)

    display_avatar.short_description = 'Avatar'


class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_photo')

    def display_photo(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.photo.url)

    display_photo.short_description = 'Photo'


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Hotel, HotelAdmin)
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
