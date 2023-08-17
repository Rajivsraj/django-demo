from django.shortcuts import render, HttpResponse


# Create your views here.
def set_session(request):
    request.session["username"] = "admin"
    return render(request, "sessionApp/index.html")


def get_session(request):
    usrnm = request.session.get("username")
    session = request.session
    print(session)
    print(list(session.items()))
    print(session.keys())
    print(session.values())
    # for x in request.session:
    #     print(x)
    if "username" in request.session:
        print("yes")
    else:
        print("no")
    return HttpResponse(usrnm)


# delete session
def logout(request):
    del request.session["username"]
    usrnm = request.session.get("username")
    return HttpResponse(usrnm)