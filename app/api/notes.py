from app.api import bp
from app.api.errors import bad_request
from flask import jsonify, request, url_for

id_notes = 0
notes = dict()


@bp.route('/notes', methods=['GET'])
def get_notes():
    responce = list()
    for item in notes.items():
        responce.append(item)
    return jsonify(responce)


@bp.route('/notes', methods=['POST'])
def add_notes():
    data = request.get_json() or {}
    if 'title' not in data or 'connent' not in data:
        return bad_request(" ")
    else:
        responce = {"id": id_notes+1, "title": data["title"], "content": data["content"]}
        return jsonify(responce)


@bp.route('/notes/<int:n_id>', methods=['GET'])
def get_note(n_id):
    if n_id in notes:
        responce = {"id": n_id, "title": notes["title"], "content": notes["content"]}
        notes.update(responce)
        return jsonify(responce)


@bp.route('/notes/<int:n_id>', methods=['PUT'])
def edit_note(n_id):
    pass


@bp.route('/notes/<int:n_id>', methods=['DELETE'])
def delete_note(n_id):
    notes.pop(n_id)


@bp.route('/notes', methods=['GET'])
def search_note():
    text_search = str(request.args['query'])
