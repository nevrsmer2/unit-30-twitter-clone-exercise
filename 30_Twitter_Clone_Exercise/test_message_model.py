'''Message Model Tests'''

import os
from unittest import TestCase

from app import app
from models import Follows, Message, User, db

os.environ['DATABASE_URL'] = "postgresql://warbler-test"
db.create_all()
