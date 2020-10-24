from django import forms
from .models import OrderItem, SizeVariation, Product


class AddToCartForm(forms.ModelForm):
    size = forms.ModelChoiceField(queryset=SizeVariation.objects.none())

    class Meta:
        model = OrderItem
        fields = ['quantity', 'size']

    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop('product_id')
        product = Product.objects.get(id=product_id)
        super().__init__(*args, **kwargs)

        self.fields['size'].queryset = product.available_sizes.all()
