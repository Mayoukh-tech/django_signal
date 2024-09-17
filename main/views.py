# my_app/views.py
from django.http import HttpResponse
from .signals import my_signal
import threading
from django.db import transaction

def home_view(request):
    return HttpResponse("Welcome to the Django Signals Demo!")
# View for Question 1 (Synchronous Execution)
def trigger_signal_view(request):
    print("Sending signal...")
    my_signal.send(sender=None)
    return HttpResponse("Signal triggered.")

# View for Question 2 (Thread Check)
def test_thread_view(request):
    print(f"View running in thread: {threading.current_thread().name}")
    my_signal.send(sender=None)
    return HttpResponse("Thread check done.")

# View for Question 3 (Transaction Check)
def test_transaction_view(request):
    try:
        with transaction.atomic():
            print("Inside transaction, sending signal...")
            my_signal.send(sender=None)
            raise Exception("Simulated error to rollback transaction")
    except Exception:
        print("Transaction rolled back.")
    return HttpResponse("Transaction check done.")
