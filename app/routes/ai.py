import os
from flask import Blueprint, request, jsonify

ai_bp = Blueprint('ai', __name__)


@ai_bp.route('/ask', methods=['POST'])
def ask():
    """Natural language query endpoint. Requires ANTHROPIC_API_KEY env var."""
    data = request.get_json(silent=True) or {}
    question = data.get('question', '').strip()
    if not question:
        return jsonify(error='question field required'), 400
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        return jsonify(error='AI not configured', hint='Set ANTHROPIC_API_KEY'), 503
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model='claude-sonnet-4-6',
            max_tokens=1024,
            messages=[{'role': 'user', 'content': question}],
        )
        return jsonify(answer=message.content[0].text)
    except Exception as e:
        return jsonify(error='AI request failed', detail=str(e)), 500
