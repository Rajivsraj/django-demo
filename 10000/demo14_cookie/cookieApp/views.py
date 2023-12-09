from django.shortcuts import render, HttpResponse, HttpResponseRedirect


# Create your views here.
def set_cookie_fun(request):
    # set cookie
    res = render(request, template_name="cookie1.html", context={"msg": "Cookie set"})
    res.set_cookie("email", "abhi@gmail.com", max_age=60*60*24*4)
    res.set_cookie("username", "abhi01")
    return res

# def set_cookie_fun(request):
#     # set cookie
#     request.COOKIES["username"] = "abhi01"
#     print(request.COOKIES)
#     data = request.COOKIES["username"]
#     print(data)
#     return render(request, template_name="cookie1.html", context={"msg": data})



def get_cookie_fun(request):
    # get cookie
    # data = request.COOKIES["username"]
    # print(data)
    print(request.COOKIES)
    # data = request.COOKIES["email"]
    data = request.COOKIES.get("email")
    data2 = request.COOKIES.get("username")

    print(data)
    print(data2)
    return render(request, template_name="get-cookie.html", context={"data":data, "data2":data2})


def del_cookie_fun(request):
    res = HttpResponseRedirect("/get-cookie/")
    res.delete_cookie("username")

    # print("res: ",res)
    return res