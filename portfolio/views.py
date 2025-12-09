from django.shortcuts import render


def index(request):
    context = {
        'members': [
            {
                'name': 'Honor',
                'specialty': 'Machine Learning, Web Development, Frontend Development',
                'experience': '5 years',
                'image': '/static/portfolio/honor.jpg'
            },
            {
                'name': 'Vargas',
                'specialty': 'Cloud Computing, Backend Development',
                'experience': '5 years',
                'image': '/static/portfolio/vargas.jpg'
            }
        ]
    }
    return render(request, 'portfolio/index.html', context)
