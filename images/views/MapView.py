from django.views import View
from django.shortcuts import render


class MapView(View):
 def get(self,request):
     return render(request,'map_view.html')