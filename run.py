import os
from app import create_app

app = create_app(config_name=os.getenv("FLASK_ENV", "default"))

if __name__ == "__main__":
    app.run()
