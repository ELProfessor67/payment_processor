from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def add_transaction(request):
#     if(request.method != "POST"):
#         return HttpResponse(f"can't {request.method} /add_transation")
    

# def get_all_transaction(request):
#     pass

def home(request):
    return HttpResponse('Working... please go /admin')

def about(request):
    return HttpResponse('Working... i am about')