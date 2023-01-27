from functions.app import app_context


class Posts():
    def __init__(self):
        self.posts = app_context.data['posts']
        self.facets = app_context.data['facets']
        self.tags = app_context.data['facets']['tags']
        self.ordering = app_context.data['ordering']
        self.facet_type = None
        self.facet_name = None


    def order_posts(self, order_by='weeks', ordering='desc'):
        ordering = f'{order_by}_{ordering}'
        if self.facet_type and self.facet_name:
            #try
            facet = self.facets[self.facet_type][self.facet_name]
            #except:
            #    facet = []
            ordered_posts = [self.posts[slug] for slug in self.ordering[ordering] if slug in facet]
        else:
            ordered_posts = [self.posts[slug] for slug in self.ordering[ordering]]
        return ordered_posts


    def latest(self, limit=10):
        return self.order_posts()[:limit]


    def filter(self, facet_type, facet_name):
        self.facet_type = facet_type
        self.facet_name = str(facet_name)
        return self.order_posts()


    def all_tags(self):
        processed_tags = {tag:len(self.tags[tag]) for tag in self.tags}
        return processed_tags


    def get(self, slug):
        if slug in self.posts:
            return self.posts[slug]
        else:
            return {'error':f'No match for {slug}'}