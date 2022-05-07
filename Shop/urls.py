from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='Shop/Login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('brands/', brandspage, name='brands'),
    path('catalogues/', cataloguespage, name='catalogues'),
    path('shop/', boutiquepage, name='shop'),
    path('^catalogue(?P<cata_id>\d+)$', Shopbycatalogue, name='shopitem'),
    path('^catalogue(?P<brand_id>\d+)$', shopitembrand, name='shopitembrand'),
    path('^product(?P<product_id>\d+)$', productdetail, name='productdetail'),
    path('<int:product_id>/offre/', offredetail, name='offredetail'),

    path('', homepage, name='home'),
    path('offrepage/', offrepage, name='offrepage'),
    path('offrepage_reçus/', offres, name='offres'),
    path('Myarticle/', articles, name='articlesarticles'),
    path('addproduct', addproduct, name='addproduct'),
    path('Conversation/<int:offer_id>/', Conversation, name='Conversation'),
    path('<int:product_id>/modifier', Modifyproduct, name='Modifyproduct'),
    path('<int:product_id>/Supprimer', Deleteproduct, name='Deleteproduct'),
]

