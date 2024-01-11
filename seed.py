from app  import app, db
from models import Customer, Author, Book


def seed_data():
    author1 = Author(name="Eric", yob=2000, nationality="Uganda")
    author2 = Author(name="Faith", yob=2001, nationality="Kenya")

    db.session.add_all([author1, author2])
    db.session.commit()

    # Books
    book1 = Book(title="Lorem Ipsum", published_year=2021, price=2400, qty_in_stock=5,author_id = author2.id )
    book2 = Book(title="Life in the Jungle", published_year=2023, price=4000, qty_in_stock=3, author_id = author1.id )

    db.session.add_all([book1, book2])
    db.session.commit()

    # Customers
    customer1 = Customer(name="Brian Cherus", email="brian@gmail.com", phone="0712345678", address = "Ngong Road" )
    customer2 = Customer(name="Onesmus Githua", email="onesmus@gmail.com", phone="0112345678", address = "Ngong Road" )

    db.session.add_all([customer1, customer2])
    db.session.commit()


if __name__ =='__main__':
    with app.app_context():
        print("Seeding started -----")
        seed_data()
        print("Seeded successfully")

