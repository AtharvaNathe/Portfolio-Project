from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# Resume data (single source of truth)
RESUME = {
    'name': 'Atharva Anil Nathe',
    'title': 'Backend Developer — Java, Spring Boot, Django, ML',
    'phone': '+91-8975609030',
    'email': 'atharvanathe093@gmail.com',
    'location': 'Amravati, Maharashtra',
    'linkedin': 'https://linkedin.com/in/atharva-nathe',
    'github': 'https://github.com/AtharvaNathe',
    'objective': 'Backend developer with hands-on experience building scalable APIs, microservices, and AI/ML prototypes. Experienced with Spring Boot, Django, Docker and cloud integration.',
    'experience': [
        {
            'role': 'Trainee Application Developer Intern (On-site)',
            'org': 'SohamGlobal, Amravati',
            'period': 'Feb–Jul 2025',
            'desc': 'Developed REST APIs and backend modules with Spring Boot, JPA, MySQL, MongoDB and integrated AI features using OpenAI API.'
        }
    ],
    'skills': ['Java', 'Python', 'Django', 'Spring Boot', 'REST', 'MySQL', 'MongoDB', 'Docker', 'OpenAI API', 'OpenCV'],
    'projects': [
        {'name': 'E-Commerce Webapp', 'tech': 'Spring Boot, Docker, MySQL', 'link': 'https://github.com/AtharvaNathe/E-commerce-Web-App-in-Spring-Java'},
        {'name': 'Predator AI-Vision', 'tech': 'Python, OpenCV, DeepFace', 'link': 'https://github.com/AtharvaNathe/Predator-AI-Vision'},
        {'name': 'Plant Health Prediction', 'tech': 'Django, TensorFlow', 'link': 'https://github.com/AtharvaNathe/Plant-Whisperer'},
    ],
    'education': [
        {'degree': 'B.E. in Computer Science', 'inst': 'Sipna COET, Amravati', 'year': 'Expected 2026', 'extra': 'CGPA: 7.25'},
    ],
    'certifications': [
        'Java Full Stack Developer Internship – AICTE + EduSkills (2025)',
        'Enterprise Java Development Certificate – SohamGlobal + Microsoft (2025)'
    ],
    'achievements': [
        'Group Leader — Smart India Hackathon (SIH)',
        'Group Leader — Techno Vision Hackathon'
    ]
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
