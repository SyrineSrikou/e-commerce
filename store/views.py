from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('user_dashboard:stores')

    context = {'form':form}
    return render(request, 'create_store.html', context)


#get specific store by Id
def store(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    context = {
        'store' : store
    }
    return render(request, 'store_dashboard.html', context)
