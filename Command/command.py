class Wizard():
    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src
    
    def preferences(self, command):
        self.choices.append(command)
        
    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, " to ", self.rootdir)
            else:
                print("No Operation")
    
if __name__ == "__main__":
    # 클라이언트
    wizard = Wizard('python.3.5. gzip', '/usr/bin/')
    
    wizard.preferences({"python": True})
    wizard.preferences({"java":False})
    wizard.execute()