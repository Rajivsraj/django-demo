from django.shortcuts import render, HttpResponse
from datetime import datetime, date, time

# Create your views here.
def set_session(request):
    request.session["username"] = "admin"
    request.session["password"] = "admin@123"
    request.session["email"] = "admin@gamil.com"
    # request.session.set_expiry(120)

    request.session.set_test_cookie()
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
    session_age = datetime.fromtimestamp(session_age).strftime("%A %B %d %Y")
    # session_age = datetime.fromtimestamp(session_age)

    session_exp_age = request.session.get_expiry_age()
    sess_exp_date = request.session.get_expiry_date()
    on_browser_close = request.session.get_expire_at_browser_close()
    isCookieworking = request.session.test_cookie_worked()

    # return HttpResponse([usrnm,key])
    return render(request, "sessionApp/index.html", context={"isCookieworking": isCookieworking, "exp_browser": on_browser_close, "keys": key, "values": values, "kv": key_values, "sca": session_age, "exp_age": session_exp_age, "exp_date": sess_exp_date})


# delete session
def logout(request):
    # del request.session["username"]
    # request.session.clear()
    # request.session.setdefault("username", "abc")

    request.session.flush()
    request.session.clear_expired()
    usrnm = request.session.get("username")
    return HttpResponse(usrnm)

