
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . models import TributeMessage
from . forms import TributeForm


def index(request):
    tributes = TributeMessage.objects.all()

    page_num = request.GET.get('page', 1)
    paginator = Paginator(tributes, 3)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = TributeForm(request.POST)
        if form.is_valid():
            new_tribute = TributeMessage(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
            )
            new_tribute.save()

            context = {
                'name' : form.cleaned_data['name'],
                'email' : form.cleaned_data['email'],
                'text' : form.cleaned_data['text'],
            }

            return render(request, 'thankyou.html', context = context)
    else:
        form = TributeForm()
    
    
    context = {
        'tributes': tributes,
        'page_obj': page_obj,
        'form' : form
    }
    return render(request, 'index.html', context=context)

# Create your views here.
