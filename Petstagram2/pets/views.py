from django.shortcuts import render, redirect

# Create your views here.
from Petstagram2.common.forms import CommentForm
from Petstagram2.common.models import Comment
from Petstagram2.core.clean_up import clean_up_files
from Petstagram2.pets.form import PetForm, EditPetForm
from Petstagram2.pets.models import Pet, Like


def list_pets(request):
    all_pets = Pet.objects.all()

    context = {
        'pets': all_pets,
    }

    return render(request, 'pet_list.html', context)

#
# def pet_details(request, pk):
#     pet = Pet.objects.get(pk=pk)
#     pet.likes_count = pet.like_set.count()
#     comments = pet.comment_set.all()
#     context = {
#         'pet': pet,
#         'comment_form': CommentForm(),
#         'comments': comments,
#     }
#
#     return render(request, 'pet_detail.html', context)
#variant 1
# def comment_pet(request, pk):
#     pet = Pet.objects.get(pk=pk)
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = Comment(
#             text=form.cleaned_data['text'],
#             pet=pet,
#         )
#         comment.save()
#     return redirect('pet details', pet.id)
# variant 2

def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    comments = pet.comment_set.all()
    print(pet)
    context = {
        'pet': pet,
        'comment_form': CommentForm(initial={'pet_pk':pk}),
        'comments': comments,
    }

    return render(request, 'pet_detail.html', context)



def comment_pet(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('pet details', pk)


def like_pet(request, pk):
    pet_to_like = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet_to_like,
    )
    like.save()
    return redirect('pet details', pet_to_like.id)

def create_pet(request):
    if request.method == 'POST':
        form = EditPetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list pets')

    context = {'form': PetForm(),}
    return render(request, 'pet_create.html', context)

def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        old_image = pet.image
        form = EditPetForm(request.POST,request.FILES, instance=pet)
        if form.is_valid():
            if old_image:
                clean_up_files(old_image.path)
            form.save()
            return redirect('list pets')

    context = {
        'form': EditPetForm(instance=pet),
        'pet': pet
    }
    return render(request, 'pet_edit.html', context)

def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('list pets')
    context = {
        'pet':pet,
    }
    return render(request, 'pet_delete.html', context)