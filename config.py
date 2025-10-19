from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Google OAuth JSONs (paste the raw JSON contents)
    NEST_CLIENT_SECRET_JSON: str = ""
    NEST_TOKEN_JSON: str = ""

    # Google Drive folder with your PDFs
    NEST_DRIVE_FOLDER_ID: str = ""

    # Performance knobs
    NEST_MAX_FILES: int = 50          # cap number of PDFs to index
    NEST_TTL_SECS: int = 1800         # re-index every 30 min by default

    model_config = SettingsConfigDict(env_file=".env", env_prefix="")

settings = Settings()
