from flask import Flask, jsonify, request
from transformers import pipeline

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"about":"Hello World"})

summarizer = pipeline("summarization", model="lidiya/bart-large-xsum-samsum")


@app.route("/summary",methods = ["POST"])
def summary():

    sentence = request.form.get('summarytext')
    processed  = summarizer(sentence) 
    return jsonify({
            "summaryText": str(processed[0]["summary_text"])
    })

if __name__ == '__main__':
    app.run(debug=True, threaded=True)


