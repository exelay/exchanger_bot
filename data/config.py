import os
from typing import List
from dotenv import load_dotenv

load_dotenv()

# Environment variables
TOKEN: str = str(os.getenv("TOKEN"))
PG_USER = str(os.getenv("PG_USER"))
PG_PASSWORD = str(os.getenv("PG_PASSWORD"))
DATABASE = str(os.getenv("DATABASE"))
DB_HOST = str(os.getenv("DB_HOST"))

ip = os.getenv('ip')

# List of allowed users
ALLOWED_USERS: List[int] = [
    305516197,
]

ADMINS: List[int] = [
    305516197,
]

POSTGRES_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{DB_HOST}/{DATABASE}"
