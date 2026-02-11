from flask import Flask

app = Flask(__name__)

@app.route("/")

def main():
    print("Hello from backend!")
    return "Hello from backend!"


if __name__ == "__main__":
    main()
