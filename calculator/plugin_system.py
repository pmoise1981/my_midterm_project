import importlib
import os

class PluginSystem:
    def __init__(self, plugin_dir='calculator/plugins'):
        self.plugin_dir = plugin_dir

    def load_plugin(self, plugin_name):
        try:
            plugin = importlib.import_module(f"calculator.plugins.{plugin_name}")
            plugin.run()
            logging.info(f"Plugin {plugin_name} loaded successfully.")
        except ModuleNotFoundError:
            logging.error(f"Plugin {plugin_name} not found.")
        except Exception as e:
            logging.error(f"Error loading plugin {plugin_name}: {str(e)}")

    def list_plugins(self):
        plugins = os.listdir(self.plugin_dir)
        for plugin in plugins:
            if plugin.endswith('.py') and plugin != '__init__.py':
                print(f"- {plugin[:-3]}")

