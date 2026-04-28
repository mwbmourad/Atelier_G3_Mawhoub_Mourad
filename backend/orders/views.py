from django.shortcuts import render, redirect
from django.views import View
from .forms import OrderForm
from cart.utils import get_or_create_cart
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import OrderItem

class CreateOrderView(LoginRequiredMixin, View):
    def get(self, request):
        cart = get_or_create_cart(request)
        form = OrderForm()
        return render(request, 'orders/shipping.html', {'form': form, 'cart': cart})

    def post(self, request):
        cart = get_or_create_cart(request)
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
            order.update_total()
            cart.items.all().delete()
            return render(request, 'orders/confirmation.html', {'order': order})