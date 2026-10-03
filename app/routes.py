"""Rutas iniciales. Aquí se agregarán blueprints por módulo (auth, catálogo, cotizaciones, paneles)."""
from flask import Blueprint, current_app, jsonify, render_template
from sqlalchemy import text

from .extensions import db

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/health/db")
def health_db():
    """Verifica la conexión con MySQL: abre http://127.0.0.1:5000/health/db"""
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify(status="ok")
    except Exception:
        current_app.logger.exception("Fallo la conexión a la base de datos")
        return jsonify(status="error"), 500
