@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Events API"
    })

@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events])