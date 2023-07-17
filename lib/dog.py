from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, search_name):
    #these both do the same thing
    print(session.query(Dog).filter_by(name=search_name).all())
    print(session.query(Dog).filter(Dog.name.like(f'%{search_name}%')).all())
    return session.query(Dog).filter_by(name=search_name).all()[0]

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id)[0]

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed)[0]

def update_breed(session, search_dog, updated_breed):
    for dog in session.query(Dog):
        if dog.id == search_dog.id:
            dog.breed = updated_breed 