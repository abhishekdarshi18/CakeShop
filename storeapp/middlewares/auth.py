from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print('Middleware')
        returnUrl = ''
        print(request.META['PATH_INFO'])
        if not request.session.get('customer_id'):
            # return redirect(f'login?return_url={returnUrl}')
            return redirect('login')
        
        response = get_response(request)
        return response
    
    return middleware