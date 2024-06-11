from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='prediccion_index'),
    path('detalle/', views.detalle, name='prediccion_detalle'),

]
