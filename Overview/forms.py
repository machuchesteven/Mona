from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model =  Product
        fields = ('__all__')
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['id','user','content']
    # def form_valid(self, form):
    #     form.instance.product_id = self.request.product.product_id
    #     return super(PermCreate, self).form_valid(form)
    
# class CategoryForm(forms.ModelForm):
#     class Meta:
