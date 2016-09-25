from pictureswap.website.views import error


def handler404(request):
    return error(request, "404: Page not found")


def handler500(request):
    return error(request, "500: Internal error")
