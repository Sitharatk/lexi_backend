from pydantic import BaseSettings
import os

# Set Hugging Face cache directory
os.environ["HF_HOME"] = ".cache/hf"

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
