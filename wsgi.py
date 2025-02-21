#for debug purpose
import os
import sys

print(f"WSGI: DATABASE_URL = {os.environ.get('DATABASE_URL')}", file=sys.stderr)

#--main code
from src import app

