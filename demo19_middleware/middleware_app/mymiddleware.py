from django.http import HttpResponse
from django.shortcuts import render

# def testing_middleware(get_response):
#     print("This will run one time in there whole life")
#     def inner_fun(request):
#         print("before view call on every request")
#         res = get_response(request)
#         print("Will execute after view call")
#         return res
#     return inner_fun


# class ClassMiddleware():
#     def __init__(self, get_response):
#         print("One time execution only 1")
#         self.get_res = get_response
#
#     def __call__(self, request, *args, **kwargs):
#         print("Before view call 1")
#         res = self.get_res(request)
#         print("Run after view call 1", res)
#         return res
#
#
#
# class ClassMiddleware2():
#     def __init__(self, get_response):
#         print("One time execution only 2")
#         self.get_res = get_response
#
#     def __call__(self, request, *args, **kwargs):
#         print("Before view call 2")
#         res = self.get_res(request)
#         # return HttpResponse("Hello this is return by m2")
#         # return render(request, "template_url")
#         print("Run after view call 2", res)
#         return res
#
#
# class ClassMiddleware3():
#     def __init__(self, get_response):
#         print("One time execution only 3")
#         self.get_res = get_response
#         # print("one Time 3", self.get_res)
#
#     def __call__(self, request, *args, **kwargs):
#         print("Before view call 3", request.get_full_path())
#         res = self.get_res(request)
#         print("Run after view call 3", res)
#         return res



# class ClassMiddleware3():
#     def __init__(self, get_response):
#         print("One time execution only 3")
#         self.get_res = get_response
#
#     def __call__(self, request, *args, **kwargs):
#         print("Before view call 3", request.get_full_path())
#         if str(request.get_full_path()) == "/middle/":
#             print("Matched")
#             return HttpResponse("You are not allowed to access this page")
#         else:
#             # res = self.get_res(request)
#             return self.get_res(request)
#
#         # print("Run after view call 3", res)
#         # return res



class ClassMiddleware3():
    def __init__(self, get_response):
        print("One time execution only 3")
        self.get_res = get_response

    def __call__(self, request, *args, **kwargs):
        print("Before view call 3", request.get_full_path())
        # if str(request.get_full_path()) == "/middle/":
        #     print("Matched")
        #     return HttpResponse("You are not allowed to access this page")
        # else:
            # res = self.get_res(request)
        res = self.get_res(request)
        # print(stuid)
        print("Run after view call 3", res)
        return res
