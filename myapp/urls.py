from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from myapp import views

#Esto me genera automaticamente todas las urls para tasks, (GET - POST - PUT - DELETE)
router = routers.DefaultRouter()
router.register(r'fields', [views.get_data_view, views.input_view, views.get_all_data_view], 'fields')

urlpatterns = [
    path('input/<str:my_target_field>/', views.input_view, name='input'),
    path('get_data/<int:id>/', views.get_data_view, name='get_data'),
    path('get_all_data/', views.get_all_data_view, name="get_all_data"),
    path('docs/', include_docs_urls(title = "Fields api"))
]