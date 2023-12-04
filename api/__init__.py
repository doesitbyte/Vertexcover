from flask import Flask
from flask_cors import CORS
from datetime import datetime
import time

def init_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/status", methods=["GET"])
    def checkServerStatus():
        startTime = time.time()
        return {
            "code": 200,
            "status": "online",
            "ping": time.time() - startTime,
            "serverDateTime": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        }

    with app.app_context():
        from .coupon import couponAPI

        app.register_blueprint(couponAPI.couponBlueprint, url_prefix="/coupon")

    return app