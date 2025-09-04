from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile(request):
    """Render the user profile / account settings placeholder page."""
    return render(request, 'profile.html')
