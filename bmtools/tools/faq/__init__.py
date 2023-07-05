from ..registry import register

@register("faq")
def faq():
    from .api import build_tool
    return build_tool
