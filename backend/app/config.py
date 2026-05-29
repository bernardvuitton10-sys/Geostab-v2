from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    api_port: int = 8000
    database_url: str = "postgresql://geostab:geostab123@localhost:5432/geostab"
    secret_key: str = "your-super-secret-key-change-this"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    max_upload_mb: int = 15
    storage_path: str = "/app/uploads"
    reports_path: str = "/app/reports"
    allowed_extensions: str = "jpg,jpeg,png"
    yolo_model_path: str = "/app/models/yolo/yolov8n.pt"
    redis_url: str = "redis://localhost:6379"
    environment: str = "development"
    log_level: str = "INFO"
    
    @property
    def allowed_extensions_list(self) -> List[str]:
        return [ext.strip() for ext in self.allowed_extensions.split(",")]
    
    @property
    def max_upload_bytes(self) -> int:
        return self.max_upload_mb * 1024 * 1024
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
