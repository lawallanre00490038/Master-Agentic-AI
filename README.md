Try pip with Tsinghua mirror first (most effective for SSL/timeouts)
Why
If the download takes too long or gets interrupted, pip's SSL layer may throw this error due to packages like  bitsandbytes, and transformers
pip install -r requirements.txt --no-cache-dir --timeout 100 -i https://pypi.tuna.tsinghua.edu.cn/simple



export HUGGINGFACEHUB_API_TOKEN=
export LANGCHAIN_API_KEY="your_langsmith_api_key_here"

Windos
set LANGCHAIN_API_KEY="your_langsmith_api_key_here"
# Master-Agentic-AI
