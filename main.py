"""How much Wes Anderson?

Run it locally:
$ flask --app main --debug run

Access at http://localhost:5000/

TensorFlow was using 800MB of memory so I ported this to TensorFlow Lite 
to stay on the free tier of Fly.
"""
import os
from pathlib import Path
import secrets


from tflite_support.task import vision
from flask import (
    Flask,
    render_template,
    flash,
    request,
    redirect,
    url_for,
)
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg"}


app = Flask(__name__)
app.secret_key = secrets.token_hex()
app.config["UPLOAD_FOLDER"] = "static"


classifier = vision.ImageClassifier.create_from_file("model.tflite")


def allowed_file(filename):
    return Path(filename).suffix in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            return redirect(url_for("wes_probability", filename=filename))
    return render_template("index.html")


def predict(image_file):
    """Generate an image classification prediction

    Parameters
    ----------
    image_file : str
        Image file name

    Returns
    -------
    float
        Value from 0-1 representing the probability it is Wes
    """

    image = vision.TensorImage.create_from_file(image_file)
    classification_result = classifier.classify(image)
    return classification_result.classifications[0].categories[0].score


@app.route("/wes_probability/<filename>")
def wes_probability(filename):
    """Load image and render html result"""
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    score = round(100 * (predict(filepath)))
    result = f"This image is {score}% Wes Anderson"
    return render_template(
        "wes_result.html",
        image_link=filepath,
        result=result,
    )
