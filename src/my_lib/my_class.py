class MyClass:
    """_summary_

    Attributes:
        attr (int): description
    """
    def __init__(self, attr1: int):
        """_summary_

        Args:
            attr1 (int): _description_
        """
        self.attr1 = attr1

    def method1(self, message: str) -> str:
        """print 'message attr1'

        Args:
            message (str): _description_

        Outputs:
            message (str): _description_
        """
        message = f"{message} {self.attr1}"
        return message
