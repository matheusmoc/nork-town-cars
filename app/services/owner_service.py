from app.models import db
from app.models.owner import Owner
from sqlalchemy import asc, desc

def create_owner(name, contact=None):
    new_owner = Owner(name=name, contact=contact)
    db.session.add(new_owner)
    db.session.commit()
    return new_owner

def get_all_owners():
    return Owner.query.order_by(desc(Owner.id)).all()

def get_owner_by_id(owner_id):
    return Owner.query.get(owner_id)

def update_owner(owner_id, name=None, contact=None):
    owner = get_owner_by_id(owner_id)
    if owner:
        if name:
            owner.name = name
        if contact:
            owner.contact = contact
        db.session.commit()
    return owner

def delete_owner(owner_id):
    owner = get_owner_by_id(owner_id)
    if owner:
        db.session.delete(owner)
        db.session.commit()
        return True
    return False
