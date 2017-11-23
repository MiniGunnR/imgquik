from django import forms

from io import BytesIO
from PIL import Image, ImageDraw
from django.core.cache import cache

class ImageForm(forms.Form):
    """Form to validate requested placeholder image."""

    width = forms.IntegerField(min_value=1, max_value=2000)
    height = forms.IntegerField(min_value=1, max_value=2000)

    def generate(self, image_format='PNG', bg='#FFFFFF', fg='#000000'):
        """Generate an image of the given type and return as raw bytes."""
        width = self.cleaned_data['width']
        height = self.cleaned_data['height']
        key = '{}.{}.{}.{}.{}'.format(width, height, image_format, bg, fg)
        content = cache.get(key)
        if content is None:
            image = Image.new('RGB', (width, height), bg)
            draw = ImageDraw.Draw(image)
            text = '{} x {}'.format(width, height)
            textwidth, textheight = draw.textsize(text)
            if textwidth < width and textheight < height:
                texttop = (height - textheight) // 2
                textleft = (width - textwidth) // 2
                draw.text((textleft, texttop), text, fill=fg)
            content = BytesIO()
            image.save(content, image_format)
            content.seek(0)
            cache.set(key, content, 60 * 60)
        return content
