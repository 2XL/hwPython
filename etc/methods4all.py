class Method:
    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self):
        pass

    def __del__(self):
        # called on garbage collection or on destroy
        pass

    def __bytes__(self):
        pass

    def __hash__(self):
        pass

    def __str__(self):
        pass # called when str(self)

    def __bool__(self):
        pass # if not defined __len__ is called, if neither then default: true.

    def __call__(self, *args, **kwargs):
        # invoked on self(args...), when an instance is called like a function.
        # args may take any function-defined argument form.
        pass

    def __getattr__(self, item):
        # this is called when the attribute intended to access does not exist
        pass

    def __delattr__(self, item):
        # called on `del self.name`
        pass