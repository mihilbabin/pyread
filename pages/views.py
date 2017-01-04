from django.shortcuts import render, get_object_or_404
from .models import Category, Page


def index(request):
    categories = Category.objects.order_by("-likes")[:5]
    most_viewed_pages = Page.objects.order_by("-views")[:5]
    return render(request, 'pages/index.html', {'categories': categories,
                                                'pages': most_viewed_pages})


def about(request):
    return render(request, 'pages/about.html')

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    pages = category.pages.all()
    return render(request, 'pages/detail.html', {'category': category, 'pages': pages})
