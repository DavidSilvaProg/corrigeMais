from datetime import datetime
from flask import session, flash, render_template
from app.models.database import Database

class tarefaService:
    def __init__(self):
        self.db = Database()

    def cadastraTarefa(self):
        print("cadastrar")