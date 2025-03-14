from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data_store), 200

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    if not item:
        return jsonify({"error": "Invalid input"}), 400
    data_store.append(item)
    return jsonify(item), 201

@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    if index < 0 or index >= len(data_store):
        return jsonify({"error": "Item not found"}), 404
    updated_item = request.json
    if not updated_item:
        return jsonify({"error": "Invalid input"}), 400
    data_store[index] = updated_item
    return jsonify(updated_item), 200

@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    if index < 0 or index >= len(data_store):
        return jsonify({"error": "Item not found"}), 404
    deleted_item = data_store.pop(index)
    return jsonify(deleted_item), 200

if __name__ == '__main__':
    app.run(debug=True)
