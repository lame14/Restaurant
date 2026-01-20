from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking, Review, MenuItem
import datetime
from django.utils import timezone

# Страница бронирования
def booking(request):
    success = False
    error_message = ''

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        guests = request.POST.get('guests')
        comment = request.POST.get('comment', '')

        # Проверка даты и времени
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        time = datetime.datetime.strptime(time_str, '%H:%M').time()
        now = datetime.datetime.now()

        if date < now.date() or (date == now.date() and time <= now.time()):
            error_message = "Неможливо забронювати на минулу дату або час."
        elif date > now.date() + datetime.timedelta(days=365):
            error_message = "Неможливо забронювати більш ніж на рік вперед."
        else:
            Booking.objects.create(
                name=name,
                phone=phone,
                date=date,
                time=time,
                guests=guests,
                comment=comment
            )
            success = True

    return render(request, 'booking/booking.html', {'success': success, 'error_message': error_message})


def home(request):
    reviews = Review.objects.all().order_by('-created_at')[:5]
    return render(request, 'home/home.html', {'reviews': reviews})


def menu(request):
    items = MenuItem.objects.filter(is_available=True).order_by("category", "title")
    return render(request, "menu/menu.html", {"items": items})


def reviews(request):
    error_message = ""

    if request.method == "POST":
        name = request.POST.get("name")
        text = request.POST.get("text")
        rating_raw = request.POST.get("rating")

        if not name or not text or not rating_raw:
            error_message = "Всі поля повинні бути заповнені."
        else:
            try:
                rating = int(rating_raw)
            except ValueError:
                rating = 0
            
            if rating < 1 or rating > 5:
                error_message = "Рейтинг повинен бути від 1 до 5."
            else:
                # Django сам добавит created_at
                Review.objects.create(
                    name=name,
                    text=text,
                    rating=rating,
                )
                return redirect('reviews:reviews')
            
    reviews_list = Review.objects.all().order_by('-created_at')
    return render(
        request,
        "reviews/reviews.html",
        {"reviews": reviews_list, "error_message": error_message},
    )
