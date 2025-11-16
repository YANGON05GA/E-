import os


def load_env(env_path: str = ".env"):
    """No-op for backwards compatibility.

    Project now reads API credentials from `apis.json`. The previous behavior
    of loading a local `.env` or `.api_key` into environment is intentionally
    removed to centralize credential management in `apis.json`.
    """
    return


def get_settings():
    return {
        "DB_FILE": os.getenv("DB_FILE", "bills.db"),
        "DASHSCOPE_API_KEY": os.getenv("DASHSCOPE_API_KEY"),
        "UVICORN_HOST": os.getenv("UVICORN_HOST", "0.0.0.0"),
        "UVICORN_PORT": int(os.getenv("UVICORN_PORT", "8000")),
    }


def init_app():
    # 延迟导入以便环境变量已经加载
    try:
        from bills import db as bills_db
        bills_db.init_db()
    except Exception:
        # 忽略初始化错误，调用方可自行处理
        pass
