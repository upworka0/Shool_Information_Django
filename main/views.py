from django.shortcuts import render
from django.views.generic import ListView, DetailView
from administrator.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.
def home(request):
	return render(request, 'main/transparencyboard.html')

class PostListView(ListView):
	# photos = Photo.objects.all().order_by('-date_posted');
	# return render(request, 'main/gallery.html', {'photos': photos})
	model = Post
	template_name = 'main/post_list.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post
	template_name = 'main/post_detail.html'

class HomepageView(ListView):
	template_name = 'main/home.html'
	model = Post

	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		context['post_list'] = Post.objects.all()
		return context
