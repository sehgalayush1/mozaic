from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def index(request):
	post_lists = Post.objects.order_by('-pub_date', '-pk')
	category_list = Category.objects.all()
	paginator = Paginator(post_lists, 5)
	page = request.GET.get('page')
	try:
		post_list = paginator.page(page)
	except PageNotAnInteger:
		post_list = paginator.page(1)
	except EmptyPage:
		post_list = paginator.page(paginator.num_pages)

	context = {
		'post_list' : post_list,
		'category_list' : category_list
	}
	return render(request, 'blog/index.html', context)

def post(request, post_id):
	category_list = Category.objects.all()
	try:
		p = Post.objects.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404("Post does not exist")
	context = {
		'post' : p,
		'category_list': category_list
	}
	return render(request, 'blog/post.html', context)


def category(request, category_name):
	category_list = Category.objects.all()
	post_lists = Post.objects.filter(category__category_name=category_name).order_by('-pub_date', '-pk')
	paginator = Paginator(post_lists, 5)
	page = request.GET.get('page')
	try:
		post_list = paginator.page(page)
	except PageNotAnInteger:
		post_list = paginator.page(1)
	except EmptyPage:
		post_list = paginator.page(paginator.num_pages)

	context = {
		'post_list' : post_list,
		'category_list': category_list
	}
	return render(request, 'blog/categorypost.html', context)


def team(request):
	author_list = Author.objects.all()
	category_list = Category.objects.all()
	return render(request, 'blog/ourteam.html', {"author_list":author_list, "category_list":category_list})



def contact_us(request):
	category_list = Category.objects.all()
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		if name and email and message:
			try:
				send_mail(name, message + "\n" + email, email, ['sehgalayush26@gmail.com'])
			except BadHeaderError:
				return render(request, 'blog/contact_us.html', {"error":"Something went wrong. Please try again.", "category_list":category_list})
			return render(request, 'blog/contact_us.html', {"success":"Thank You for writing to us.", "category_list":category_list})
		else:
			return render(request, 'blog/contact_us.html', {"error":"Please make sure all fields are entered correctly.", "category_list":category_list})
	else:
		return render(request, 'blog/contact_us.html', {"category_list":category_list})
