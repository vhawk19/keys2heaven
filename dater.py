import pandas as pandas
import faker


fake=Faker()

def student_names():
	a=[]
	for _ in range(50):
		a+=[fake.name()]
	return a

def create_id_name_pair():
	students=student_names()
	id_name=[]
	for i in range(50):
		id_name+=[hash(i),students[i]]
	df=pd.DataFrame(id_name,columns=['id','age'])
	df.to_csv('master.csv',sep='\t',encoding='utf-8')

create_id_name_pair();
