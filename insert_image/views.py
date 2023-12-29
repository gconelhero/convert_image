from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

from PIL import Image as PILImage
import filetype

from .forms import ImageForm
from .models import Image


def index(request):
    return render(request, 'index.html')

def convert_image(image):
    # Convert JPEG to PNG
    img = PILImage.open(image)
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    return InMemoryUploadedFile(buffer, None, f'{image.name.split(".")[0]}.png', 'image/png', buffer.tell(), None)

def upload_image(request):
    message = ''
    if request.method == 'POST' and request.FILES:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image_file']
            file_type = filetype.guess(image)
            if file_type.MIME == 'image/jpeg':
                form.instance.image_file = convert_image(image)
                form.save()
                session_images = request.session.get('uploaded_images', [])
                session_images.append(form.instance.id)
                request.session['uploaded_images'] = session_images
        
                return HttpResponseRedirect(reverse('uploaded_images'))
            else:
                message = 'Error file type!'
    else:
        form = ImageForm()
        return render(request, 'upload_image.html', {'form': form,
                                                             'message': message
                                                             })
    return render(request, 'upload_image.html', {'form': form,
                                                             'message': message
                                                             })
def uploaded_images(request):
    # Retrieve uploaded image IDs from session
    session_images = request.session.get('uploaded_images', [])

    images = Image.objects.filter(id__in=session_images)
    return render(request, 'uploaded_images.html', {'images': images})

