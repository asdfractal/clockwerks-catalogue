import os
from app import APP

if __name__ == "__main__":
    APP.run(host=os.getenv("IP"), port=os.getenv("PORT"), debug=os.getenv("DEBUG"))
