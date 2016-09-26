import requests
from block_ip.models import BlockIP
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from ipware.ip import get_ip
from .forms import UploadPictureForm
from .models import Picture, Report, Laughing, Fearful, Banana

MAX_PICTURES = 36;
REPORT_BAN_THRESHOLD = 2;

def index(request):
    return render(request, 'website/index.html')


def __upload_picture(request):
    picture = Picture(image=request.FILES['picture'], title=request.POST['title'])
    picture.uploader_ip = get_ip(request)
    picture.save()
    if is_sensitive(picture):
        picture.delete()


def is_sensitive(picture):
    response = requests.get('https://api.github.com/user', headers={
            "X-Mashape-Key": "0sXHP6IbW2mshFHzVOJtQ6xVmwDcp1tRLhUjsn95qhByhS1dvb",
            "Accept": "application/json"
        })
    if 'sensitive' in response.json() and response.json()['sensitive']:
        return response.json()['sensitive']
    else:
        return False


def __delete_old_pictures():
    while Picture.objects.count() > MAX_PICTURES:
        oldest = Picture.objects.order_by('datetime').first()
        oldest.delete()


def __delete_reported_pictures():
    pictures = Picture.objects.all()
    for picture in pictures:
        if picture.report_count() >= REPORT_BAN_THRESHOLD:
            __delete_reported_picture(picture)


def __delete_reported_picture(picture):
    ban = BlockIP.objects.create(network=picture.uploader_ip, reason_for_block='Reported %d or more times' % REPORT_BAN_THRESHOLD)
    ban.save()
    picture.delete()


def upload(request):
    if request.method == 'POST':
        form = UploadPictureForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                last_picture_pk = Picture.objects.order_by('-datetime')[0].pk
                __upload_picture(request)
                __delete_old_pictures()
                return redirect('success', last_picture_pk=last_picture_pk)
            except:
                __upload_picture(request)
                last_picture_pk = Picture.objects.order_by('-datetime')[0].pk
                return redirect('success', last_picture_pk=last_picture_pk)

        else:
            return error(request, "Invalid image")
    else:
        return error(request, "You didn't post any picture")


def success(request, last_picture_pk):
    try:
        picture = Picture.objects.get(pk=last_picture_pk)
        context = {'picture': picture.image.url, 'title': picture.title }
        return render(request, 'website/success.html', context)
    except:
        return error(request, "That image does not exists")


def error(request, error='Something went wrong'):
    context = {'error': error}
    return render(request, 'website/error.html', context)


def rules(request):
    return render(request, 'website/rules.html')


def gallery(request):
    __delete_reported_pictures()
    context = {
        'pictures': Picture.objects.all().order_by('-datetime')
    }
    return render(request, 'website/gallery.html', context)


@require_POST
@csrf_exempt
def report(request):
    try:
        picture = Picture.objects.get(pk=request.POST['picture'])
        reporter_ip = get_ip(request)

        if Report.objects.filter(picture=picture, reporter_ip=reporter_ip).exists():
            return HttpResponse('already_reported')
        else:
            new_report = Report.objects.create(picture=picture, reporter_ip=reporter_ip)
            new_report.save()
            return HttpResponse('ok')
    except:
        return HttpResponse('error')


@require_POST
@csrf_exempt
def laughing(request):
    try:
        picture = Picture.objects.get(pk=request.POST['picture'])
        rater_ip = get_ip(request)

        if Laughing.objects.filter(picture=picture, rater_ip=rater_ip).exists():
            return HttpResponse('already_voted')
        else:
            new_rating = Laughing.objects.create(picture=picture, rater_ip=rater_ip)
            new_rating.save()
            return HttpResponse('ok')
    except:
        return HttpResponse('error')


@require_POST
@csrf_exempt
def fearful(request):
    try:
        picture = Picture.objects.get(pk=request.POST['picture'])
        rater_ip = get_ip(request)

        if Fearful.objects.filter(picture=picture, rater_ip=rater_ip).exists():
            return HttpResponse('already_voted')
        else:
            new_rating = Fearful.objects.create(picture=picture, rater_ip=rater_ip)
            new_rating.save()
            return HttpResponse('ok')
    except:
        return HttpResponse('error')


@require_POST
@csrf_exempt
def banana(request):
    try:
        picture = Picture.objects.get(pk=request.POST['picture'])
        rater_ip = get_ip(request)

        if Banana.objects.filter(picture=picture, rater_ip=rater_ip).exists():
            return HttpResponse('already_voted')
        else:
            new_rating = Banana.objects.create(picture=picture, rater_ip=rater_ip)
            new_rating.save()
            return HttpResponse('ok')
    except:
        return HttpResponse('error')
