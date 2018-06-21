class ContentFilter:
    
    def __init__(self, filename):
        self.filename = filename
        self.contents = None
        while self.contents is None:
            try:
                with open(self.filename, 'r') as file:
                    contents = file.readlines()
                self.contents = contents
            except:
                self.filename = input("Please provide a valid filename: ")
            
    def uniform(self, file, mode='w', case='upper'):
        if mode not in ['w', 'x', 'a']:
            raise ValueError('invalid writing mode')
        with open(file, mode) as f:
            if case == 'upper':
                for line in self.contents:
                    f.write(line.upper())
            elif case == 'lower':
                for line in self.contents:
                    f.write(line.lower())
            else:
                raise ValueError('case must be either upper or lower')
                
    def reverse(self, file, mode='w', unit='line'):
        with open(file, mode) as f:
            if unit == 'line':
                for line in self.contents[::-1]:
                    f.write(line)