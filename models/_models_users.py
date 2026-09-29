from db.data_base import Base 
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String,Date, Boolean
from datetime  import datetime
from sqlalchemy import Column

class Users(Base):
    __tablename__ = "Users"
    id : Mapped[int]= mapped_column(Integer,autoincrement=True,primary_key=True,index=True)
    nom: Mapped[str]= mapped_column(String,index=True)
    last_name : Mapped [str]= mapped_column(String,index=True)
    email:Mapped[str]=mapped_column(String,unique=True, nullable=False)
    password:Mapped[str]=mapped_column(String)
    datecreation:Mapped[Date|datetime]=mapped_column(Date,default = datetime.now())
    
    
    
    
    
