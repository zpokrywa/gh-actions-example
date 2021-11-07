from hello import print_name


def test_hello_default():
    assert print_name() == "Hello World\n"


def test_hello_name():
    assert print_name("George") == "Hello George\n"
