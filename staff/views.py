from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse
from django.views import generic
from cart.models import Order, Product
from .mixins import StaffUserMixin


class StaffView(LoginRequiredMixin, generic.ListView):
    template_name = 'staff/staff.html'
    # Sorts orders by most recent first
    queryset = Order.objects.filter(ordered=True).order_by('-ordered_date')
    paginate_by = 20
    context_object_name = 'orders'


class ProductListView(LoginRequiredMixin, StaffUserMixin, generic.ListView):
    template_name = 'staff/product_list.html'
    queryset = Product.objects.all()
    paginate_by = 20
    context_object_name = 'products'


class ProductDeleteView(LoginRequiredMixin, StaffUserMixin, generic.DeleteView):
    template_name = 'staff/product_delete.html'
    queryset = Product.objects.all()

    def get_success_url(self):
        return reverse("staff:product-list")
