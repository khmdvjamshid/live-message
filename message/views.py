from django.shortcuts import render,redirect
from . forms import MessageForm
from django.contrib import messages
# Create your views here.

def main(request):

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Message Send!')
            return redirect("main")
    else:
        form = MessageForm()
    return render(request, "main.html", {'form': form}) 