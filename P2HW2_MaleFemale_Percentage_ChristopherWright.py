#Getting the male to female percentage in a class.
#9/21/2018
#CTI-110 P2HW2-Male Female Percentage
#Christopher Wright


males=int(input("Enter number of males in class:"))
females= int(input("Enter number of females in class:"))
totalStudents= males+females
malePercentage= males/totalStudents
femalePercentage= females/totalStudents
print("There are "  + str(totalStudents )+" students." +\
format(malePercentage,".0%")+ " males " +\
format(femalePercentage,".0%")+ " females ")                

