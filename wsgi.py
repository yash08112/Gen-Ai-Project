"""
WSGI entry point for deployment
"""
import sys
import os

# Add the project root and backend to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
backend_path = os.path.join(project_root, 'backend')
sys.path.insert(0, project_root)
sys.path.insert(0, backend_path)

# Import the Flask app
from backend.app import app

# This is what Gunicorn will use
application = app

if __name__ == "__main__":
    app.run()

