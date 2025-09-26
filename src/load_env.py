import os
from dotenv import load_dotenv

def load_and_check_env():
    """加载并检查环境变量"""

    # 加载.env文件中的环境变量
    load_dotenv()
    # 获取所有环境变量
    env_json = {key: os.getenv(key) for key in os.environ.keys()}
    
    return env_json

# 调用函数
if __name__ == "__main__":
    env_json = load_and_check_env()
    print(env_json["OLLAMA_BASE_URL"])
