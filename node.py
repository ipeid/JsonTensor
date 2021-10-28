
from __future__ import unicode_literals

import uuid

class Node(object):
    """
    Nodes are elementary objects that are stored in the `_nodes` dictionary of a Tree.
    Use `data` attribute to store node-specific data.
    """

    def __init__(self, child=None, identifier=None, child_type=None, deep=None):
        """Create a new Node object to be placed inside a Tree object"""

        #: if given as a parameter, must be unique
        self._identifier = None
        self._set_identifier(identifier)

        self._child = child
        self._child_type = child_type
        self.deep = deep


    def _set_identifier(self, nid):
        """Initialize self._set_identifier"""
        if nid is None:
            self._identifier = str(uuid.uuid1())
        else:
            self._identifier = nid

    @property
    def identifier(self):
        """
        The unique ID of a node within the scope of a tree. This attribute can be
        accessed and modified with ``.`` and ``=`` operator respectively.
        """
        return self._identifier

    @identifier.setter
    def identifier(self, value):
        """Set the value of `_identifier`."""
        if value is None:
            print("WARNING: node ID can not be None")
        else:
            self._set_identifier(value)

    @property
    def child(self):
        """
        The readable node name for human. This attribute can be accessed and
        modified with ``.`` and ``=`` operator respectively.
        """
        return self._child

    @child.setter
    def child(self, value):
        """Set the value of `_child`."""
        self._child = value if value is not None else None

    @property
    def child_type(self):
        """
        The readable node name for human. This attribute can be accessed and
        modified with ``.`` and ``=`` operator respectively.
        """
        return self._child_type

    @child_type.setter
    def child_type(self, value):
        """Set the value of `_child`."""
        if value not in ["list", "dict", "value"]:
            raise ValueError("unknow child type, must be 'list', 'dict' or 'value' !")
        self._child_type = value

    @property
    def deep(self):
        """
        The readable node name for human. This attribute can be accessed and
        modified with ``.`` and ``=`` operator respectively.
        """
        return self._deep

    @deep.setter
    def deep(self, value):
        """Set the value of `_child`."""
        self._deep = value if value is not None else None

    def __repr__(self):
        name = self.__class__.__name__
        kwargs = [
            "child={0}".format(self.child),
            "identifier={0}".format(self.identifier),
            "child_type={0}".format(self.child_type),
            "deep={0}".format(self.deep),
        ]
        return "%s(%s)" % (name, ", ".join(kwargs))
