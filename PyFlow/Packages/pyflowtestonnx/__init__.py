PACKAGE_NAME = 'pyflowtestonnx'

from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Function based nodes
from PyFlow.Packages.pyflowtestonnx.FunctionLibraries.DemoLib import DemoLib

# Class based nodes
from PyFlow.Packages.pyflowtestonnx.Nodes.DemoNode import DemoNode

# Exporters
from PyFlow.Packages.pyflowtestonnx.Exporters.DemoExporter import DemoExporter

# Factories
from PyFlow.Packages.pyflowtestonnx.Factories.UINodeFactory import createUINode

_FOO_LIBS = {}
_NODES = {}
_PINS = {}
_TOOLS = OrderedDict()
_PREFS_WIDGETS = OrderedDict()
_EXPORTERS = OrderedDict()

_FOO_LIBS[DemoLib.__name__] = DemoLib(PACKAGE_NAME)

_NODES[DemoNode.__name__] = DemoNode

_EXPORTERS[DemoExporter.__name__] = DemoExporter


class pyflowtestonnx(IPackage):
	def __init__(self):
		super(pyflowtestonnx, self).__init__()

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

