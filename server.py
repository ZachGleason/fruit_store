from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    print(f"Charging {{Customer name}} for {{count}} fruits")
    return render_template("checkout.html")

if __name__ == "__main__":
    app.run(debug=True)