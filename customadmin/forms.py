from django import forms
from users.models import CustomUser
from django.forms import EmailInput
from django.forms import ModelForm, TextInput, EmailInput, CharField, PasswordInput, ChoiceField, BooleanField, \
    NumberInput, DateInput
from .models import WebsiteSettings,Product, ProductImage, Category,TrandingProducts,Contactus,ContactInquiry,\
    SubCategory,RentAndHireProduct, RentImage
from ckeditor.widgets import CKEditorWidget
    
class WebSiteSettingsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['address1'].widget.attrs.update({'class': 'form-control'})
        self.fields['number1'].widget.attrs.update({'class': 'form-control'})
        self.fields['number2'].widget.attrs.update({'class': 'form-control'})
        self.fields['address2'].widget.attrs.update({'class': 'form-control'})
        
    class Meta:
            model = WebsiteSettings
            fields = ('name', 'image','address1','number1','address2',
            'number2')
            

class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget()) 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['description'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['pdf'].widget.attrs.update({'class': 'form-control'})
        self.fields['subcategory'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Product
        fields = ['category', 'name', 'description','pdf','subcategory']
        
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
        widgets = {

            'image': forms.ClearableFileInput(attrs={'allow_multiple_selected': True})

        }
        
        
class RentAndHireProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget()) 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['description'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['pdf'].widget.attrs.update({'class': 'form-control'})
        self.fields['tag_line1'].widget.attrs.update({'class': 'form-control'})
        self.fields['tag_line2'].widget.attrs.update({'class': 'form-control'})
        self.fields['tag_line3'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = RentAndHireProduct
        fields = ['category', 'name', 'description','pdf','tag_line1','tag_line2','tag_line3']
        
class RentImageForm(forms.ModelForm):
    class Meta:
        model = RentImage
        fields = ['image']
        widgets = {

            'image': forms.ClearableFileInput(attrs={'allow_multiple_selected': True})

        }

# class ProductImageForm(forms.Form):
#     images = forms.FileField(required=False, widget=forms.FileInput(attrs={'multiple': True}))

        
# class ProductFormWithImages(forms.Form):
#     images = forms.FileField(required=False, widget=forms.FileInput(attrs={'multiple': True}))


class CategoryForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget()) 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['image'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['description'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['tag_line'].widget.attrs.update({'class': 'form-control valid'})
    class Meta:
        model = Category
        fields = ['name','image','description','tag_line']
        
class SubCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['image'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['category'].widget.attrs.update({'class': 'form-control valid'})
    class Meta:
        model = SubCategory
        fields = ['name','image','category']
        
class TrandingProductsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['keyfeature1'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['keyfeature2'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['keyfeature3'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['keyfeature4'].widget.attrs.update({'class': 'form-control valid'})
    class Meta:
        model = TrandingProducts
        fields = ['name','keyfeature1','keyfeature2','keyfeature3','keyfeature4','image']
        
class ContactusForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['email'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['telephone'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['company_name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['message'].widget.attrs.update({'class': 'form-control valid'})
    class Meta:
        model = Contactus
        fields = ['name','email','telephone','company_name','message']
        
class ContactInquiryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['email'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['title'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['Full_address'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['zip_code'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['telephone'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['company_name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['product_type'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['needed_by'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['project_details'].widget.attrs.update({'class': 'form-control valid'})
    class Meta:
        model = ContactInquiry
        fields = ['name','email','title','Full_address','zip_code','telephone','company_name','product_type',
                  'quantity','needed_by','project_details']