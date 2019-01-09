from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'administrator'

urlpatterns = [
	path('posts/new/', PostCreateView.as_view(), name='post-create'),
	path('reports/new/', ReportCreateView.as_view(), name='report-create'),
	path('users/new/', UserCreateView.as_view(), name='user-create'),
	path('posts/', PostListView.as_view(), name='post-list'),
	path('posts/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
	path('students/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
	path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
	path('students/<int:pk>/delete', StudentDeleteView.as_view(), name='student-delete'),
	path('staff/new/', StaffCreateView.as_view(), name='staff-create'),
	path('students/new/', StudentCreateView.as_view(), name='student-create'),
	path('staff/', StaffListView.as_view(), name='staff-list'),
	path('students/', StudentListView.as_view(), name='student-list'),
	path('sections/', SectionListView.as_view(), name='section-list'),
	path('reports/', ReportListView.as_view(), name='report-list'),
	path('users/', UserListView.as_view(), name='user-list'),
	path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
	path('staff/<int:pk>/edit', StaffUpdateView.as_view(), name='staff-update'),
	path('reports/<int:pk>/edit', ReportUpdateView.as_view(), name='report-update'),
	path('users/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
	path('staff/<int:pk>/delete', StaffDeleteView.as_view(), name='staff-delete'),
	path('report/<int:pk>/delete', ReportDeleteView.as_view(), name='report-delete'),
	path('users/log/', LogEntryListView.as_view(), name='logentry-list'),
	path('', DashboardView.as_view(), name='dashboard'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
