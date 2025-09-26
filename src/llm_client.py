# llm_client.py
from langchain_openai import ChatOpenAI

def get_llm(
    model: str = "qwen-omni-3b",
    api_key: str = "xxx",
    base_url: str = "http://127.0.0.1:6006/v1"
) -> ChatOpenAI:
    """
    初始化并返回大模型客户端实例
    
    参数:
        model: 模型名称
        api_key: 访问模型的密钥
        base_url: 模型服务的基础URL
    
    返回:
        配置好的ChatOpenAI实例
    """
    try:
        llm = ChatOpenAI(
            model=model,
            api_key=api_key,
            base_url=base_url,
        )
        print(f"成功连接大模型: {model}")
        return llm
    except Exception as e:
        print(f"大模型连接失败: {str(e)}")
        raise  # 抛出异常，让调用方处理

if __name__ == "__main__":
    llm = get_llm()
    print(llm.invoke("你好"))