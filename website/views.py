from django.shortcuts import render
from customadmin.models import WebsiteSettings,Category,Product,TrandingProducts,SubCategory,\
    RentAndHireProduct,Contactus,ContactInquiry
# from customadmin.models import Category,Product
from django.shortcuts import render, redirect, get_object_or_404
from customadmin.forms import ContactusForm,ContactInquiryForm
from django.contrib import messages


def CatWiseProduct():
    cat_wise_product = []

    catlist = Category.objects.all()
    print('list:', catlist)

    for i in catlist:
        catdict = {}
        catdict['cat_id'] = i.id
        catdict['cat_name'] = i.name

        subcat_list = []
        for j in i.subcategories.all():
            subcat_dict = {}
            subcat_dict['subcat_id'] = j.id
            subcat_dict['subcat_name'] = j.name
            subcat_dict['products'] = list(j.products.all().values())  # or use serializers if needed

            subcat_list.append(subcat_dict)

        catdict['subcategories'] = subcat_list
        cat_wise_product.append(catdict)

    print("*" * 100)
    print(cat_wise_product)
    return cat_wise_product

# Create your views here.
def index(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    cat=Category.objects.all()
    cat_wise_product=CatWiseProduct()
    tranding_product=TrandingProducts.objects.filter(is_active=True).first()
    
    catlist=Category.objects.all()
    print('list:',catlist)
    index_product=[]
    for i in catlist:
        catdict={}
        catdict['id']=i.id
        catdict['image']=i.image
        catdict['name']=i.name
        catdict['product']=i.products.all()
        index_product.append(catdict)
    return render(request,'web/index.html',{'obj':obj,'cat':cat,'cat_wise_product':cat_wise_product,
                                            'tranding_product':tranding_product,'index_product':index_product})
    
def contactus(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    cat=Category.objects.all()
    cat_wise_product=CatWiseProduct()
    form=ContactusForm()
    if request.method=='POST':
        form=ContactusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Form submited successfully!')
            return redirect('web:contactus')
        else:
            print('errrrrrrrr',form.errors)
            messages.error(request,form.errors)
    return render(request,'web/contactus.html',{'obj':obj,'cat':cat,'cat_wise_product':cat_wise_product,
                                            'form':form})
    
def quate(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    cat=Category.objects.all()
    cat_wise_product=CatWiseProduct()
    form=ContactInquiryForm()
    if request.method=='POST':
        form=ContactInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Form submited successfully!')
            return redirect('web:quate')
        else:
            print('errrrrrrrr',form.errors)
            messages.error(request,form.errors)
    return render(request,'web/quate.html',{'obj':obj,'cat':cat,'cat_wise_product':cat_wise_product,
                                            'form':form})

def aboutus(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    cat=Category.objects.all()
    cat_wise_product=CatWiseProduct()
    return render(request,'web/about.html',{'obj':obj,'cat':cat,'cat_wise_product':cat_wise_product})

def products(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    cat=Category.objects.all()
    cat_wise_product=CatWiseProduct()
    return render(request,'web/product.html',{'obj':obj,'cat':cat,'cat_wise_product':cat_wise_product})

def careers(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    cat=Category.objects.all()
    cat_wise_product=CatWiseProduct()
    return render(request,'web/carrers.html',{'obj':obj,"cat":cat,'cat_wise_product':cat_wise_product})

def flame_detectors(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    return render(request,'web/Products_Flame_Detectors.html',{'obj':obj})

def Products_Controllers_UPES(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    return render(request,'web/Products_Controllers_UPES.html',{'obj':obj})

def Products_Toxic_Gas_Detectors(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    return render(request,'web/Products_Toxic_Gas_Detectors.html',{'obj':obj})

def Products_Toxic_Oxygen_product(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    return render(request,'web/Products_Toxic_Oxygen_product.html',{'obj':obj})

def Product_Combustible_Gas_Detectors(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    return render(request,'web/Product_Combustible-Gas-Detectors.html',{'obj':obj})

def product_combustible_gas_detectors_SGOES(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    return render(request,'web/product_combustible_gas_detectors_SGOES.html',{'obj':obj})

def product_combustible_gas_detectors_tgaes(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    return render(request,'web/product-combustible-gas-detectors-tgaes.html',{'obj':obj})

def product_combustible_gas_detectors_VECTOR_Combustible(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    return render(request,'web/product-combustible-gas-detectors-VECTOR-Combustible.html',{'obj':obj})



def combustible_gas_detectors_tgaes(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    return render(request,'web/combustible-gas-detectors-tgaes.html',{'obj':obj})

def Flame_Detectors_IPES_IR_UV(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    return render(request,'web/Flame_Detectors_IPES_IR_UV.html',{'obj':obj})

def Flame_Detectors_IPES_IR3(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    return render(request,'web/Flame_Detectors_IPES_IR3.html',{'obj':obj})

# def cat(request, id):
#     obj = WebsiteSettings.objects.filter(is_active=True).first()
#     category = get_object_or_404(Category, id=id)  
#     product = Product.objects.filter(category=category.id) if category else Product.objects.none()
#     cat=Category.objects.all()
#     cat_wise_product=CatWiseProduct()
#     subcategories = category.subcategories.prefetch_related('products')
#     print('%'*100)
#     print(subcategories)
#     products_without_subcategory = Product.objects.filter(category=category, subcategory__isnull=True)
#     return render(request, 'web/cat.html', {'obj': obj,'product': product,'category':category,'cat':cat,
#                                             'cat_wise_product':cat_wise_product,'subcategories':subcategories,
#                                             'products_without_subcategory':products_without_subcategory})
    
def cat(request, id):
    obj = WebsiteSettings.objects.filter(is_active=True).first()
    category = get_object_or_404(Category, id=id)  
    cat=Category.objects.all()
    subcategories = SubCategory.objects.filter(category=category)
    cat_wise_product=CatWiseProduct()
    print('%'*100)
    print(subcategories)
    products_without_subcategory = Product.objects.filter(category=category, subcategory__isnull=True)
    return render(request, 'web/cat.html', {'obj': obj,'category':category,'cat':cat,
                                            'subcategories':subcategories,'cat_wise_product':cat_wise_product,
                                            'products_without_subcategory':products_without_subcategory})
    
def subcat(request, id):
    obj = WebsiteSettings.objects.filter(is_active=True).first()
    cat=Category.objects.all()
    subcategory = get_object_or_404(SubCategory, id=id)  
    cat_wise_product=CatWiseProduct()
    product = Product.objects.filter(subcategory=id) if id else Product.objects.none()
    return render(request, 'web/subcat.html', {'obj': obj,'cat':cat,
                                            'subcategory':subcategory,
                                            'cat_wise_product':cat_wise_product,
                                            'product':product})
    
    
def product_details(request,id,subcategory_id):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    product = get_object_or_404(Product, id=id)  
    category = get_object_or_404(SubCategory, id=subcategory_id)  
    cat=Category.objects.all()
    cat_wise_product=CatWiseProduct()
    return render(request,'web/dynamic_product.html',{'obj':obj,'product':product,'category':category,
                                                      'cat':cat,'cat_wise_product':cat_wise_product})

def rent(request):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    cat_wise_product=CatWiseProduct()
    cat=Category.objects.all()
    rentandhire=RentAndHireProduct.objects.all()
    return render(request,'web/rent.html',{'obj':obj,'cat':cat,'cat_wise_product':cat_wise_product,
                                           'rentandhire':rentandhire})
    
def rent_details(request,id):
    obj=WebsiteSettings.objects.filter(is_active=True).first()
    cat_wise_product=CatWiseProduct()
    rentandhire = get_object_or_404(RentAndHireProduct, id=id)  
    cat=Category.objects.all()
    # category = get_object_or_404(SubCategory, id=category_id) 
    # rentandhire=RentAndHireProduct.objects.filter(category=id) if id else RentAndHireProduct.objects.none()
    return render(request,'web/rent_details.html',{'obj':obj,'cat':cat,
                                                   'cat_wise_product':cat_wise_product,
                                                   'rentandhire':rentandhire})




# scp -i esp.pem mainesp.zip ubuntu@13.235.87.123:/home/ubuntu
# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Root@123';
# database:esp

# [program:gunicorn]
# directory=/home/ubuntu/mainesp
# command=/home/ubuntu/env/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/mainesp/app.sock mainesp.wsgi:application  
# autostart=true
# autorestart=true
# stderr_logfile=/var/log/gunicorn/gunicorn.err.log
# stdout_logfile=/var/log/gunicorn/gunicorn.out.log

# [group:guni]
# programs:gunicorn  