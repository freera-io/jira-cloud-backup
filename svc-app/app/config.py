import os
from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    version: str = os.getenv("APP_VERSION")
    env: str = os.getenv("APP_ENV")
    app_hostname: str = os.environ.get("APP_HOSTNAME")
    jira_server_url: str = os.environ.get("JIRA_SERVER_URL")  # "https://YOUR_JIRA_SERVER_URL.atlassian.net"
    jira_login: str = os.environ.get("JIRA_LOGIN")  # "YOUR_EMAIL_AS_JIRA_LOGIN@gmail.com"
    jira_api_token: str = os.environ.get("JIRA_API_TOKEN")  # see: [https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/]
    mongo_dsn: str = os.environ.get("MONGO_DSN")

@lru_cache()
def get_settings() -> Settings:  # BaseSettings:
    cfg = Settings()
    return cfg
