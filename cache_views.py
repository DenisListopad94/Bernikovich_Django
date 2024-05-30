from django.views.decorators.cache import cache_page

# Кэшируем вьюшку на 30 минут (1800 секунд)
@cache_page(1800)
def my_view(request):
    # Ваш код для вьюшки здесь
    pass

@cache_page(1800)
def another_view(request):
    pass

