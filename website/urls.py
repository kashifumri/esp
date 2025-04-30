from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('products',views.products,name='products'),
    path('careers',views.careers,name='careers'),
    path('flame-detectors',views.flame_detectors,name='flame_detectors'),
    path('Products-Controllers-UPES',views.Products_Controllers_UPES,name='Products_Controllers_UPES'),
    path('Products-Toxic-Gas-Detectors',views.Products_Toxic_Gas_Detectors,name='Products_Toxic_Gas_Detectors'),
    path('Products-Toxic-Oxygen-product',views.Products_Toxic_Oxygen_product,name='Products_Toxic_Oxygen_product'),  
    
    path('Product_Combustible-Gas-Detectors',views.Product_Combustible_Gas_Detectors,name='Product_Combustible_Gas_Detectors'),
    path('product_combustible_gas_detectors_SGOES',views.product_combustible_gas_detectors_SGOES,name='product_combustible_gas_detectors_SGOES'),
    path('product-combustible-gas-detectors-tgaes',views.product_combustible_gas_detectors_tgaes,name='product_combustible_gas_detectors_tgaes'),
    path('product-combustible-gas-detectors-VECTOR-Combustible',views.product_combustible_gas_detectors_VECTOR_Combustible,name='product_combustible_gas_detectors_VECTOR_Combustible'),
    
    
    path('combustible-gas-detectors-tgaes',views.combustible_gas_detectors_tgaes,name='combustible_gas_detectors_tgaes'),
    path('Flame_Detectors_IPES_IR_UV',views.Flame_Detectors_IPES_IR_UV,name='Flame_Detectors_IPES_IR_UV'),
    path('Flame_Detectors_IPES_IR3',views.Flame_Detectors_IPES_IR3,name='Flame_Detectors_IPES_IR3'),
    # path('combustible-gas-detectors-tgaes',views.combustible_gas_detectors_tgaes,name='combustible_gas_detectors_tgaes'),
    # path('combustible-gas-detectors-tgaes',views.combustible_gas_detectors_tgaes,name='combustible_gas_detectors_tgaes'),
    
    path('rent',views.rent,name='rent'),
    path('contactus',views.contactus,name='contactus'),
    path('quate',views.quate,name='quate'),
    path('cat/<int:id>/',views.cat,name='cat'),
    path('sub-cat/<int:id>/',views.subcat,name='subcat'),
    path('product/<int:subcategory_id>/<int:id>/',views.product_details,name='product_details'),
    path('rent/<int:id>/',views.rent_details,name='rent_details'),
    
]