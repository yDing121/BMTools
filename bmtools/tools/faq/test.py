from bmtools.agent.singletool import load_single_tools, STQuestionAnswerer

tool_name, tool_url = 'faq',  "http://127.0.0.1:8079/tools/faq/"
tools_name, tools_config = load_single_tools(tool_name, tool_url)
print(tools_name, tools_config)

qa = STQuestionAnswerer()

agent = qa.load_tools(tools_name, tools_config)

agent("What is the answer to question A?")