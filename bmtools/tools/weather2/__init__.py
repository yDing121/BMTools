
from ..registry import register

@register("weather2")
def weather2():
    from .api import build_tool
    return build_tool
