import os
from typing import Final
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Define a function to get environment variables
def _getenv(v: str) -> str:
    env = os.getenv(v)
    assert env is not None, f"Environment variable {v} is not set"
    return env


# Access the variables
BOT_TOKEN: Final = _getenv("BOT_TOKEN")
BOT_NAME: Final = _getenv("BOT_NAME")
BOT_USERNAME: Final = _getenv("BOT_USERNAME")
