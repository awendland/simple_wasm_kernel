from ipykernel.kernelapp import IPKernelApp
from .kernel import WasmKernel
IPKernelApp.launch_instance(kernel_class=WasmKernel)
