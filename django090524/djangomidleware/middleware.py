from django.shortcuts import render, HttpResponse

#function based middleware
def middleware1(get_response):
    #one time initialization
    print('one time intialization 1')
    def function1(request):
        #code before view
        print('Code before view 1')
        response = get_response(request)
        #code after view
        print('code after view 1')
        return response
    return function1

#class based view
class Middleware2:
    def __init__(self, get_response):
        self.get_response = get_response
        print('one time initialization 2')
        
    def __call__(self, request):
        print('code before view 2')
        response = self.get_response(request)
        print('code after view 2')
        return response
    
    def process_view(request, *args, **kwargs):
        print('process view executed')
        #return HttpResponse("Before View Executed!") #as it return httresponse, no view excuted
        return None #as it returns None, view will executed
    
    #if exception occurs we are dispalying below HttpRepose with msg
    def process_exception(self, request, exception):
        print('exception occured')
        msg = exception
        return HttpResponse(msg)
    
    # we can change the context data from htmltemplate using below, like changin field (name, age etc)
    def process_template_response(self, request, response):
        print('process response template middeware')
        response.context_data['name'] = 'Rahul'
        return response