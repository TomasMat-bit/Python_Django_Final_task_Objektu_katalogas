from django.urls import path
from . import views
from .views import ItemUpdateView, ItemDeleteView, ItemCreateView

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('stats/', views.stats, name='stats'),
    path('item/add/', ItemCreateView.as_view(), name='item_add'),
    path('item/<int:pk>/edit/', ItemUpdateView.as_view(), name='item_edit'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
]
