from django.shortcuts import render

from .services.spellchecker import process_text

from .forms import TextForm


def index(request):
    if request.method == 'POST':
        text_form = TextForm(request.POST)
        if text_form.is_valid():
            print(process_text(text_form.cleaned_data['text']))
    text_form = TextForm()
    context = {'text_form': text_form}
    return render(request, 'index.html', context=context)
