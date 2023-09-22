def testing_middleware(get_response):
    print("This will run one time in there whole life")
    def inner_fun(request):
        print("before view call on every request")
        res = get_response(request)
        print("Will execute after view call")
        return res
    return inner_fun

