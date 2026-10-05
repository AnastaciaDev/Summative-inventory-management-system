from flask import jsonify


def success_response(message, data=None):
    return jsonify({
        "message": message,
        "data": data
    }), 200


def created_response(message, data=None):
    return jsonify({
        "message": message,
        "data": data
    }), 201


def deleted_response(message):
    return jsonify({
        "message": message
    }), 200


def validation_error(message):
    return jsonify({
        "message": message
    }), 400


def not_found(message):
    return jsonify({
        "message": message
    }), 404


def server_error(message="Internal server error"):
    return jsonify({
        "message": message
    }), 500

