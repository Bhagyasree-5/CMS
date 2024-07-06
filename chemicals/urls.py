from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("add",views.add_chemical,name='add'),
    path("display",views.display_chemicals,name='display'),
    path("stock",views.stock,name='stock'),
    path('utenadd',views.addUtensil, name='utenadd'),
    path('utendisplay',views.utendisplay,name='utendisplay'),
    path('fineadd',views.addFine, name='fineadd'),
    path('finedisplay',views.finedisplay,name='finedisplay'),
    path('view/<int:chem_id>/',views.purchased_details,name='purchased_details'),
    path('Finerecive/<int:fine_id>/',views.fine_recived,name='fine_recived'),
    path('chemicals/delete/<int:pk>/', views.delete_chemical, name='delete_chemical'),
    path('utensils/delete/<int:id>/', views.delete_utensil, name='delete_utensil'),
    path('fines/delete/<int:pk>/', views.delete_fine, name='delete_fine'),
    path('add_stock/', views.add_stock, name='add_stock'),
    path('stock_list/', views.stock_list, name='stock_list'),
]