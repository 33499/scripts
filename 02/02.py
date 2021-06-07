from typing import Counter
from sqlalchemy import Column, String, create_engine, Integer, engine
from sqlalchemy.ext import declarative
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()
# 初始化数据库连接:
engine = create_engine('postgresql+psycopg2://postgres:402402402@120.27.241.217/app1')
engine = create_engine('sqlite:///foo.db')

# 定义User对象
class User(Base):
    #表的名字
    __tablename__ = 'user'

    #表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    age = Column(Integer)

    def __repr__(self):
        return 'User(id={id},name={name},age={age})'.format(id=self.id, name=self.name, age=self.age)
#创建所有定义的表到数据库中
def init_db():
    Base.metadata.create_all(engine)

#从数据库中删除所有定义的表
def drop_db():
    Base.metadata.drop_all(engine)

if __name__ == '__main__':
    drop_db()
    init_db()
    #创建DBsession类型和对象
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    #创建User对象
    new_user = User(id='7', name='ali', age=11)
    user1 = User(id='8', name='mary', age=12)
    user2 = User(id='1', name='bob', age=12)
    #插入数据
    session.add(new_user)
    session.add_all([user2,user1])
    session.commit()
    #更新数据
    # session.query(User).filter(User.id == 1).delete()
    # session.commit()
    # 查询数据
    ret = session.query(User).all()
    print(ret)
    session.close()