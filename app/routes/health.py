import time
from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)
_START = time.time()


@health_bp.route('/health')
def health():
    return jsonify(status='ok', uptime_seconds=round(time.time() - _START))


@health_bp.route('/diag')
def diag():
    return jsonify(status='ok', service='disaster_flask_app', version='2.0.0')
