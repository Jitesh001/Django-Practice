from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import Signal, receiver
from django.db.models.signals import pre_save, post_save
from django.core.signals import request_started, request_finished, got_request_exception

@receiver(user_logged_in, sender=User) #method2 - connecting signal using decorator
def login_success(sender, request, user, **kwargs): #reciever function
    print('--------login signal called------')
    print('sender', sender, 'request', request, 'user', user, 'kwargs', kwargs)

#connecting login signal to receiver
#user_logged_in.connect(login_success, sender=User) #method1 - connecting signal
#sender = User Model class, reuest = URL, user = User model Object, kwargs = {'signal':value}

@receiver(user_logged_out, sender=User) #method2 - connecting signal using decorator
def login_success(sender, request, user, **kwargs): #reciever function
    print('--------logout signal called------')
    print('sender', sender, 'request', request, 'user', user, 'kwargs', kwargs)

@receiver(user_login_failed) #method2 - connecting signal using decorator
def login_success(sender, request, credentials, **kwargs): #reciever function
    print('--------loing failed !!!!!!!!!------')
    print('sender', sender, 'request', request, 'credentials', credentials, 'kwargs', kwargs)
    
@receiver(pre_save, sender=User) #we are using User model here
def before_user_save(sender, instance, **kwargs): #reciever function
    print('--------User Model Pre Save -------')
    print('sender', sender, 'instance', instance, 'kwargs', kwargs)
    
@receiver(request_started) 
def request_begins(sender, environ, **kwargs): #reciever function
    print('--------request started!!!!!! -------')
    print('sender', sender, 'environ', environ, 'kwargs', kwargs)
    
@receiver(request_finished) 
def request_begins(sender, **kwargs): #reciever function
    print('--------request finished!!!!!! -------')
    print('sender', sender, 'kwargs', kwargs)
    
@receiver(got_request_exception) 
def request_begins(sender, request, **kwargs): #reciever function
    print('--------request Exception!!!!!! -------')
    print('sender', sender, 'request', request, 'kwargs', kwargs)
    
    
#custome signal
notification = Signal()
@receiver(notification)
def show_notification(sender, **kwargs):
    print('------Custome signal--------')
    print('sender', sender, 'kwargs', kwargs)
#refer views.py where signal is sent when sign up view/url is triggered
    