from django.urls import path
from . import views

app_name='ecomapp'
urlpatterns=[
    path('',views.home,name='home'),
    path('all',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.Prodcatdetail,name='Prodcatdetail'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('forgot',views.forgot,name='forgot'),
]