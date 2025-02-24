from django.shortcuts import render, get_object_or_404
from .models import Trainer, Category

def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainer/trainer_list.html', {'trainers': trainers})

def trainers_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    trainers = category.trainers.all()
    return render(request, 'trainer/trainers_by_category.html', {'category': category, 'trainers': trainers})

def trainer_detail(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    return render(request, 'trainer/trainer_detail.html', {'trainer': trainer})