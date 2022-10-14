from typing import Any, Dict, List, Tuple

from docutils import nodes
from docutils.parsers.rst import roles
from docutils.nodes import Node, system_message
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.util.docutils import ReferenceRole


class PyPIRole(ReferenceRole):
    def run(self) -> Tuple[List[Node], List[system_message]]:
        target_id = 'index-%s' % self.env.new_serialno('index')
        entries = [
            ('single', f"PyPI package: {self.target}", target_id, '', None)
        ]

        index = addnodes.index(entries=entries)
        target = nodes.target('', '', ids=[target_id])
        self.inliner.document.note_explicit_target(target)

        refuri = f"https://pypi.org/project/{self.target}/"
        reference = nodes.reference('', '', internal=False, refuri=refuri)
        if self.has_explicit_title:
            reference += nodes.strong(self.title, self.title)
        else:
            title = self.title
            reference += nodes.strong(title, title)

        return [index, target, reference], []


def setup(app: Sphinx) -> Dict[str, Any]:
    roles.register_local_role("pypi", PyPIRole())

    return {
        'version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
