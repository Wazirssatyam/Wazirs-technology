from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def index(request):
  
     return render(request,'index.html')

# def about(request):
#     return render(request,"about.html")
# def services(request):
#     return render(request,"services.html")
# @csrf_exempt
# def contact(request):
#       redirect('/')
# #     return render(request,"contact.html")