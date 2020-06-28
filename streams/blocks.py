from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class CardBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
               ('image', ImageChooserBlock(required=True)),
               ('title', blocks.CharBlock(required=True, max_length=40)),
               ('text', blocks.TextBlock(required=True, max_length=200)),
               ('button_page', blocks.PageChooserBlock(required=False)),
               ('button_url', blocks.URLBlock(required=False, help_text="use if you want to go to external links")),
               ('button_title', blocks.CharBlock(required=False, max_length=40, help_text="Give your button a title")),
            ]
        )
    )

    class Meta: # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Cards"