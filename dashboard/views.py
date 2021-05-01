from django.shortcuts import render

#get all stores owned by a user
def stores(request):
    stores =  request.user.store_set.all()
    return render(request, 'stores.html', {'stores': stores})


