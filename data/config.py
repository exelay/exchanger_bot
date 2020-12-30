import os
from dotenv import load_dotenv

load_dotenv()

# Environment variables
TOKEN: str = str(os.getenv("TOKEN"))
