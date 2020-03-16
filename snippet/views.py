from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from .models import Snippet, Language
from users.models import User
from .forms import SnippetForm, LanguageForm

@login_required
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
   def add_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.owner = request.user
            snippet.save()
            return redirect('user_home')
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'core/snippet_edit.html', {'snippet': snippet, 'form':form, 'pk': pk})


def snippet_delete(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.delete()
    return redirect('homepage')

@login_required
def lang_add(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            language = form.save()
            return redirect('homepage')
    else:
            form = LanguageForm()
    return render(request, 'core/add_language.html', {'form': form})



def get_queryset(self): # new
    query = self.request.GET.get('q')
    object_list = Snippet.objects.filter(
        Q(title__icontains=query) | Q(language__icontains=query)
    )
    return render(request, "core/homepage.html", {"object_list": object_list})

    # def snippet_by_lang(request, slug):
    #     lang = Language.objects.get(slug=slug)
    #     snippet_for_lang=SnippetForm.objects.filter(lang=lang)
    #     return render(request, 'core/snippet_by_lang.html', {'snippet':snippet_for_lang, 'lang': lang })