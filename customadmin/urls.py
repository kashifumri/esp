from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('site',views.Websitesettingviews,name='site'),
    path('trandingproducts',views.TrandingProductsviews,name='trandingproducts'),
    path('categorylist/', views.category_list, name='category_list'),
    path('subcategorylist/', views.subcategory_list, name='subcategory_list'),
    path('products/', views.product_list, name='product_list'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('product/image/delete/<int:image_id>/', views.delete_product_image, name='delete_product_image'),
    path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/category/<int:category_id>/', views.product_list, name='product_list_by_category'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    
    path('rent-and-hire-list/', views.rent_and_hire_list, name='rent_and_hire_list'),
    path('add-rent-and-hire/', views.add_rent_and_hire, name='add_rent_and_hire'),
    path('edit-rent-and-hire/<int:product_id>/', views.edit_rent_and_hire, name='edit_rent_and_hire'),
    path('rent-and-hire/image/delete/<int:image_id>/', views.delete_rent_and_hire_image, name='delete_rent_and_hire_image'),
    path('rent-and-hire/delete/<int:product_id>/', views.delete_rent_and_hire, name='delete_rent_and_hire'),
    path('rent-and-hire/<int:pk>/', views.rent_and_hire_detail, name='rent_and_hire_detail'),
    path('add-product/', views.add_product, name='add_product'),
    path('add-category/', views.add_category, name='add_category'),
    path('update-category/<int:id>/', views.add_category, name='update_category'),
    path('delete-category/<int:id>/', views.delete_category, name='delete_category'),
    path('add-subcategory/', views.add_subcategory, name='add_subcategory'),
    path('update-subcategory/<int:id>/', views.add_subcategory, name='update_subcategory'),
    path('delete-subcategory/<int:id>/', views.delete_subcategory, name='delete_subcategory'),
    path('contact-us', views.contactus_list, name='contactus_list'),
    path('delete-contact-us/<int:id>/', views.delete_contactus, name='delete_contactus'),
    path('quate', views.quate_list, name='quate_list'),
    path('delete-quate/<int:id>/', views.delete_quate, name='delete_quate'),
    path('details-quate/<int:id>/', views.details_quate, name='details_quate'),
    path('get-subcategories/', views.get_subcategories, name='get_subcategories'),
    
]