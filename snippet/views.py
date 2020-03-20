from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from .models import Snippet, Language
from users.models import User
from .forms import SnippetForm


def homepage(request):
    snippets = Snippet.objects.all()
    languages = Language.objects.all()
    return render(request, "core/homepage.html", {"snippets": snippets, "languages": languages})


@login_required
def snippet_create(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save()
            return redirect('homepage')
    else:
        form = SnippetForm()

    return render(request, 'core/snippet_create.html', {"form": form})



def snippet_detail(request, pk):
    snippet = Snippet.objects.get(pk=pk)
    return render(request, "core/snippet_detail.html", {'snippet': snippet, 'pk': pk})

def snippet_edit(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            snippet = form.save()
            return redirect('homepage')
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'core/snippet_edit.html', {'snippet': snippet, 'form':form, 'pk': pk})


def snippet_delete(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.delete()
    return redirect('homepage')


def lang_add(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            language = form.save()
            return redirect('homepage')
    else:
            form = LanguageForm()
    return render(request, 'core/snippet_create.html', {'form': form})

def public(request):
    snippets = Snippet.objects.all()
    languages = Language.objects.all()
    return render(request, "core/public.html", {"snippets": snippets, "languages": languages})