from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from streams.blocks import CardBlock
from wagtail.images.blocks import ImageChooserBlock


# Create your models here.

class FlexPage(Page):

    body = StreamField([
        ('heading', blocks.CharBlock(icon="title", null=True, blank=True)),
        ('image', ImageChooserBlock(required=False)),
        ('paragraph', blocks.RichTextBlock(icon="pilcrow", features=['h3', 'h4', 'centre', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'embed'],  null=True, blank=True)),
        ('embed', EmbedBlock(icon="media", null=True, blank=True)),
        ('embed_HTML', blocks.RawHTMLBlock(required=False, help_text="use this to embed elements that do not embed using the normal embed block, e.g. google forms", null=True, blank=True)),
        ('cards', CardBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
    ]
