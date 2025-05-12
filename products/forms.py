from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=200, label="Nombre")
    description = forms.CharField(max_length=300, label="Descripcion")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    available = forms.BooleanField(initial=True, required=False, label="Disponible")
    photo = forms.ImageField(required=False, label="Foto")
    stock = forms.IntegerField(min_value=0, label="Cantidad")
    
    class Meta:  # ¡Clase Meta faltante!
        model = Product  # Especifica el modelo
        fields = '__all__'  # o lista de campos: ['name', 'description', ...]
    def save(self):
        Product.objects.create(
            name = self.cleaned_data["name"],
            description = self.cleaned_data["description"],
            price = self.cleaned_data["price"],
            available = self.cleaned_data["available"],
            photo = self.cleaned_data["photo"],
            stock = self.cleaned_data["stock"],
        )   