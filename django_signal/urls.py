"""
URL configuration for django_signal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from main.views import home_view,trigger_signal_view, test_thread_view, test_transaction_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trigger-signal/', trigger_signal_view),  # Synchronous signal
    path('check-thread/', test_thread_view),      # Thread check
    path('check-transaction/', test_transaction_view),  # Transaction check
    path('', home_view),  # Map root URL to home_view
]