from app import db
from datetime import datetime
from sqlalchemy.sql.expression import text
from sqlalchemy.exc import SQLAlchemyError
import os




class People(db.Model):
      id            = db.Column(db.Integer, primary_key=True)
      email         = db.Column(db.String(100), index=True)
      senha         = db.Column(db.String(255), index=True)          
      date_created  = db.Column(db.DateTime)
      date_modified = db.Column(db.DateTime)
      tasks         = db.relationship('Task', backref='people', lazy=True)

      def __repr__(self):
          return '<People %r>' %(self.email)


      def __init__(self,email, senha):
          self.email          = email
          self.senha          = senha
          self.date_created   = datetime.now()
          self.date_modified  = datetime.now()

          

      def get_id(self):
          return str(self.id)

      def add(self,people):
          db.session.add(people)
          return session_commit ()

      def update(self):
          self.date_modified  = datetime.now()
          return session_commit()

      def delete(self,people):
          db.session.delete(people)
          return session_commit()

class Task(db.Model):
      id            = db.Column(db.Integer, primary_key=True)
      titulo        = db.Column(db.String(100), index=True)
      status        = db.Column(db.Integer)
      data          = db.Column(db.Date) 
      date_created  = db.Column(db.DateTime)
      date_modified = db.Column(db.DateTime)
      people_id     = db.Column(db.Integer, db.ForeignKey('people.id'))


      def __repr__(self):
          return '<Task %r>' %(self.titulo)


      def __init__(self,titulo,data, people_id):
          #Status
          # 1 - Ativo
          # 2 - Cancelado
          # 3 - Realizado

          self.titulo         = titulo
          self.status         = 1  
          self.data           = data
          self.people_id     = people_id        
          self.date_created   = datetime.utcnow()
          self.date_modified  = datetime.utcnow()



      def get_id(self):
          return str(self.id)

      def add(self,task):
          db.session.add(task)          
          return session_commit()

      def update(self):
          self.date_modified  = datetime.now()
          return session_commit()

      def delete(self,task):
          db.session.delete(task)
          return session_commit()



#      def set_password(self, password):
#          self.password = generate_password_hash(password)
   
#      def check_password(self, password):
#          return check_password_hash(self.password, password)





#Universal functions

def  session_commit():
      try:
        db.session.commit()
      except SQLAlchemyError as e:             
         db.session.rollback()
         reason=str(e)
         return reason