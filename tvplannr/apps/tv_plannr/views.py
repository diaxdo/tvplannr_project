from django.shortcuts import render
#CONTROLLER
# Create your views here.
def index(request):
    print('8'*100)
    return render(request, 'tv_plannr/index.html')
def plannr(request):
    print('8'*100)
    return render(request, 'tv_plannr/plannr.html')
def create_account(request):
    print('8'*100)
    return render(request, 'tv_plannr/create_account.html')
