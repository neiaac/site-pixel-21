from django.shortcuts import render

from django.views.generic import View

# Create your views here.
class homepage_view(View):
    def get(self, request):
        print("Homepage_get")
        return render(request, 'homepage.html')

    def post(self, request):
        print("Homepage_post")