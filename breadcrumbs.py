from flask import g

from collections import namedtuple, Sequence

Breadcrumb = namedtuple('Breadcrumb', ['url', 'name'])


def breadcrumbs(*bcs):
    g.breadcrumbs = []
    for item in bcs:
        if isinstance(item, Sequence) and not isinstance(item, str):
            bc = Breadcrumb(url=item[0], name=item[1])
        else:
            bc = Breadcrumb(url=None, name=item)

        g.breadcrumbs.append(bc)
