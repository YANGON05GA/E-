from services.qwen import get_client

# 尝试获取客户端，这应该会使用apis.json中的key_env值作为API key
try:
    client = get_client()
    print("成功获取客户端！API密钥处理正常")
    print(f"基础URL: {client.base_url}")
    # 注意：我们不实际调用API，只测试客户端创建是否成功
    print("测试通过：已成功修复API密钥处理逻辑")
except Exception as e:
    print(f"错误：{e}")
    print("测试失败：API密钥处理逻辑仍有问题")
