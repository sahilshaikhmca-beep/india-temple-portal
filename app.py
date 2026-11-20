from flask import Flask, render_template, request, abort, jsonify
from data import TEMPLES, PILGRIMAGES

app = Flask(__name__)


def filter_temples(query="", state=""):
    results = TEMPLES
    if query:
        q = query.lower()
        results = [
            t for t in results
            if q in t["name"].lower()
            or q in t["city"].lower()
            or q in t["deity"].lower()
            or q in t["category"].lower()
        ]
    if state:
        results = [t for t in results if t["state"] == state]
    return results


@app.route("/")
def index():
    query = request.args.get("q", "").strip()
    state = request.args.get("state", "").strip()
    states = sorted({t["state"] for t in TEMPLES})
    return render_template(
        "index.html",
        temples=filter_temples(query, state),
        states=states,
        query=query,
        selected_state=state,
    )


@app.route("/temple/<slug>")
def temple_detail(slug):
    temple = next((t for t in TEMPLES if t["slug"] == slug), None)
    if temple is None:
        abort(404)
    return render_template("temple.html", temple=temple)


@app.route("/pilgrimages")
def pilgrimages():
    return render_template("pilgrimages.html", circuits=PILGRIMAGES)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/api/temples")
def api_temples():
    return jsonify(filter_temples(
        request.args.get("q", "").strip(),
        request.args.get("state", "").strip(),
    ))


@app.errorhandler(404)
def not_found(_):
    return render_template("base.html", content="Page not found."), 404


if __name__ == "__main__":
    app.run(debug=True)