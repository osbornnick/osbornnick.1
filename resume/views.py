from django.shortcuts import render


def resume(request):
    context = {}
    return render(request, 'resume.html', context)
