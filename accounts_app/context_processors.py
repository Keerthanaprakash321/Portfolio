from .models import Profile

def profile_context(request):
    try:
        return {'profile': Profile.objects.first()}
    except Exception:
        return {'profile': None}
