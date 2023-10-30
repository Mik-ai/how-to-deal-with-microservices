from orm import linux_db, windows_db
import load_models


from sqlalchemy.orm import Session
from sqlalchemy import select
from config import engine


def main():
    # testing model:
    stmt = (
        select(windows_db.ProductsData.marketplace_id)
        .where(
            windows_db.ProductsData.marketplace_id.in_(
                [361554111, 361554114, 409406582]
            )
        )
        .limit(2)
    )

    with Session(engine) as session:
        result = session.execute(stmt).all()
        session.rollback()
    # конец проверки модели

    print("debug")


if __name__ == "__main__":
    main()
