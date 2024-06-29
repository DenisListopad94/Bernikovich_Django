from django.urls import path
import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from views import register, custom_login
from django.urls import path
from views import home_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/', views.view_profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('', views.index, name='index'),  # Главная страница
    path('hotels/', views.hotels, name='hotels'),  # Страница с отелями
    path('users/', views.users, name='users'),  # Страница с пользователями
    path('comments/', views.comments, name='comments'),  # Страница с комментариями
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('signup/', register, name='signup'),
    path('login/', custom_login, name='login'),
    path('home/', home_view, name='home'),
]

urlpatterns = ['https://'
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
