from django.shortcuts import render


# Create your views here.
def set_session(request):
    request.session["username"] = "abhi01"
    request.session["name"] = "Shristi"
    request.session["email"] = "hello@gmail.com"
    request.session["rollno"] = "101"
    request.session["cmtid"] = 1111
    return render(request, template_name="set-session.html")


def get_session(request):
    # uname = request.session["username"]
    # name = request.session["name"]
    uname = request.session.get("username")
    email = request.session.get("email")
    name = request.session.get("name")
    rollno = request.session.get("rollno")
    commit_id = request.session.get("cmtid", "0000")
    print(commit_id)
    # if rollno == None:
    #     print("name has no value")

    # if "rollno" in request.session:
    #     print("yes it has")

    # print(request.session)
    for key in request.session.keys():
        # print(key)
        # print(request.session.get(key))
        print(f"{key}: {request.session.get(key)}")

    return render(request, template_name="get-session.html", context={"username": uname, "name": name, "email": email})



def del_session(request):
    # del request.session["sdlkfklsd"]

    if "cmtid" in request.session:
        del request.session["cmtid"]
        res = "deleted"
    else:
        res = "key not found or this session not exists"

    return render(request, template_name="del-session.html", context={"result": res})