from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
from database import Base, engine

app = Flask(__name__)

# Create DB Tables
Base.metadata.create_all(bind=engine)

# Add GraphQL endpoint
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True  # Enable GraphiQL UI
    ),
)

if __name__ == "__main__":
    app.run(debug=True)
