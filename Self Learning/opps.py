class divA:

   
    def __init__(self,name):
        self.div = 'A'
        self.sname = name

        pass

    def AddSubject(self,subName):
           self.subjectName = subName



_81 = divA("shivam")
_31 = divA("nupur")

print(_31.sname)


_31.AddSubject("network")

print(_31.subjectName)
_31.AddSubject("pytrhon")

print(_31.subjectName)

        