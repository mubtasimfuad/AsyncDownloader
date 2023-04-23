from django.shortcuts import render, redirect
from .models import File, Download
import aiohttp
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from asgiref.sync import sync_to_async
from django.db import IntegrityError
from django.utils import timezone
from django.http import JsonResponse
@login_required

def file_list(request):
    files = File.objects.all()
    context = {'files': files}
    return render(request, 'file_downloader/file_list.html', context)

# Create your views here.


async def download_file(request, pk):
    file_obj = await sync_to_async(File.objects.get)(pk=pk)
    url = file_obj.url
    download = await sync_to_async(Download.objects.create)(
        file=file_obj, user=request.user, status="in progress"
    )
    try:
        await sync_to_async(download.save)()
    except IntegrityError:
        await sync_to_async(Download.objects.filter(file=file_obj).update)(
            downloaded_at=timezone.now()
        )
        
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            if res.status == 200:
                content = await res.read()
                response = HttpResponse(content, content_type=res.headers['Content-Type'])
                response['Content-Disposition'] = f'attachment; filename="{file_obj.name}"'

                download.status = "Successful"
                download.downloaded_at = timezone.now()
                await sync_to_async(download.save)()

                return response
            else:
                download.status = "Failed"
                download.downloaded_at = timezone.now()
                await sync_to_async(download.save)()

                return HttpResponse('Failed to download file')


@login_required
def download_list(request):
    downloads = Download.objects.filter(user=request.user).order_by('-downloaded_at')
    return render(request, 'file_downloader/download_list.html', {'downloads': downloads.exclude(status='Successful')})


def download_status(request, pk):
    download = Download.objects.get(pk=pk)
    return JsonResponse({'status': download.status})


