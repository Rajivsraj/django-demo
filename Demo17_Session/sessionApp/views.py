from django.shortcuts import render, HttpResponse
import time

# Create your views here.
def set_session(request):
    request.session["username"] = "admin"
    request.session["password"] = "admin@123"
    request.session["email"] = "admin@gamil.com"

    return render(request, "sessionApp/index.html")


def get_session(request):
    usrnm = request.session.get("username")
    session = request.session
    print(session)
    key_values = session.items()
    print(session.keys())
    values = session.values()
    # for x in request.session:
    #     print(x)
    if "username" in request.session:
        print("yes")
    else:
        print("no")

    key = request.session.keys()
    session_age = request.session.get_session_cookie_age()

    session_age = time.localtime(session_age)


    # return HttpResponse([usrnm,key])
    return render(request, "sessionApp/index.html", context={"keys": key, "values": values, "kv": key_values, "sca": session_age})


# delete session
def logout(request):
    # del request.session["username"]
    # request.session.clear()
    # request.session.setdefault("username", "abc")

    request.session.flush()
    usrnm = request.session.get("username")
    return HttpResponse(usrnm)

