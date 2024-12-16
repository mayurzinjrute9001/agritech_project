from django.views import View
from django.shortcuts import redirect,render

class Home(View):
    def get(self,request):
        return render(request,'home.html')