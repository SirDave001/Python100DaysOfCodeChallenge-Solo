class Engineer:
    def __init__(self, LicenseNo):
        self.LicenseNo = LicenseNo
    def DesignProjects(self):
        print('I am designing a project!')
class SeniorEngineer(Engineer):
    def __init__(self, LicenseNo, NumProjects):
        super().__init__(LicenseNo)
        self.NumProjects = NumProjects
    def DealProjects(self):
        print('I have a project to do.')
        self.NumProjects += 1
class SeniorComputerEngineer(SeniorEngineer):
    def __init__(self, LicenseNo, NumProjects, CurrentProject):
        super().__init__(LicenseNo, NumProjects)
        self.Curentproject = CurrentProject
        
Leslie = Engineer('AB123')
Leslie.DesignProjects()

Cindy = SeniorEngineer('CD456', 5)
Cindy.DealProjects()
print(f'Cindy has handled {Cindy.NumProjects} projects so far')

Terry = SeniorComputerEngineer('EF789', 8, 'Blockchain')
print(f'Terry is currently working on a {Terry.Curentproject} project.')