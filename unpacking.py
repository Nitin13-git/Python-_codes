def get_marks(scores_dataset, subject):
    l=[]
    for student in scores_dataset:
        print(student)
        if subject in student:
            l.append((student['Name'],student[subject]))
    return l
scores_dataset={'name':'nitin','cardno':10,'physics':90,"mathematics":90}
for x in scores_dataset:
    print(x)
    
    
    
    
    
    
   
