"""
The table below outlines the grade boundaries on a certain university course. Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.
points	grade
< 0	impossible!
0-49	fail
50-59	1
60-69	2
70-79	3
80-89	4
90-100	5
> 100	impossible!

Some examples:
Sample output

How many points [0-100]: 37
Grade: fail
Sample output

How many points [0-100]: 76
Grade: 3
Sample output

How many points [0-100]: -3
Grade: impossible!

"""

# se avessi dovuto fare un controllo su moltissimi numeri sarebbe convenuto usare set(range()),
#  poichè controllo di complessità O(1), quindi istantaneo


def grades_points():

    fail = range(50)
    vote_1 = range(50, 60)
    vote_2 = range(60, 70)
    vote_3 = range(70, 80)
    vote_4 = range(80, 90)
    vote_5 = range(90, 101)
    
    user_vote = int(input("How many points [0-100]: "))

    if user_vote < 0:
        print("impossible!")
    
    elif user_vote in fail:
        print("Grade: fail")
    
    elif user_vote in vote_1:
        print("Grade: 1")
    
    elif user_vote in vote_2:
        print("Grade: 2")
    
    elif user_vote in vote_3:
        print("Grade: 3")
    
    elif user_vote in vote_4:
        print("Grade: 4")
    
    elif user_vote in vote_5:
        print("Grade: 5")
    
    else:
        print("Grade: impossible!")


grades_points()