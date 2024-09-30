'''userText="Patient Name:Koushik Date:13/05/2021 Doctor:Nikhil Problem:Cold"
x = userText.split()
print(x)
nm=(x[2])
dt=(x[3])
dc=(x[4])
pb=(x[5])
name = (nm.split(':'))
dted = (dt.split(':'))
doc = (dc.split(':'))
pro = (pb.split(':'))'''
import imp
my_model = imp.load_compiled("mymodel","train.cpython-37.pyc")
