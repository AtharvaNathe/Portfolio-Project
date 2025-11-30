from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# Resume data (single source of truth)
RESUME = {
    # Your Data.....
}

# convenience: first name (template-friendly)
RESUME['first_name'] = RESUME['name'].split()[0]

def index(request):
    return render(request, 'portfolio/index.html', {'r': RESUME})

@require_POST
@csrf_exempt  # If you prefer CSRF-protected AJAX, remove this and send CSRF header from JS.
def contact_endpoint(request):
    # Very simple endpoint — extend to store or send email
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    message = request.POST.get('message', '').strip()

    if not name or not email or not message:
        return JsonResponse({'ok': False, 'error': 'Missing fields'}, status=400)

    # TODO: integrate email sending (django.core.mail) or save to DB.
    # For now simply return success
    return JsonResponse({'ok': True})

