from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

users = [
    {
        "name": "James",
        "age": 25,
        "city": "New York",
        "photo": "https://img.freepik.com/free-photo/young-bearded-man-with-round-glasses-and-denim-shirt_273609-12127.jpg?size=626&ext=jpg&ga=GA1.1.2125429974.1702055257&semt=ais"
    },
    {
        "name": "Anna",
        "age": 30,
        "city": "London",
        "photo": "https://img.freepik.com/free-photo/horizontal-portrait-of-smiling-happy-young-pleasant-looking-female-wears-denim-shirt-and-stylish-glasses-with-straight-blonde-hair-expresses-positiveness-poses_176420-13176.jpg?size=626&ext=jpg&ga=GA1.1.2125429974.1702055257&semt=ais"
    },
    {
        "name": "David",
        "age": 32,
        "city": "Los Angeles",
        "photo": "https://img.freepik.com/free-photo/handsome-young-cheerful-man-with-arms-crossed_171337-1073.jpg?size=626&ext=jpg&ga=GA1.1.2125429974.1702055257&semt=ais"
    },
    {
        "name": "Emma",
        "age": 27,
        "city": "Seoul",
        "photo": "size=626&ext=jpg&ga=GA1.1.2125429974.1702055257&semt=ais"
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def search():
    search_term = request.json.get('search')
    results = [user for user in users if search_term.lower()
               in user['name'].lower()]
    return jsonify(results)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)



