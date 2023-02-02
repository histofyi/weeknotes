from functions.app import app_context
import datetime
import calendar


class Posts():
    def __init__(self):
        self.posts = app_context.data['posts']
        self.facets = app_context.data['facets']
        self.tags = app_context.data['facets']['tags']
        self.ordering = app_context.data['ordering']
        self.facet_type = None
        self.facet_name = None

    def add_fulldate(self, post):
        post['metadata']['fulldate'] = datetime.datetime(post['metadata']['year'], post['metadata']['month'], post['metadata']['day'])
        return post

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
        for post in ordered_posts:
            post = self.add_fulldate(post)
        return_data = {'posts':ordered_posts}
        if self.facet_type and self.facet_name:
            return_data['facet_type'] = self.facet_type
            return_data['facet_name'] = self.facet_name
            if self.facet_type == 'months':
                year = self.facet_name[0:4]
                month = int(self.facet_name[4:6])
                return_data['facet_ui_name'] = f'{calendar.month_name[month]} {year}'
            else:
                return_data['facet_ui_name'] = self.facet_name

        return return_data


    def latest(self, limit=10):
        posts = self.order_posts()
        posts['posts'] = posts['posts'][:limit]
        return posts


    def filter(self, facet_type, facet_name):
        self.facet_type = facet_type
        self.facet_name = str(facet_name)
        return self.order_posts()


    def all_tags(self):
        processed_tags = {tag:len(self.tags[tag]) for tag in self.tags}
        tags = {'tags':processed_tags}
        return tags


    def get(self, slug):
        if slug in self.posts:
            post = self.add_fulldate(self.posts[slug])
            return {'post':post}
        else:
            return {'error':f'No match for {slug}'}