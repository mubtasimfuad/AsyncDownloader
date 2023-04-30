from django.shortcuts import render, redirect
from .models import DownloadedFile
import aiohttp
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError,StreamingHttpResponse
from asgiref.sync import sync_to_async
from django.db import IntegrityError
from django.utils import timezone
from django.http import JsonResponse
from .forms import URLForm
import os
from urllib.parse import urlparse
from django.contrib import messages
from django.core.files.base import ContentFile
from django.conf import settings
import aiofiles
import aiohttp

@login_required

def file_list(request):
    files = DownloadedFile.objects.filter(user=request.user).order_by('-created_at')
    context = {'files': files}
    return render(request, 'file_downloader/file_list.html', context)

# Create your views here.


# 

async def download_local_file(request, pk):
    try:
        file = await sync_to_async(DownloadedFile.objects.get)(pk=pk)
    except DownloadedFile.DoesNotExist:
        return HttpResponseNotFound()

    file_path = file.content.path
    if os.path.exists(file_path):
        async with aiofiles.open(file_path, mode='rb') as f:
            contents = await f.read()
            response = HttpResponse(contents, content_type='application/force-download')
            response['Content-Disposition'] = f'attachment; filename="{file.name}"'
            return response
    else:
        return HttpResponseNotFound()



def download_status(request, pk):
    download = DownloadedFile.objects.get(pk=pk)
    return JsonResponse({'status': download.status})





def url_download_page(request):
    return render(request, 'file_downloader/download_from_link.html')
 

async def download_file_remote(request):
    if request.method == "POST":
        url = request.POST.get('url')
        parsed_url = urlparse(url)
        file_name = os.path.basename(parsed_url.path)
        file_path = os.path.join(settings.MEDIA_ROOT, 'files', file_name)
        user_id = await sync_to_async(lambda: request.user)()
        
        if os.path.exists(file_path):
            name, ext = os.path.splitext(file_name)
            count = 1
            while os.path.exists(file_path):
                file_name = f"{name}_{count}{ext}"
                file_path = os.path.join(settings.MEDIA_ROOT, 'files', file_name)
                count += 1
        file_obj = await sync_to_async(DownloadedFile.objects.create)(
                        user=user_id,
                        name=file_name,
                        content=f"files/{file_name}",
                    )
        
        async with aiohttp.ClientSession(trust_env=True) as session:
            async with session.get(url) as res:
                if res.status == 200:
                    content = await res.read()
                    file_path = os.path.join(settings.MEDIA_ROOT, 'files', file_name)
                    with open(file_path, 'wb') as f:
                        f.write(content)
                    file_obj.status = "Downloaded"
                    await sync_to_async(file_obj.save)()
                    return HttpResponse('downloaded file')

                else:
                    file_obj.status = "Failed"
                    await sync_to_async(file_obj.save)()

                    return JsonResponse({'error': 'Failed to download file'})
                    
    return JsonResponse(status=204)





# async def download_file(request, pk):
#     file_obj = await sync_to_async(DownloadedFile.objects.get)(pk=pk)
#     url = file_obj.content 
#     file_path = settings.MEDIA_ROOT+str(url)

#     # download = await sync_to_async(Download.objects.create)(
#     #     file=file_obj, user=request.user, status="in progress"
#     # )
#     # try:
#     #     await sync_to_async(download.save)()
#     # except IntegrityError:
#     #     await sync_to_async(Download.objects.filter(file=file_obj).update)(
#     #         downloaded_at=timezone.now()
#     #     )

#     async with aiohttp.ClientSession(trust_env = True) as session:
#         async with session.get(file_path) as res:

#             if res.status == 200:
#                 content = await res.read()
#                 response = HttpResponse(content, content_type=res.headers['Content-Type'])
#                 response['Content-Disposition'] = f'attachment; filename="{file_obj.name}"'

#                 # download.status = "Successful"
#                 # download.downloaded_at = timezone.now()
#                 # await sync_to_async(download.save)()

#                 return response
#             else:
#                 # download.status = "Failed"
#                 # download.downloaded_at = timezone.now()
#                 # await sync_to_async(download.save)()

#                 return HttpResponse('Failed to download file')
