from django import forms
from django.core.exceptions import ValidationError

from shop.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        if any(word in cleaned_data.lower() for word in forbidden_words):
            raise ValidationError("Имя не должно содержать запрещенные слова: " + ', '.join(forbidden_words))

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        if any(word in cleaned_data.lower() for word in forbidden_words):
            raise ValidationError("Описание не должно содержать запрещенные слова: " + ', '.join(forbidden_words))

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = ('version_number', 'version_name', 'is_current')
