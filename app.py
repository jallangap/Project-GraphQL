from flask import Flask
from graphene import ObjectType, String, Schema
from flask_graphql import GraphQLView

class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return f"Hello, {name}!"

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=Schema(query=Query), graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
