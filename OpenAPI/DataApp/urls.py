from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import DummyDataView, DummyDataAPIView

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),  #OpenAPI schema 
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), #Swagger UI
    path('get-dummy-data/', DummyDataView.as_view(), name='dummy-data'),
    path('dummy-data/', DummyDataAPIView.as_view(), name='dummy-data-list'), #GET and POST 
    path('dummy-data/<int:pk>/', DummyDataAPIView.as_view(), name='dummy-data-detail') #PUT and DELETE
]

