from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.orm import relationship

Base = declarative_base()

class IntPk:
    id = Integer(primary_key=True)

class Material(Base, IntPk):
    __tablename__ = 'materials'
    file_path = Column(String)
    slices = relationship(
        'Slice',
        order_by='Bullet.position',
        collection_class=ordering_list('position'),
        backref='material'
    )

class Slice(Base, IntPk):
    __tablename__ = 'slices'
    material_id = Integer(ForeignKey('Material.id'))
    position = Column(Integer)
