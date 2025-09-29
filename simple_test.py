import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from langchain_demo.prompt_factory import (
        StringConfig,
        create_string_prompt,
        create_chat_prompt,
        create_partial_variables_prompt
    )
    print("成功导入模块")
except Exception as e:
    print(f"导入模块失败: {e}")
    exit(1)

# 测试字符串模板
string_config = StringConfig(
    template="将{name}翻译成{target_language}",
    input_variables=["name"],
    partial_variables={"target_language": "英文"}
)
string_prompt = create_string_prompt(string_config)
result = string_prompt.format(name="你好")
print("字符串模板结果:", result)

# 测试聊天模板
chat_prompt = create_chat_prompt(string_config)
messages = chat_prompt.format_messages(input_text="你好，世界！")
print("聊天模板结果:", messages)

# 测试部分变量模板
partial_prompt = create_partial_variables_prompt()
# 使用字典解包传递参数
result = partial_prompt.format(**{
    "source_language": "中文",
    "target_language": "英文",
    "input_text": "今天天气怎么样？"
})
print("部分变量模板结果:", result)