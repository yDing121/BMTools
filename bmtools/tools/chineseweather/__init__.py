
from ..registry import register

@register("chineseweather")
def chineseweather():
    from .api import build_tool
    return build_tool
