from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from items.models import  Items


@login_required
def checkout(request, item_id):
    item = get_object_or_404(Items, id=item_id)
    return render(request, 'payments/checkout.html', {'item': item})