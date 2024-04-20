from django.shortcuts import render
from .models import CustomerProfile, PerformerProfile

def customer_profile(request):
    try:
        # Получение профиля заказчика текущего пользователя
        customer_profile = CustomerProfile.objects.all()
    except CustomerProfile.DoesNotExist:
        # Если профиль не найден, можно выполнить какие-то дополнительные действия или вернуть сообщение об ошибке
        return render(request, 'profile_not_found.html')
    return render(request, 'customer_profile.html', {'profile': customer_profile})

def performer_profile(request):
    try:
        # Получение профиля исполнителя текущего пользователя
        performer_profile = PerformerProfile.objects.all()
    except PerformerProfile.DoesNotExist:
        return render(request, 'profile_not_found.html')
    return render(request, 'performer_profile.html', {'profile': performer_profile})
