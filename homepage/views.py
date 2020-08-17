import subprocess
from django.shortcuts import render

from homepage.models import UserInput
from homepage.forms import inputform

# Create your views here.

def index(request):
    if request.method == "POST":
        form = inputform(request.POST)
        newform = inputform()
        if form.is_valid():
            data = form.cleaned_data
            UserInput.objects.create(
                text=data.get('text')
            )
            cowsay = subprocess.run('cowsay', input=data.get('text').encode('utf-8'), capture_output=True)
            return render(request, 'post.html', {"form": newform, "cowsay": cowsay.stdout.decode()})
    cowsayform = inputform()
    return render(request, "post.html", {"form": cowsayform})

def topten(request):
    tencowsays = UserInput.objects.order_by('-id')[:10]
    return render(request, "topten.html", {'topten': tencowsays})