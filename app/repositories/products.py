from sqlalchemy.orm import Session

import app.schemas.schemas as schemas
import app.models.models as models


def get_product(db: Session, product_id: int):
    """
    select * from products where id = product_id
    limit 1
    """
    return db.query(models.Product).filter(models.Product.id == product_id).first()