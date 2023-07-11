from bmtools.agent.tools_controller import load_valid_tools, MTQuestionAnswerer
from my_utils.load_keys import load_key

load_key("openai")

tools_mappings = {
    'weather': "http://127.0.0.1:8079/tools/weather/",
    'file_operation': "http://127.0.0.1:8079/tools/file_operation/",
}

tools = load_valid_tools(tools_mappings)

qa = MTQuestionAnswerer(openai_api_key='', all_tools=tools)

agent = qa.build_runner()

agent("what is the weather in Beijing?")