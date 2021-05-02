from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from store.models import Store

#get all stores owned by a user
def stores(request):
    stores =Store.objects.filter(owner=request.user)
    return render(request, 'stores.html', {'stores': stores})


