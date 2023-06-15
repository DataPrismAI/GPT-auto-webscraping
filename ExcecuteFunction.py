import importlib

def execute_function():
    module = "output"
    function = "extract_info"
    module = importlib.import_module(module)
    function = getattr(module, function)
    print("returning function")
    return function
