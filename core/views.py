from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from core.models import *

# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = 'core/index.html'
    success_url = '/'  # After submiting the form keep staying on the same url
    success_message = 'Your Form has been successfully submitted!'
    paginate_by = 5

    # override get context date method
    def get_context_data(self, **kwargs):
        # first, call super get context data
        context = super().get_context_data(**kwargs)
        context['about'] = AboutME.objects.first()
        context['exp'] = Experience.objects.all().order_by('-date_posted')
        context['test'] = Testimonial.objects.all()
        context['tags'] = CategoryList.objects.first()
        context['portfolio'] = Portfolios.objects.all().order_by('-date_posted')
        context['post'] = Portfolios.objects.all()
        context['blog'] = Blog.objects.all().order_by('-date_posted')
        return context


def detail_view(request, id):
    post = get_object_or_404(Portfolios, id=id)
    project = Portfolios.objects.all().order_by('-date_posted')

    context = {
        'post': post,
        'project': project
    }
    return render(request, 'core/detail.html', context)


def blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    context = {
        'blog': blog,
        # 'project': project
    }
    return render(request, 'core/post-single3.html', context)
