from django.shortcuts import render

# Create your views here.
def query_set(request):
    return render(request, "app1/data.html")
