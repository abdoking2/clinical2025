import os
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# إرسال ملف index.html مباشرة
@app.route("/")
def home():
    return send_from_directory(os.getcwd(), "index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    symptoms = data.get("symptoms", "").lower()

    if "حمى" in symptoms and "سعال" in symptoms:
        diagnosis = "انفلونزا"
        recommendation = "الراحة + أدوية الانفلونزا"
    elif "صداع" in symptoms:
        diagnosis = "صداع نصفي"
        recommendation = "مسكنات + راحة"
    else:
        diagnosis = "غير معروف"
        recommendation = "استشر الطبيب"

    return jsonify({"diagnosis": diagnosis, "recommendation": recommendation})


if __name__ == "__main__":
    app.run(debug=True)
