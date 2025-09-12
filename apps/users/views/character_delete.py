from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from esi.models import Token # Adjusted import for project structure

@require_POST
@login_required
def character_delete(request, character_id):
    # Only allow deletion of tokens belonging to the current user
    token = get_object_or_404(Token, character_id=character_id, user=request.user.id)
    token.delete()
    return redirect('users:characters')
