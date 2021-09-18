from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View

from laundry.forms import UserForm
from laundry.models import (
    User,
    Load,
    Washer,
    Dryer,
    Bin
)

class WasherView(View):
    template_name = 'washer.html'
    
    def get(self, request, washer_id):
        washer = get_object_or_404(Washer, id=washer_id)
        form = UserForm()
        context = {
            'form': form,
            'washer': washer
        }
        return render(request, self.template_name, context)

    def post(self, request, washer_id):
        washer = get_object_or_404(Washer, id=washer_id)
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            

        context = {
            'form': form,
            'washer': washer
        }
        return render(request, self.template_name, context)
        

class DryerView(View):
    def get(self, request, dryer_id):
        pass

    def post(self, request, dryer_id):
        pass

