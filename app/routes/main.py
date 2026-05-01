from flask import Blueprint, render_template, request, escape
from datetime import datetime
import pytz

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
@main_bp.route('/index.html')
def hello_world():
    date = datetime.now(tz=pytz.utc).astimezone(pytz.timezone('US/Pacific'))
    message = f"Hello World! {date.strftime('%Y-%m-%d %H:%M:%S %Z')}"
    image_src = 'https://s3.amazonaws.com/kiran-test-2/cruiser80.jpg'
    return render_template('index.html', src_hello=message, image_name=image_src)


@main_bp.route('/surnames/')
def get_surname():
    query_val = request.args.get('Name', '')
    parts = query_val.split()
    surname = ' '.join(parts[1:]) if len(parts) > 1 else query_val
    return f'<p>Name Is: {escape(surname)}</p>'
