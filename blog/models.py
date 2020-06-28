from django.db import models

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class BlogIndexPage(Page):
    max_count = 1
    subpage_types =['blog.BlogPage',
    'flex.FlexPage',]

    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context"""
        context = super().get_context(request, *args, **kwargs)
        live_blogpages = self.get_children().live()
        all_posts = BlogPage.objects.live().public().order_by('-first_published_at')

        paginator = Paginator(all_posts, 2)

        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context["blogpages"] = posts

        return context
    

class BlogPage(Page):
    subpage_types = []
    author = models.CharField(max_length=100, default="")
    date = models.DateField("Post date")
    preview_image = models.ForeignKey(
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
        ImageChooserPanel('preview_image'),
        FieldPanel('subtitle'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]
