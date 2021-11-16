from django.shortcuts import get_object_or_404, render 
from .models import Category, Post

def blog(request):
    _all_posts= Post.objects.all()
    return render(request, "blog/blog.html",{"posteos":_all_posts})

#def category(request, category_id):
    _all_categories= get_object_or_404 (category, id= category_id) #_all_categories: category.objects.get(id=category_id)
    #me traigo el objeto de la category del from
    _all_posts= Post.objects.filter(categories=category)
    #me traigo los post que tenga la categoria
    return render(request, "blog/category.html", {"categorias": category, "posteos": _all_posts})

def category(request, category_id ):
    category = get_object_or_404(Category, id=category_id )
    return render(request, 'blog/category.html', { 'categoria': category })