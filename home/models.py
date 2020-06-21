from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
    
    
class HomePage(Page):
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body', classname="full"),
    ]
