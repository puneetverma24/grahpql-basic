import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Book, Author
from database import SessionLocal

# Object Types
class AuthorType(SQLAlchemyObjectType):
    class Meta:
        model = Author

class BookType(SQLAlchemyObjectType):
    class Meta:
        model = Book

# Queries
class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.Int(required=True))

    def resolve_all_books(parent, info):
        db = SessionLocal()
        return db.query(Book).all()

    def resolve_book(parent, info, id):
        db = SessionLocal()
        return db.query(Book).filter(Book.id == id).first()

# Mutations
class CreateAuthor(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    author = graphene.Field(lambda: AuthorType)

    def mutate(self, info, name):
        db = SessionLocal()
        new_author = Author(name=name)
        db.add(new_author)
        db.commit()
        return CreateAuthor(author=new_author)

class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author_id = graphene.Int(required=True)

    book = graphene.Field(lambda: BookType)

    def mutate(self, info, title, author_id):
        db = SessionLocal()
        new_book = Book(title=title, author_id=author_id)
        db.add(new_book)
        db.commit()
        return CreateBook(book=new_book)

class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    create_book = CreateBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
