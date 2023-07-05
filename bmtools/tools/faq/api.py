from ..tool import Tool


def build_tool(config) -> Tool:
    tool = Tool(
        tool_name="FAQ Info",
        description="Plugin for retrieving FAQ information",
        name_for_model="FAQ",
        description_for_model="Plugin for retrieving FAQ information. Make sure to pass the actual question to the API, for example if the user asks \"What is the answer to question X?\", pass \"question x\" to the API",
        logo_url="",
        contact_email="hello@contact.com",
        legal_info_url="hello@legal.com"
    )

    @tool.get("/get_answer")
    def get_answer(question: str):
        ansdict = {
            "question a": "Apples are sweet",
            "question b": "Bee stings hurt",
            "question c": "Clip-in stabilizers are bad",
            "问题a": "苹果很甜",
            "问题b": "被蜜蜂蛰会很痛",
            "问题c": "钢板卫星轴不太好"
                 }
        return f"{question}的答案: " + ansdict.get(question.lower(), "Python是一个高级编程语言")
    return tool
