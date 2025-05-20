from django.shortcuts import render
from django.contrib import messages
from datetime import datetime

def home(request):
    context = {
        'welcome_message': 'Welcome to Firewing Technologies',
        'current_year': datetime.now().year,
        'featured_projects': [
            {'name': 'Project Alpha', 'tech': 'AI/ML', 'image': 'project1.jpg'},
            {'name': 'Project Beta', 'tech': 'Cloud Computing', 'image': 'project2.jpg'},
            {'name': 'Project Gamma', 'tech': 'IoT Solutions', 'image': 'project3.jpg'},
        ]
    }
    return render(request, 'home.html', context)

def about(request):
    team_members = [
        {'name': 'John Doe', 'role': 'CEO', 'experience': '15+ years'},
        {'name': 'Jane Smith', 'role': 'CTO', 'experience': '12+ years'},
        {'name': 'Mike Johnson', 'role': 'Lead Developer', 'experience': '8+ years'},
    ]
    return render(request, 'about.html', {'team': team_members})

def services(request):
    services_list = [
        {
            'title': 'Web Development',
            'description': 'Custom web applications and solutions',
            'icon': 'fa-globe',
            'technologies': ['Django', 'React', 'Node.js']
        },
        {
            'title': 'Mobile Development',
            'description': 'iOS and Android app development',
            'icon': 'fa-mobile',
            'technologies': ['Flutter', 'React Native', 'Swift']
        },
        {
            'title': 'Cloud Solutions',
            'description': 'Cloud infrastructure and deployment',
            'icon': 'fa-cloud',
            'technologies': ['AWS', 'Azure', 'Google Cloud']
        }
    ]
    return render(request, 'services.html', {'services': services_list})

def portfolio(request):
    projects = [
        {
            'name': 'E-commerce Platform',
            'client': 'ABC Corp',
            'tech_stack': ['Django', 'React', 'PostgreSQL'],
            'image': 'project1.jpg'
        },
        {
            'name': 'Mobile Banking App',
            'client': 'XYZ Bank',
            'tech_stack': ['Flutter', 'Node.js', 'MongoDB'],
            'image': 'project2.jpg'
        }
    ]
    return render(request, 'portfolio.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        # Add form processing logic here
        messages.success(request, 'Thank you for contacting us!')
    
    contact_info = {
        'address': '123 Tech Street, Silicon Valley',
        'email': 'contact@firewing.com',
        'phone': '+1 234 567 8900'
    }
    return render(request, 'contact.html', {'contact_info': contact_info})

def careers(request):
    job_openings = [
        {
            'title': 'Senior Python Developer',
            'experience': '5+ years',
            'location': 'Remote',
            'type': 'Full-time'
        },
        {
            'title': 'UI/UX Designer',
            'experience': '3+ years',
            'location': 'On-site',
            'type': 'Full-time'
        }
    ]
    return render(request, 'careers.html', {'openings': job_openings})
