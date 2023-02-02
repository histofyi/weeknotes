from flask import request, current_app, redirect, abort

from functools import wraps

from .templating import render



def templated(template:str):
    """
    This decorator is used perform html templating of views.

    Args:
        template (string) : the name of the template to be used
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = f"{request.endpoint.replace('.', '/')}.html"
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                ctx = {'content': ctx}
            ctx['site_title'] = current_app.config['SITE_TITLE']
            ctx['static_route'] = current_app.config['STATIC_ROUTE']
            if 'collection_colours' in current_app.data:
                ctx['collection_colours'] = current_app.data['collection_colours']
            if 'chains' in current_app.data:
                ctx['chain_types'] = current_app.data['chains']
            if 'features' in current_app.data:
                ctx['features'] = current_app.data['features']
            if '/' in template_name:
                section = template_name.split('/')[0]
                ctx['nav'] = section
            if not 'redirect_to' in ctx:
                if not 'code' in ctx:
                    ctx['code'] = 200
                return render(template_name, ctx)
            else:
                return redirect(ctx['redirect_to'], 302)
        return decorated_function
    return decorator