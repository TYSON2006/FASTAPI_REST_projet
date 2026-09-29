from db.data_base import Base 
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String,Boolean,Date,func
from datetime  import datetime,date
from models._models_users import Users


class Tasks(Base):
    __tablename__ = "table_taches"
    id : Mapped[int]= mapped_column(Integer,primary_key=True,index=True)
    title: Mapped  [str]=mapped_column(String)
    description:Mapped[str|None]=mapped_column(String)
    completed:Mapped[bool]= mapped_column(Boolean,default=False)
    priorities : Mapped[str]= mapped_column(String,)
    datecreation:Mapped [datetime] = mapped_column(Date, default= func.now())
    user_id : Mapped[int]= mapped_column(Integer,primary_key=("Users.id"))