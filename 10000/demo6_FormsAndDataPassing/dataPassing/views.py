from django.shortcuts import render


# Create your views here.
def home(request):
    stu_details = {
        "name": "rahul",
        "age": 20,
        "city": "Delhi",
        "course": "Django"
    }

    lst = [34,4,5,6,5,6,4,43,4]

    stu_rec = [{
        "rollno": [1, 2, 3, 4, 5],
        "name": ["Rahul", "sumit", "amit", "ajay", "vijay"],
        "age": [23, 65, 34, 54, 34]
    }]

    print(stu_rec[0]["rollno"])
    return render(request, "home.html", {"names": stu_details, "marks": lst, "stu_dtails": stu_rec})

