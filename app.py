@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Events API"
    })

@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events])

@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    new_id = max([event.id for event in events], default=0) + 1

    new_event = Event(
        new_id,
        data["title"]
    )

    events.append(new_event)

    return jsonify(new_event.to_dict()), 201

@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    event = find_event(event_id)

    if not event:
        return jsonify({"error": "Event not found"}), 404

    data = request.get_json()

    if "title" in data:
        event.title = data["title"]

    return jsonify(event.to_dict())

@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = find_event(event_id)

    if not event:
        return jsonify({"error": "Event not found"}), 404

    events.remove(event)

    return "", 204