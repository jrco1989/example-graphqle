import graphene

from .types import Query as SchemaQuery

class Query(SchemeQuery, graphene.ObjectType):
    pass

schema= graphene.Schema(query=Query)
