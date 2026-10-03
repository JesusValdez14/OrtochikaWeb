"""Extensiones instanciadas aquí para evitar importaciones circulares."""
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

login_manager.login_view = "main.index"  # cambiar a "auth.login" en el Sprint 3
login_manager.login_message = "Inicia sesión para continuar."
