from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *

# Open a Store
def createStore(request):
    form = CreateStoreForm()
    if request.method == 'POST':
        form = CreateStoreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            store = form.cleaned_data.get('name')
            messages.success(request, 'store was opened')
            return redirect('discover:home')

    context = {'form':form}
    return render(request, 'create_store.html', context)
