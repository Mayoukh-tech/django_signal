'''Question 1: Are Django signals executed synchronously or asynchronously by default?
By default, Django signals are executed synchronously. This means the signal handler will 
be executed within the same process and will block the caller until the signal handling is complete.

Question 2: Do Django signals run in the same thread as the caller?
Yes, Django signals run in the same thread as the caller.

Question 3: Do Django signals run in the same database transaction as the caller?
Yes, Django signals run in the same database transaction as the caller by default.
This means if the signal handler makes a database change, it will be part of the same 
transaction as the view or model action that triggered the signal.
'''
from django.dispatch import Signal, receiver

my_signal = Signal()

@receiver(my_signal)
def my_handler_one(sender, **kwargs):
    print("Handler one triggered")

@receiver(my_signal)
def my_handler_two(sender, **kwargs):
    print("Handler two triggered")
