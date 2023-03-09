from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import (
    UserRegisterForm, 
    UserUpdateForm, 
    ProfileUpdateForm,
    ImageAddForm,
    )
from .models import MultipleImage, NoiseImage
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView)
#Libraries for distorting
from skimage import img_as_ubyte
from skimage.io import imread, imsave
from block_distortion import distort_image 

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#Must be logged in to be able to see profile
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                  request.FILES, instance =request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance =request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)




def segment(request):
    #Again filter for just the user
    cur_image = MultipleImage.objects.filter(segmented=False).first()
    #Check if the list is empty
    if cur_image:
        cur_image.segmented = True
        cur_image.save()
        return render(request, 'users/segment.html', {'cur_image': cur_image})
    #If empty, move to the Images with Noise
    else:
        #Guaranteed not to be segmented so you dont have to check
        cur_image = NoiseImage.objects.first()
        cur_image.segmented = True
        cur_image.save()
        return render(request, 'users/distorted_segment.html', {'cur_image': cur_image})


def distorted_segment(request):
    #Again filter for just the user
    cur_image = NoiseImage.objects.filter(segmented=False).first()
    #Check if the list is empty
    if cur_image:
        cur_image.segmented = True
        cur_image.save()
        return render(request, 'users/distorted_segment.html', {'cur_image': cur_image})
    #If empty, move to the Images with Noise
    else:
        images = MultipleImage.objects.all()
        #remove duplicate images
        image_form = ImageAddForm()
        duplicate_images = NoiseImage.objects.all()
        return render(request, 'users/pictures.html', {'form': image_form, 'images': images, 'dup_images':duplicate_images})



@login_required
def upload(request):
    if request.method == "POST":
        image_form = ImageAddForm(request.POST, request.FILES)
        if image_form.is_valid():
            #Save inital image
            image_form.instance.user = request.user
            image_form.save()
            #Distort Image for Noisey image and ave
            distorted_image = imread('/Users/chris/Desktop/user_API/' + MultipleImage.objects.filter(label=image_form.cleaned_data.get('label')).first().images.url)
            distorted_image = distort_image(distorted_image)
            imsave('/Users/chris/Desktop/user_API/media/distorted' + MultipleImage.objects.filter(label=image_form.cleaned_data.get('label')).first().images.url, img_as_ubyte(distorted_image))
            noise_image = NoiseImage(user = request.user, images ='/distorted' + MultipleImage.objects.filter(label=image_form.cleaned_data.get('label')).first().images.url, label = image_form.cleaned_data.get('label'))
            noise_image.save()
            


            
    else:
        image_form = ImageAddForm()
    #Make this just pertain to the user
    images = MultipleImage.objects.all()
    #remove duplicate images
    duplicate_images = NoiseImage.objects.all()
    return render(request, 'users/pictures.html', {'form': image_form, 'images': images, 'dup_images':duplicate_images})
