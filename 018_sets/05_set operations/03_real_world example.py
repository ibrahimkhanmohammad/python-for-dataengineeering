#   in a test conducted to a class of students find out the students who failed in both subjects and also failed in either subject
sub1_failed = {'Aman', 'Rahul', 'Priya', 'Manoj'}
sub2_failed ={'Priya', 'Karan', 'Aman'}

#   students who failed in both subjects
print(sub1_failed.intersection(sub2_failed))

#   students who failed in either subject
print(sub1_failed.union(sub2_failed))