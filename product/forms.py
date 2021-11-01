from django.forms import ModelForm
from product.models import Category
from product.models import Burger

class CreateBurgerForm(ModelForm):

    class Meta:
        fields = ('name', 'content', 'rasmi', 'price', 'category')
        model = Burger 

class CreateCategoryForm(ModelForm):

    class Meta:
        fields = ('name',)
        model = Category 