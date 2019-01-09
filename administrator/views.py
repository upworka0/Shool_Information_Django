from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.admin.models import LogEntry
from django.db.models import Q

# Create your views here.
class StudentCreateView(LoginRequiredMixin, CreateView, SuccessMessageMixin):
	model = Student
	form_class = StudentCreateForm
	success_message = "Student added successfully."
	template_name = 'administrator/student_create.html'

	def form_valid(self, form):
		messages.success(self.request, self.success_message)
		return super().form_valid(form)

class StudentUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
	model = Student
	fields = '__all__'
	success_message = "Student updated successfully."

class StudentListView(LoginRequiredMixin, ListView):
	model = Student
	paginate_by = 10
	# ordering = ['section__grade_level', 'section__name', 'last_name']

	def get_queryset(self):
		query = self.request.GET.get('q')
		student_list = self.model.objects.all().order_by('-section__grade_level')
		if query is not None:
			student_list = student_list.filter(
			Q(first_name__icontains=query) |
			Q(middle_name__icontains=query) |
			Q(last_name__icontains=query) |
			Q(lrn__icontains=query)
			)
		return student_list

# class StudentBulkDeleteView(View):
#     model = Student
#
#     def post(self, request, *args, **kwargs):
#         delete_ids = request.POST['delete_ids'].split(',')  # should validate
#         self.model.objects.filter(pk__in=delete_ids).delete()
#         return reverse_lazy('student-list')

class ReportListView(LoginRequiredMixin, ListView):
	model = Report
	context_object_name = 'reports'
	ordering = ['-month_year']

class ReportUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
	model = Report
	fields = ['title', 'remarks', 'file', 'month_year']
	success_message = 'Report updated successfully.'

class StudentDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
	model = Student
	success_url = reverse_lazy('student-list')
	success_message = "Student deleted successfully."

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(StudentDeleteView, self).delete(request, *args, **kwargs)

class LogEntryListView(LoginRequiredMixin, ListView):
	model = LogEntry
	context_object_name = 'actions'
	template_name = "administrator/logentry_list.html"
	ordering = ['-action_time']
	paginate_by = 10

class PostListView(LoginRequiredMixin, ListView):
	model = Post
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostCreateView(LoginRequiredMixin, CreateView, SuccessMessageMixin):
	model = Post
	fields = ['title', 'desc', 'image']
	success_message = "Post created successfully."
	template_name = 'administrator/post_create.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		messages.success(self.request, self.success_message)
		return super().form_valid(form)

class ReportCreateView(LoginRequiredMixin, CreateView, SuccessMessageMixin):
	model = Report
	fields = ['title', 'remarks', 'file', 'month_year']
	success_message = "Report uploaded successfully."
	template_name = 'administrator/report_create.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		messages.success(self.request, self.success_message)
		return super().form_valid(form)

class ReportDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
	model = Report
	success_url = reverse_lazy('report-list')
	success_message = "Report deleted successfully."

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(ReportDeleteView, self).delete(request, *args, **kwargs)

class PostUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
	model = Post
	fields = ['title', 'desc', 'image']
	success_message = "Post updated successfully."

class PostDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
	model = Post
	success_url = reverse_lazy('post-list')
	success_message = "Post deleted successfully."

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(PostDeleteView, self).delete(request, *args, **kwargs)

class DashboardView(LoginRequiredMixin, ListView):
	context_object_name = 'students'
	template_name = 'administrator/dashboard.html'
	queryset = Student.objects.all()

	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		context['staffs'] = Staff.objects.all()
		context['users'] = User.objects.all()
		context['reports'] = Report.objects.all()
		context['posts'] = Post.objects.all()
		return context

class StaffCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
	model = Staff
	form_class = StaffCreateForm
	template_name = 'administrator/staff_create.html'
	success_message = 'Staff profile created.'

class StaffListView(LoginRequiredMixin, ListView):
	model = Staff
	context_object_name = 'staffs'
	ordering = ['-salary']

class SectionListView(LoginRequiredMixin, ListView):
	model = Section

	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		query = self.request.GET.get('SY')
		if query is None:
			sections = Section.objects.filter(term=Term.objects.latest('start_date'))
		else:
			sections = Section.objects.filter(term__title=query)
		context['terms'] = Term.objects.all().order_by('-start_date')
		context['sections']=sections
		# for i in range(0, 6):
		#     key = 'grade{}'.format(i)
		#     context[key] = sections.filter(grade_level=i)
		return context




class StaffDetailView(LoginRequiredMixin, DetailView):
	model = Staff

class StaffUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
	model = Staff
	fields = ['image',
	'first_name',
	'last_name',
	'middle_name',
	'contact_number',
	'birthdate',
	'sex',
	'civil_status',
	'advisory_section',
	'position',
	'salary',
	'appointment_file',
	'pds_file',
	'prc_license_file',
	'saln_file']
	success_message = "Profile updated successfully."
	# form_class = StaffCreateForm

class StaffDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
	model = Staff
	success_url = reverse_lazy('staff-list')
	success_message = "Profile deleted successfully."

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(StaffDeleteView, self).delete(request, *args, **kwargs)

class UserCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
	model = User
	fields = ['first_name', 'last_name', 'username', 'password', 'groups']
	template_name = 'administrator/user_create.html'
	success_message = 'User created.'
	success_url = reverse_lazy('user-list')

class UserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
	model = User
	template_name = 'administrator/user_form.html'
	fields = ['first_name', 'last_name' , 'username', 'password', 'groups', 'is_active']
	success_message = 'User updated successfully.'
	success_url = reverse_lazy('user-list')

	def form_valid(self, form):
		form.instance.set_password(form.instance.password)
		return super().form_valid(form)

class UserListView(LoginRequiredMixin, ListView):
	model = User
	template_name = 'administrator/user_list.html'
	context_object_name = 'user_list'
	ordering = ['groups']
