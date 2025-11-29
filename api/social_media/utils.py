from graphene.relay import Node

def node_resolver(ModelNode,info, global_id):
    # body = info.context.body.decode()
    
    _, id = Node.from_global_id(global_id)
    response = ModelNode.get_node(info, id)
    return response



def hash_key(query_body) -> str:
    """
    Generate a unique hash key based on the provided arguments.
    """
    import hashlib

    hash_input = query_body.replace(r'\t', '').replace(r'\n', '').replace(' ', '').replace(',', '')
    return hashlib.sha256(hash_input.encode()).hexdigest()


def save_to_cache(key, value, ModelNode):
    from django.core.cache import cache

    """
    Keep track of the cache keys of all models for later invalidation
    """

    node_name = ModelNode.__name__
    model_cache = cache.get(node_name, set())
    model_cache.add(key)
    cache.set(node_name, model_cache)
    cache.set(key, value)

def get_from_cache(key):
    from django.core.cache import cache

    return cache.get(key)