"""
Example toolbox.

"""
from custom_module.custom_tool_one import ToolOne
from custom_module.custom_tool_two import ToolTwo


class Toolbox(object):
    """
    Example Toolbox class.

    """
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Custom Toolbox"
        self.alias = 'Custom_tbx'
        self.description = 'This toolbox is used as an template'


        # List of tool classes associated with this toolbox
        self.tools = [ToolOne, ToolTwo]
