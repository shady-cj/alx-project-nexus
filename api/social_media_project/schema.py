import graphene

from graphql_auth.schema import UserQuery, MeQuery
from user_management.schema import AuthMutation
from social_media.schema import SocialMediaQuery, SocialMediaMutation

class Query(UserQuery, MeQuery, SocialMediaQuery, graphene.ObjectType):
    pass

class Mutation(AuthMutation, SocialMediaMutation, graphene.ObjectType):
    pass 



schema = graphene.Schema(query=Query, mutation=Mutation)