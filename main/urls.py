from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'main'
urlpatterns = [
    path('news/', PostListView.as_view(), name='news'),
    path('news/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('', HomepageView.as_view(), name='home'),
    path('transparency/', home, name='pubreport-list'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
