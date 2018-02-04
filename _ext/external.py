"""Extension to load external links in new window."""
import re
from sphinx.writers.html import HTMLTranslator
from sphinx.builders.html import StandaloneHTMLBuilder
from docutils import nodes

ALLOWED_HOSTS = [
    'git-pull.com',
    '0.0.0.0',
]


class GitPullHTMLTranslator(HTMLTranslator):

    def visit_reference(self, node):
        """
        Changes:

        - monkeypatch bugfix https://sourceforge.net/p/docutils/bugs/322/
        - add target _blank to offsite urls
        - add class offsite for offsite urls
        - add class insite for insite urls (note, internal is already used
          for reference links in the *same* document)
        """
        atts = {'class': 'reference'}

        if 'refuri' in node:
            atts['href'] = node['refuri']
            if (self.settings.cloak_email_addresses and
                    atts['href'].startswith('mailto:')):
                atts['href'] = self.cloak_mailto(atts['href'])
                self.in_mailto = True
            atts['class'] += ' external'
            if (not any(node['refuri'] in host
                        for host in ALLOWED_HOSTS) and
                    not node['refuri'].startswith('#') and
                    not re.match(r'(\.\.)?(\/)?[\w_]*\.html', node['refuri']) and
                    not node['refuri'].startswith('/')):
                atts['target'] = '_blank'
                atts['class'] += ' offsite'
                # sphinx sites, a ref wrapping a nodes.literal is a code link
                if isinstance(node[0], nodes.literal):
                    atts['class'] += ' code'
            else:
                atts['class'] += ' insite'
        else:
            assert 'refid' in node, \
                'References must have "refuri" or "refid" attribute.'
            atts['href'] = '#' + node['refid']
            atts['class'] += ' internal'

        self.body.append(self.starttag(node, 'a', '', **atts))


def setup(app):
    app.set_translator('html', GitPullHTMLTranslator)
# vim: set expandtab shiftwidth=4 softtabstop=4 :
