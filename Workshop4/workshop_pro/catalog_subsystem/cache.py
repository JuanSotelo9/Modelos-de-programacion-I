
class Cache:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Cache, cls).__new__(cls)
            cls.instance._preferences = {}
        return cls.instance
    
    def __init__(self):
        self.search_cache = []

    def add_search_result(self, search, result):
        self.search_cache.insert(0, (search, result))

        if len(self.search_cache) > 3:
            self.search_cache.pop()

    def get_search_result(self, search):
        for cache_search, result in self.search_cache:
            if cache_search == search:
                return result
        return None
    
    def clear_cache(self):
        self.search_cache = []