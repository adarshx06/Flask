from flask import Flask, render_template, request, redirect, url_for, flash
app= Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Flask App!'

if __name__ == '__main__':
    app.run()
