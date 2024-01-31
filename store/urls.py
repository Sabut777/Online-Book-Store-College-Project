from django.urls import path
from .import views

# from .views import LogoutView

urlpatterns = [
    path('',views.index, name='index'),
    path('add',views.addPhoto, name='add_photo'),
    path('photo/<str:pk>',views.viewPhoto, name='view_photo'),


    path('orderby', views.orderPrice, name='order_price'),

    path('ordername', views.orderName, name='order_name'),

    path('search', views.search, name='search'),

    path('login', views.loginAdmin, name='login'),

    path('logout', views.logoutAdmin, name='logout'),

    # path("logout/", LogoutView.as_view(), name="logout"),




    
]



