from pydantic import BaseSettings
from huggingface_hub import configure_http_backend

class Settings(BaseSettings):
    EMBEDDING_MODEL: str = "sentence-transformers/all-mpnet-base-v2"  
    LLM_REPO_ID: str = "HuggingFaceH4/zephyr-7b-beta"               
    HUGGINGFACEHUB_API_TOKEN: str
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200
    DOCUMENTS_DIR: str = "data/documents"
    
    class Config:
        env_file = ".env"

settings = Settings()
configure_http_backend(cache_dir=".cache/hf")
