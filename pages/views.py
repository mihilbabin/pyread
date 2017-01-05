from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Page
from .forms import CategoryForm, PageForm


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
    return render(request, 'pages/category/detail.html', {'category': category, 'pages': pages})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('root')
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    return render(request, 'pages/category/create.html', {'form': form})

def page_create(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.category = category
            page.save()
            return redirect(category)
        else:
            print(form.errors)
    else:
        form = PageForm()
    return render(request, 'pages/create.html', {'form': form, 'category': category})
