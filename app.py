from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

polls = {
    'poll_1': {
        'question': 'What is your favorite programming language?',
        'options': ['Python', 'JavaScript', 'Java', 'C++'],
        'votes': [0, 0, 0, 0]
    }
}

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/polls/<poll_id>', methods=['GET'])
def get_poll(poll_id):
    poll = polls.get(poll_id)
    if poll:
        return jsonify(poll)
    return jsonify({'error': 'Poll not found'}), 404

@app.route('/polls/<poll_id>/vote', methods=['POST'])
def vote(poll_id):
    poll = polls.get(poll_id)
    if not poll:
        return jsonify({'error': 'Poll not found'}), 404

    option = request.json.get('option')
    if option not in poll['options']:
        return jsonify({'error': 'Invalid option'}), 400

    index = poll['options'].index(option)
    poll['votes'][index] += 1
    return jsonify(poll)

if __name__ == '__main__':
    app.run(debug=True)
