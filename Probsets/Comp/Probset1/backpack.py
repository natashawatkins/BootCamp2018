class Backpack:
    
    """
    A Backpack object class. Has a name, color, size and a list of contents.
    Attributes:
        name (str): the name of the backpack's owner.
        color (str): the color of the backpack.
        max_size (int), optional: maximum capacity in backpack.
        contents (list): the contents of the backpack.
    """
    def __init__(self, name, color, max_size=5):           # This function is the constructor.
        """
        Set the name and initialize an empty list of contents.
        Parameters:
            name (str): the name of the backpack's owner.
            color (str): the color of the backpack.
            max_size (int), optional: maximum capacity in backpack.
        """
        self.name, self.color, self.max_size = name, color, max_size
        self.contents = []
    
    def put(self, item):
        """Add 'item' to the backpack's list of contents."""
        if len(self.contents) >= self.max_size:
            print("No room!")
        else:
            self.contents.append(item)  # Use 'self.contents', not just 'contents'.
         
    def take(self, item):
        """Remove 'item' from the backpack's list of contents."""
        self.contents.remove(item)
        
    def dump(self):
        '''Remove all contents from the backpack'''
        self.contents = []
        
def test_backpack():
    testpack = Backpack("Barry", "black")       # Instantiate the object.
    if testpack.name != "Barry":                # Test an attribute.
        print("Backpack.name assigned incorrectly")
    for item in ["pencil", "pen", "paper", "computer"]:
        testpack.put(item)                      # Test a method.
    print("Contents:", testpack.contents)
    print("Removing last item...")
    testpack.take(testpack.contents[-1])
    print("Contents:", testpack.contents)
    print("Dumping contents...")
    testpack.dump()
    print("Contents:", testpack.contents)
    
test_backpack()