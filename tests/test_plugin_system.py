import pytest
from calculator.plugin_system import PluginSystem

def test_plugin_system():
    plugin_system = PluginSystem()
    plugin_system.list_plugins()  # Just a simple check to see if listing works
    # Additional checks can be added for plugin loading

