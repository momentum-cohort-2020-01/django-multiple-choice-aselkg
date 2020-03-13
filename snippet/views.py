from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import Snippet, Lang, User



def homepage(request):
    snippets = Snippet.objects.all()
    return render(request, "code_snippet/homepage.html",{
        "snippets": snippets
        })


def code_create(request):
    return render(request,  "code_snippet/code_detail.html")

def code_edit(request):
    snippets = Snippet.objects.all()
    return render(request,  "code_snippet/code_detail.html",{
        "snippets": snippets
        })


def code_detail(request):
    snippets = Snippet.objects.all()
    return render(request,  "code_snippet/code_detail.html")