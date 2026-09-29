from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your-secret-key"

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        participant_name = request.form["participant_name"]
        mobile_number = request.form["mobile_number"]
        event_name = request.form["event_name"]

        flash(
            f"Registration successful! "
            f"Participant: {participant_name}, "
            f"Mobile: {mobile_number}, "
            f"Event: {event_name}",
            "success"
        )

        return redirect(url_for("register"))

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
