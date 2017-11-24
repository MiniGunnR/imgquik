from __future__ import unicode_literals

import hashlib

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import etag

from .forms import ImageForm


def generate_etag(request, width, height, bg=None, fg=None):
    content = 'Placeholder: {0} x {1} BG: {2} FG: {3}'.format(width, height, bg, fg)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()


@etag(generate_etag)
def placeholder(request, width, height, bg='FFFFFF', fg='000000'):
    form = ImageForm({'width': width, 'height': height})
    if form.is_valid():
        image = form.generate(bg='#{}'.format(bg), fg='#{}'.format(fg))
        return HttpResponse(image, content_type='image/png')
    else:
        return  HttpResponseBadRequest('Invalid Image Request')


def index(request):
    example = reverse('placeholder:placeholder', kwargs={'width': 100, 'height': 50})
    context = {
        'example': request.build_absolute_uri(example)
    }
    return render(request, 'placeholder/home.html', context)


def placeholder_shortcut(request, width):
    return redirect(reverse('placeholder:placeholder', args=[width, width]))
