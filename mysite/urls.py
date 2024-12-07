"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from railways.views import RegisterUser, LoginUser, AddTrain, check_seat_availability, BookSeat, get_booking_details


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('add-train/', AddTrain.as_view(), name='add-train'),
    path('seat-availability/', check_seat_availability, name='seat-availability'),
    path('book-seat/', BookSeat.as_view(), name='book-seat'),
    path('booking/<int:booking_id>/', get_booking_details, name='get-booking-details'),
]
