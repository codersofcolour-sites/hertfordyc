from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock


# Create your models here.

class FlexPage(Page):
    template = "flex_page.html"

    subtitle = models.CharField(max_length=250, null=True, blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(icon="title", null=True, blank=True)),
        ('paragraph', blocks.RichTextBlock(icon="pilcrow", null=True, blank=True)),
        ('embed', EmbedBlock(icon="media", null=True, blank=True)),
    ], null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('body'),
        ImageChooserPanel('image'),
    ]
