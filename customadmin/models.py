from django.db import models
import os
from ckeditor.fields import RichTextField
# Create your models here.
class WebsiteSettings(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='webimage/',null=True,blank=True)
    address1=models.CharField(max_length=255)
    number1=models.CharField(max_length=10)
    number2=models.CharField(max_length=10,null=True,blank=True)
    address2=models.CharField(max_length=255,null=True,blank=True)
    is_active=models.BooleanField(default=True)
    
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category_images/')
    description = RichTextField()
    tag_line = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    def delete(self, using=None, keep_parents=False):
        if self.image:
            self.image.delete(save=False)  # Delete file from storage
        super().delete(using=using, keep_parents=keep_parents)
        
    def save(self, *args, **kwargs):
        """ Delete old image when a new one is uploaded """
        if self.pk:  # Only check for old image if instance already exists
            try:
                old_category = Category.objects.get(pk=self.pk)
                if old_category.image and self.image and old_category.image != self.image:
                    old_category.image.delete(save=False)  # Delete old image
            except Category.DoesNotExist:
                pass  

        super().save(*args, **kwargs)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='subcategory_images/', blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('category', 'name')
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return f"{self.category.name} - {self.name}"
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    name = models.CharField(max_length=255)
    description =  RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    pdf =models.FileField(upload_to='product/pdf/',null=True,blank=True)

    def __str__(self):
        return self.name
    
    def delete(self, using=None, keep_parents=False):
        for image in self.images.all():
            image.delete()
        super().delete(using=using, keep_parents=keep_parents)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
        
        
class RentAndHireProduct(models.Model):
    category = models.ForeignKey(Category, related_name='rentproducts', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description =  RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    pdf =models.FileField(upload_to='product/pdf/',null=True,blank=True)
    tag_line1 = models.TextField()
    tag_line2 = models.TextField()
    tag_line3 = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    def delete(self, using=None, keep_parents=False):
        for image in self.rentimages.all():
            image.delete()
        super().delete(using=using, keep_parents=keep_parents)

class RentImage(models.Model):
    product = models.ForeignKey(RentAndHireProduct, related_name='rentimages', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='rent_and_hire_images/')

    def __str__(self):
        return f"Image for {self.product.name}"
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
        
class Contactus(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=500)
    street_address = models.CharField(max_length=500,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    state = models.CharField(max_length=255,null=True,blank=True)
    zipcode = models.CharField(max_length=255,null=True,blank=True)
    country = models.CharField(max_length=255,null=True,blank=True)
    telephone = models.CharField(max_length=10)
    company_name = models.CharField(max_length=255,null=True,blank=True)
    message = models.TextField()
    
class TrandingProducts(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='TrandingProduct/')
    keyfeature1 = models.CharField(max_length=500)
    keyfeature2 = models.CharField(max_length=500,null=True,blank=True)
    keyfeature3 = models.CharField(max_length=500,null=True,blank=True)
    keyfeature4 = models.CharField(max_length=500,null=True,blank=True)
    is_active =models.BooleanField(default=True)
    
class ContactInquiry(models.Model):
    # Address Fields
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    email = models.CharField(max_length=500)
    Full_address = models.CharField(max_length=600)
    zip_code = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255)

    # Inquiry Details
    product_type = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    needed_by = models.DateField(blank=True, null=True)
    project_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.company_name} ({self.telephone})"
    