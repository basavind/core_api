from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.orm import relationship

Base = declarative_base()

class IntPk:
    id = Column(Integer, primary_key=True)


class PluralName:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'


class Material(Base, IntPk, PluralName):
    __tablename__ = 'materials'
    file_path = Column(String)
    slices = relationship(
        'Slice',
        order_by='Slice.position',
        collection_class=ordering_list('position'),
        backref='material'
    )


class Slice(Base, IntPk, PluralName):
    __tablename__ = 'slices'
    material_id = Column(Integer, ForeignKey('materials.id'))
    position = Column(Integer)
