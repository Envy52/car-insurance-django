from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile, _ = Profile.objects.get_or_create(user=user)
            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']
                profile.save()

            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile.first_name = request.POST.get('first_name')
        profile.last_name = request.POST.get('last_name')
        if request.FILES.get('avatar'):
            profile.avatar = request.FILES['avatar']
        profile.save()
        return redirect('profile')

    return render(request, 'accounts/profile.html', {'profile': profile})
