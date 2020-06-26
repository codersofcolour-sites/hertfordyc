from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context"""
        context = super().get_context(request, *args, **kwargs)
        live_blogpages = self.get_children().live()
        context['blogpages'] = BlogPage.objects.live().public()
        return context
    

class BlogPage(Page):
    author = models.CharField(max_length=100, default="")
    date = models.DateField("Post date")
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL
    )
    subtitle = models.CharField(max_length=150, blank=True, default="")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        ImageChooserPanel('image'),
        FieldPanel('subtitle'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]
