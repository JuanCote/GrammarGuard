from django.shortcuts import render

from .services.text_analysis import analyze_text
from .forms import TextForm


def index(request):
    text_form = TextForm()
    context = {"text_form": text_form}
    return render(request, "index.html", context=context)


def analysis_results(request):
    if request.method == "POST":
        text_form = TextForm(request.POST)
        context = {"text_form": text_form}
        if text_form.is_valid():
            analysis_result = analyze_text(text_form.cleaned_data["text"])
            context["analysis_result"] = analysis_result
            return render(request, "analysis_result.html", context=context)
