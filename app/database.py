import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# ==============================
# ENV VARIABLES
# ==============================

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
DB_NAME = os.getenv("MYSQL_DB", "inventory_db")

# ==============================
# VALIDATION (IMPORTANT)
# ==============================

if not MYSQL_USER or not MYSQL_PASSWORD:
    raise ValueError("Database credentials are not set in environment variables")

# ==============================
# CONNECTION STRINGS
# ==============================

BASE_DB_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}"
FULL_DB_URL = f"{BASE_DB_URL}/{DB_NAME}"

# ==============================
# CREATE DATABASE (SAFE INIT)
# ==============================

server_engine = create_engine(BASE_DB_URL)

with server_engine.begin() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))

# ==============================
# MAIN ENGINE
# ==============================

engine = create_engine(
    FULL_DB_URL,
    pool_pre_ping=True,
    pool_recycle=3600
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
