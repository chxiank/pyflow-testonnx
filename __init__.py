PACKAGE_NAME = 'node'

from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Class based nodes
from PyFlow.Packages.node.Nodes.DemoNode import DemoNode

# Factories
from PyFlow.Packages.node.Factories.UINodeFactory import createUINode

_FOO_LIBS = {}
_NODES = {}
_PINS = {}
_TOOLS = OrderedDict()
_PREFS_WIDGETS = OrderedDict()
_EXPORTERS = OrderedDict()

_NODES[DemoNode.__name__] = DemoNode


class node(IPackage):
	def __init__(self):
		super(node, self).__init__()

	@staticmethod
	def GetExporters():
		return _EXPORTERS

	@staticmethod
	def GetFunctionLibraries():
		return _FOO_LIBS

	@staticmethod
	def GetNodeClasses():
		return _NODES

	@staticmethod
	def GetPinClasses():
		return _PINS

	@staticmethod
	def GetToolClasses():
		return _TOOLS

	@staticmethod
	def UINodesFactory():
		return createUINode

