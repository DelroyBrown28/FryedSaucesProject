from .models import Order


# A way for the user to go through the site without
# #having to login/signup until checking out
def get_or_set_order_session(request):
    order_id = request.session.get('order_id, None')
    if order_id is None:
        order = Order()
        order.save()
        request.session['order_id'] = order.id

    else:
        try:
            order = order.objects.get(id=order_id, ordered=False)
        except Order.DoesNotExist:
            order = Order()
            order.save()
            request.session['object_id'] = order.id

    if request.user.is_authenticated and order.user is None:
        order.user = request.user
        order.save()
    return order
