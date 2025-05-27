from django.shortcuts import render


def blog_view(request):
    return render(request=request, template_name='blog/index.html')
