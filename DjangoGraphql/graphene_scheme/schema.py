import graphene

from .types import Query as SchemaQuery
from .types import Query as SchemeQuery
from .mutation import Mutation as SchemeMutation

class Query(SchemaQuery, graphene.ObjectType):
    pass

class Mutation(SchemeMutation, graphene.ObjectType):
    pass

schema= graphene.Schema(query=Query, mutation=Mutation)
