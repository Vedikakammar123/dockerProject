from django.db.models import Count
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import MyModel
import random

def form_page(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        image = request.FILES.get('image')

        if text and image:
            user_info = MyModel.objects.create(text=text, image=image)
            return redirect('thank_you', user_info_id=user_info.id)
    return render(request, 'home1.html')

def thank_you(request, user_info_id):
    user_info = MyModel.objects.get(id=user_info_id)
    return render(request, 'home2.html', {
        'user_info': user_info,
        'show_records_url': reverse('show_records')
    })

def show_records(request):
    all_user_info = MyModel.objects.values('text').annotate(text_count=Count('text'))
    sorted_data = sorted(list(all_user_info), key=lambda x: x['text_count'])

    labels = [item['text'] for item in sorted_data]
    data = [item['text_count'] for item in sorted_data]

    return render(request, 'show_records.html', {
        'user_info_list': MyModel.objects.all(),
        'chart_labels': labels,
        'chart_data': data,
        'show_records_url': reverse('show_records')
    })
