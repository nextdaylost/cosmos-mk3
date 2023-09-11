"""Plugin utilities."""


from importlib import import_module
from pkgutil import iter_modules, ModuleInfo
from typing import Any, Iterator

import cosmos.plugins.datasets


def iter_namespace(namespace: Any) -> Iterator[ModuleInfo]:
    """Retrieves module info for a given namespace.

    Args:
        namespace: The namespace to search.
    """
    return iter_modules(namespace.__path__, namespace.__name__ + ".")


dataset_plugins = {
    name: import_module(name)
    for finder, name, is_pkg
    in iter_namespace(cosmos.plugins.datasets)
}
