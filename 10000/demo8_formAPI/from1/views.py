from django.shortcuts import render


# Create your views here.
def register(request):
    print(request)

    return render(request, "form.html", context={"frm": request.GET})



def register_post(request):

    print("hello get")
    if request.method == "POST":
        print("hello post")
        form_data = request.POST
        print(form_data)

        return render(request, "post-form.html", context={"frm": form_data})

    return render(request, "post-form.html")