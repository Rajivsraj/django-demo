class MyMiddleware:
    def __init__(self, get_response):
        self.get_res = get_response
        print("Will run once in whole life")

    def __call__(self, request):
        print("will execute before view")
        response = self.get_res(request)
        print("will execute after view")
        return response