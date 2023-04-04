from django.shortcuts import render



# Create your views here.

def form(request):

    print(request.method)

    data = request.POST
    # print(request.GET["fname"])
    # f = request.GET.get("fname")
    # print(f)
    return render(request, "form/one.html", {"userdata": data})



# def form(request):
#     data = request.GET
#     # print(request.GET["fname"])
#     # f = request.GET.get("fname")
#     # print(f)
#     return render(request, "form/one.html", {"userdata": data})




# # Create your views here.
# def form(request):
#     data = {}
#     if request.GET:
#         data = request.GET
#
#     print(data)
#     # if request.GET:
#     #     data["fn"] = request.GET["fname"]
#     #     data["ln"] = request.GET["lname"]
#     #     data["email"] = request.GET["email"]
#     #     data["pass"] = request.GET["password"]
#
#     print(data)
#
#     # return render(request, "form/one.html", {"userdata": data})
#     return render(request, "form/one.html", context={"userdata": data})
