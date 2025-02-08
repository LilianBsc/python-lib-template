from my_lib import MyClass


def test_my_class():
    x = MyClass(attr1=1)
    assert x.method1("print") == "print 1"
