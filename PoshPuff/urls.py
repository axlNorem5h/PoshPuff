from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="homePage"),
    path('about/', views.about_page, name="aboutPage"),
    path('product/', views.product_page, name="productPage"),
    path('contact/', views.contact_page, name="contactPage"),
    path('dashboard/', views.dashboard_page, name="dashboard"),
    path('productform/', views.productform_page, name="productformPage"),
    path('create_product/', views.create_product, name='create_product'),
    path('view_product/<int:product_id>/', views.view_product, name='view_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),

]
