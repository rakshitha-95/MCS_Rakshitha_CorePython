'''
11.Find common elements in 2 lists
'''
employee_list = ['Asha', 'Nikhil', ' Akhil', 'Nishitha', 'Keerthi','Sindhu']
programmers_list = ['nishant','keerthi', 'Rohit', 'nikhil', 'Suman', 'asha']
common_ele_list = []
for i in employee_list:
    for j in programmers_list:
        if i.lower() == j.lower():
            common_ele_list.append(i)
if not len(common_ele_list):
    print('No common elements found')
else:
    print('Common Elemenets :', common_ele_list)

    """a,b,c,d,e = '12,34'
    print(a,b,c,d,e)

    list1 = ['a','b']
    for i in list1:
        list1.append(i)

    print(list1)
    """
