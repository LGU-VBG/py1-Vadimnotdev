class Image():
    def __init__(self) -> None:
        self.resolution = None
        self.title = None
        self.extension = None
        self.set_data_by_user()
        self.resize()
    
    def set_data_by_user(self):
        self.resolution = int(input("Enter number for resolution: \n"))
        self.title = int(input("Enter number for title: \n"))
        self.extension = int(input("Enter number for exctension: \n"))
        print(f"Yor numbers is \n {self.resolution} - resolution \n {self.title} - title \n {self.extension} - extension")
    
    def resize(self):
        n = int(input("Enter number for change resolution: \n"))
        self.resolution = n
        print(f"resolution now is {self.resolution}")

img1 = Image()
img2 = Image()
img3 = Image()