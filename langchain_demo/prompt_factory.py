# 这是一个用于创建各种提示模板的工厂类

from langchain.prompts import PromptTemplate, ChatPromptTemplate, StringPromptTemplate
from typing import List

class StringConfig:
    template: str
    input_variables: List[str]
    # 注意：这里将 variables 改名为 input_variables 并调整类型
    partial_variables: dict

    def __init__(self, template: str, input_variables: List[str], partial_variables: dict = None):
        self.template = template
        self.input_variables = input_variables
        self.partial_variables = partial_variables or {}

def create_string_prompt(config: StringConfig) -> StringPromptTemplate:
    """根据配置创建字符串提示模板"""
    return PromptTemplate(
        template=config.template,
        input_variables=config.input_variables,
        partial_variables=config.partial_variables
    )

def create_chat_prompt(config: StringConfig) -> ChatPromptTemplate:
    """根据配置创建聊天提示模板"""
    return ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个翻译助手，能够将{source_language}翻译成{target_language}"),
            ("user", "{input_text}")
        ],
        partial_variables={
            "source_language": "Chinese",
            "target_language": "English"
        }
    )

def create_partial_variables_prompt() -> StringPromptTemplate:
    """创建带部分变量的提示模板"""
    return PromptTemplate.from_template(
        "将以下{source_language}文本翻译成{target_language}: {input_text}"
    )
