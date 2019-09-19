from django.shortcuts import render
from .models import User

# Create your views here.
def home(request):
    user = request.user
    if user.is_authenticated:
        users_dt = User.objects.all()
        target_users_list = [dt for dt in users_dt if str(dt) == user.username]
        if len(target_users_list) == 0:
            target_user = User(username=user.username)
            target_user.save()
        else:
            target_user = target_users_list[0]
        
    return render(request, 'home.html')