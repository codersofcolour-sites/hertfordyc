from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
    
    
class HomePage(Page):
    background_image =  models.ForeignKey(
        'wagtailimages.Image',
        related_name="background_image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        ImageChooserPanel('background_image'),
        FieldPanel('body', classname="full"),
    ]
