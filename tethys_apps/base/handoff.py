"""
********************************************************************************
* Name: handoff.py
* Author: Nathan Swain
* Created On: August 11, 2015
* Copyright: (c) Brigham Young University 2015
* License: BSD 2-Clause
********************************************************************************
"""


class HandoffHandler(object):
    """
    An object that is used to register a Handoff handler functions.

    Attributes:
      name(str): Name of the handoff handler.
      handler(str): Path to the handler function for the handoff interaction. Use dot-notation with a colon delineating the function (e.g.: "foo.bar:function").
    """

    def __init__(self, name, handler):
        """
        Constructor
        """
        self.name = name
        self.handler = handler

    def __repr__(self):
        """
        String representation
        """
        return '<Handoff Handler: name={0}, handler={1}>'.format(self.name, self.handler)