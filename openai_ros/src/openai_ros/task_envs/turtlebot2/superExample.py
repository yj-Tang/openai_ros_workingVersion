class SomeBaseClass(object):
    def __init__(self):
        print('SomeBaseClass.__init__(self) called')
    
class UnsuperChild(SomeBaseClass):
    def __init__(self):
        print('UnsuperChild.__init__(self) called')
        SomeBaseClass.__init__(self)
    
class SuperChild(SomeBaseClass):
    def __init__(self):
        print('SuperChild.__init__(self) called')
        super().__init__()