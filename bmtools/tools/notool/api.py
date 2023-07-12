import requests
import json
from ..tool import Tool
import os


def build_tool(config) -> Tool:
    tool = Tool(
        "Placeholder for no tool",
        "Return a final answer",
        name_for_model="Default tool",
        description_for_model="Tool for when you don't need to use a tool",
        logo_url="",
        contact_email="hello@contact.com",
        legal_info_url="hello@legal.com"
    )

        
    @tool.get("/final_answer")
    def final_answer():
        return ""

    return tool
