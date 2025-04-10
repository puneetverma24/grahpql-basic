# 📚 GraphQL Bookstore API (Python + Flask + Graphene)

This project is a simple GraphQL API built using **Python**, **Flask**, **Graphene**, and **SQLAlchemy**. It allows you to manage authors and books via a flexible GraphQL endpoint.

---

## 🚀 Features

- GraphQL API endpoint (`/graphql`)
- SQLAlchemy ORM models for `Book` and `Author`
- Full Create and Read operations using GraphQL queries and mutations
- SQLite database (easy local development)
- GraphiQL IDE enabled for interactive queries

---

## 🛠 Tech Stack

- **Python 3.9+**
- **Flask**
- **Graphene** (GraphQL framework for Python)
- **SQLAlchemy**
- **Flask-GraphQL**
- **SQLite**

---
## 📁 Project Structure

bookstore/  
├── app.py           → Main Flask application  
├── models.py        → SQLAlchemy models  
├── schema.py        → GraphQL schema (queries + mutations)  
├── database.py      → DB engine, session, and base setup  
└── README.md        → Project documentation  


---

## 🔧 Setup Instructions

### 1. Clone the Repo

```
git clone https://github.com/your-username/graphql-bookstore.git
cd graphql-bookstore
```


### 2. Install Dependencies
```
pip install -r requirements.txt
```

If you don't have a requirements.txt, install manually:
```
pip install flask graphene graphene-sqlalchemy flask-graphql sqlalchemy
```

### 3. Run the Server
```
python app.py
```
### Server will start at:
```
http://localhost:5000/graphql
```
You can now explore the API using the built-in GraphiQL interface.


## Sample Queries & Mutations
### Create an Author
```
mutation {
  createAuthor(name: "George Orwell") {
    author {
      id
      name
    }
  }
}
```
### Create a Book
```
mutation {
  createBook(title: "1984", authorId: 1) {
    book {
      id
      title
    }
  }
}
```
### Get All Books
```
query {
  allBooks {
    title
    author {
      name
    }
  }
}
```
### Get a Book by ID
```
query {
  book(id: 1) {
    title
    author {
      name
    }
  }
}
```
---
## License
This project is open-source and available under the MIT License.

---
## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 💡 Credits

Built with ❤️ using Graphene, Flask, and SQLAlchemy.

---

## 🔗 Reference
For more details, Check out the [project documentation](https://www.backendmesh.com/a-complete-guide-to-graphql-for-backend-developers/).
