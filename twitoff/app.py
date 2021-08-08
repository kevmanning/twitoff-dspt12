# pylint: disable=missing-function-docstring
"""Main app/routing file for Twitoff"""

from flask import Flask, render_template


def create_app():
    """Creating and configuring an instance of the Flask application"""
    app = Flask(__name__)
    
    @app.route('/')
    def root():
        return render_template('base.html', title='home')

    
    return app