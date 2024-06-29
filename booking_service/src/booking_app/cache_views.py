from django.views.decorators.cache import cache_page
from django.views.decorators.cache import cache_page


# Кэшируем вьюшку на 30 минут (1800 секунд)
@cache_page(1800)
def my_view():
    # Ваш код для вьюшки здесь
    pass


@cache_page(1800)
def another_view():
    pass


@cache_page(60 * 10)  # Кэшируем на 10 минут
def my_view(request):
    # Логика вашей вьюшки
    pass
