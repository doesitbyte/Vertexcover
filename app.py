from api import init_app
import os

app = init_app()

if __name__ == "__main__":
    try:
        app.run()

    except Exception as e:
        print("INITIALIZING SERVER FAILED: ", e)