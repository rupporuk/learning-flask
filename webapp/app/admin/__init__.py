from flask import Blueprint
from flask import Flask, render_template

admin = Blueprint('admin', __name__)

from . import views