from django.shortcuts import render


# Create your views here.
def home(request, id):
    return render(request, "home.html", {"post_id":id})


def characters(request, name):
    return render(request, "string.html", {"stu_name":name})


def slug(request, ok):
    return render(request, "slug.html", {"slug_val":ok})


def any_value(request, abc):
    print(abc)
    return render(request, "slug.html", {"any_val":abc})