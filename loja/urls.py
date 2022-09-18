from django.urls import path
from loja import views

urlpatterns = [
    path('', views.home, name='url_home'),
    
    path('produto/create', views.createProduto, name='createProduto'),
    path('produto/read', views.readProduto, name='readProduto'),
    path('produto/update/<int:pk>/', views.updateProduto, name='updateProduto'),
    path('produto/delete/<int:pk>/', views.deleteProduto, name='deleteProduto'),
    
    path('pedido/create', views.createPedido, name='createPedido'),
    path('pedido/read', views.readPedido, name='readPedido'),
    path('pedido/update/<int:pk>/', views.updatePedido, name='updatePedido'),
    path('pedido/delete/<int:pk>/', views.deletePedido, name='deletePedido'),
]