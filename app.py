from api import init_app
from waitress import serve
import os

app = init_app()

host = "0.0.0.0"
port = int(os.environ.get("PORT", 5000))
debug = False

if __name__ == "__main__":
    try:
        print("Starting Server...")
        print("PORT: ", port)
        print("DEBUG: ", debug)

        serve(
            app,
            host=host,
            port=port,
        )

    except Exception as e:
        print("INITIALIZING SERVER FAILED: ", e)