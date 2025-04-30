from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import WebSiteSettingsForm,ProductForm, CategoryForm,TrandingProductsForm,ContactInquiryForm,\
    SubCategoryForm,RentAndHireProductForm#,ProductFormWithImages
from .models import WebsiteSettings,Product, ProductImage, Category,Contactus,TrandingProducts,ContactInquiry,\
    SubCategory,RentAndHireProduct,RentImage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

@login_required(login_url='/')
def home(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    return render(request,'customadmin/index.html',{'user':request.user,'obj':obj})

@login_required(login_url='/')
def Websitesettingviews(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    print('obj',obj)
    if obj:
        form = WebSiteSettingsForm(instance=obj)
    else:
        obj=None
        form = WebSiteSettingsForm()
    if request.method=="POST":
        form = WebSiteSettingsForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, f'WebSite Update successfully!')
            return redirect('customadmin:site')
        else:
            print('errrrrrrrr',form.errors)
            messages.error(request,form.errors)
    return render(request,'customadmin/website_setting.html',{'user':request.user,'form':form,'obj':obj})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'customadmin/category_list.html', {'categories': categories})

def subcategory_list(request):
    categories = SubCategory.objects.all()
    return render(request, 'customadmin/subcategory_list.html', {'categories': categories})

def product_list(request, category_id=None):
    category = None
    products = Product.objects.all()
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)
    return render(request, 'customadmin/product_list.html', {'products': products, 'category': category})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def delete_product_image(request, image_id):
    image = get_object_or_404(ProductImage, id=image_id)
    product_id = image.product.id
    image.delete()
    messages.success(request, f'Product Image has been removed successfully!')
    return redirect('customadmin:edit_product', product_id=product_id)

def delete_product(request, product_id):
    obj = get_object_or_404(Product, id=product_id)
    # product_id = image.product.id
    obj.delete()
    messages.success(request, f'Product has been deleted successfully!')
    return redirect('customadmin:product_list')

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid(): 
            product = form.save() 
            images = request.FILES.getlist('images')
            for img in images:
                ProductImage.objects.create(product=product, image=img)
            
            messages.success(request, f'Product has been created successfully!')
            return redirect('customadmin:product_list')
        else:
            
            messages.error(request, f'{form.errors}')
    else:
        form = ProductForm()
    return render(request, 'customadmin/add_product.html', {'form': form
                                                         })
    
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_images = ProductImage.objects.filter(product=product)  # Fetch existing images

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES,instance=product)

        if form.is_valid():
            product = form.save()
            images = request.FILES.getlist('images')
            for img in images:
                ProductImage.objects.create(product=product, image=img)  
                
                messages.success(request, f'Product has been updated successfully!')
            return redirect('customadmin:product_list')  
        else:
            
            messages.error(request, f'{form.errors}')
    else:
        form = ProductForm(instance=product)

    return render(request, 'customadmin/edit_product.html', {
        'form': form,
        'product': product,
        'product_images': product_images
    })


def rent_and_hire_list(request,category_id=None):
    category = None
    products = RentAndHireProduct.objects.all()
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)
    return render(request, 'customadmin/rent.html', {'products': products, 'category': category})
    products = Product.objects.all()
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)
    return render(request, 'customadmin/product_list.html', {'products': products, 'category': category})

def add_rent_and_hire(request):
    if request.method == "POST":
        form = RentAndHireProductForm(request.POST,request.FILES)
        if form.is_valid(): 
            product = form.save() 
            images = request.FILES.getlist('images')
            for img in images:
                RentImage.objects.create(product=product, image=img)
            
            messages.success(request, f'Rent and Hire has been created successfully!')
            return redirect('customadmin:rent_and_hire_list')
        else:
            
            messages.error(request, f'{form.errors}')
    else:
        form = RentAndHireProductForm()
    return render(request, 'customadmin/add_rent_product.html', {'form': form
                                                         })
    
def edit_rent_and_hire(request, product_id):
    product = get_object_or_404(RentAndHireProduct, id=product_id)
    product_images = RentImage.objects.filter(product=product)  # Fetch existing images

    if request.method == "POST":
        form = RentAndHireProductForm(request.POST, request.FILES,instance=product)

        if form.is_valid():
            product = form.save()
            images = request.FILES.getlist('images')
            for img in images:
                RentImage.objects.create(product=product, image=img)  
                
                messages.success(request, f'Rent and Hire has been updated successfully!')
            return redirect('customadmin:rent_and_hire_list')  
        else:
            
            messages.error(request, f'{form.errors}')
    else:
        form = RentAndHireProductForm(instance=product)

    return render(request, 'customadmin/edit_hire_product.html', {
        'form': form,
        'product': product,
        'product_images': product_images
    })
    
def delete_rent_and_hire(request, product_id):
    obj = get_object_or_404(RentAndHireProduct, id=product_id)
    # product_id = image.product.id
    obj.delete()
    messages.success(request, f'Rent and Hire has been deleted successfully!')
    return redirect('customadmin:rent_and_hire_list')

def delete_rent_and_hire_image(request, image_id):
    image = get_object_or_404(RentImage, id=image_id)
    product_id = image.product.id
    image.delete()
    messages.success(request, f'Rent and Hire Image has been removed successfully!')
    return redirect('customadmin:edit_rent_and_hire', product_id=product_id)
def rent_and_hire_detail(request, pk):
    pass
def add_category(request,id=None):
    if request.method == "POST":
        obj=None
        if id:
            obj = get_object_or_404(Category, id=id)
            form = CategoryForm(request.POST,request.FILES,instance=obj)
        else:
            form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, f'Category has been Added successfully!')
            return redirect('customadmin:category_list')
        else:
            # print('errr',form.errors)
            
            messages.error(request, f'{form.errors}')
    else:
        obj=None
        if id:
            obj = get_object_or_404(Category, id=id)
            form = CategoryForm(instance=obj)
        else:
            form = CategoryForm()
    
    return render(request, 'customadmin/category_add.html', {'form': form,'obj':obj})

def add_subcategory(request,id=None):
    if request.method == "POST":
        obj=None
        if id:
            obj = get_object_or_404(SubCategory, id=id)
            form = SubCategoryForm(request.POST,request.FILES,instance=obj)
        else:
            form = SubCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, f'Sub-Category has been Added successfully!')
            return redirect('customadmin:subcategory_list')
        else:
            # print('errr',form.errors)
            
            messages.error(request, f'{form.errors}')
    else:
        obj=None
        if id:
            obj = get_object_or_404(SubCategory, id=id)
            form = SubCategoryForm(instance=obj)
        else:
            form = SubCategoryForm()
    
    return render(request, 'customadmin/subcategory_add.html', {'form': form,'obj':obj})

def delete_category(request,id=None):
    if id:
        obj = get_object_or_404(Category, id=id)
        obj.delete()
        
        messages.success(request, f'Category has been removed successfully!')
        return redirect('customadmin:category_list')
    
def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = SubCategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse({'subcategories': list(subcategories)})
    
def delete_subcategory(request,id=None):
    if id:
        obj = get_object_or_404(SubCategory, id=id)
        obj.delete()
        
        messages.success(request, f'Sub-Category has been removed successfully!')
        return redirect('customadmin:subcategory_list')
    
def contactus_list(request):
    contactus = Contactus.objects.all()
    return render(request, 'customadmin/contact_list.html', {'contactus': contactus})

def quate_list(request):
    contactus = ContactInquiry.objects.all()
    return render(request, 'customadmin/quate.html', {'contactus': contactus})

def delete_quate(request,id=None):
    if id:
        obj = get_object_or_404(ContactInquiry, id=id)
        obj.delete()
        messages.success(request, f'quate has been removed successfully!')
        return redirect('customadmin:quate_list')

def delete_contactus(request,id=None):
    if id:
        obj = get_object_or_404(Contactus, id=id)
        obj.delete()
        messages.success(request, f'Contact us has been removed successfully!')
        return redirect('customadmin:contactus_list')
    
def details_quate(request,id=None):
    if id:
        obj=ContactInquiry.objects.filter(id=id).first()
        form=ContactInquiryForm(instance=obj)
        return render(request, 'customadmin/quate_details.html', {'form': form})
        
    
    
@login_required(login_url='/')
def TrandingProductsviews(request):
    obj=TrandingProducts.objects.filter(is_active=True).first()
    print('obj',obj)
    if obj:
        form = TrandingProductsForm(instance=obj)
    else:
        obj=None
        form = TrandingProductsForm()
    if request.method=="POST":
        form = TrandingProductsForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, f'Tranding Products Update successfully!')
            return redirect('customadmin:trandingproducts')
        else:
            print('errrrrrrrr',form.errors)
            messages.error(request,form.errors)
    return render(request,'customadmin/tranding_product.html',{'user':request.user,'form':form,'obj':obj})
    