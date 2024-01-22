from django.shortcuts import render

from .services.text_analysis import analyze_text


def index(request):
    return render(request, "index.html")


def analysis_results(request):
    if request.method == "POST":
        text = request.POST.get("textarea")
        context = {}
        analysis_result = analyze_text(text)
        context["analysis_result"] = analysis_result
        return render(request, "analysis_result.html", context=context)
