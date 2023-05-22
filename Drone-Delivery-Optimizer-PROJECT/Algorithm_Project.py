class Drones():
    def __init__(self):            #intilize all requested array and needed array and pointers
        self.schedule = [0] * 1000
        self.schedule_pointer = 1  #will always point at the last inserted element + 1
        self.recharge = [0] * 100
        self.recharge_pointer = 1
        self.solution = [0] * 1000
        self.used = [0] * 1000

    def insert(self,arr1,arr2):                              #add user input array into the right array
        if len(arr1) != 0 and self.schedule_pointer != 1000: #nothing will be added in case user array were empty or class array is full
            for N , i in zip(range(self.schedule_pointer,self.schedule_pointer+len(arr1)),range(0,len(arr1))):
                self.schedule[N]= arr1[i]
            self.schedule_pointer = self.schedule_pointer + len(arr1)

        if len(arr2) != 0 and self.recharge_pointer != 100:
            for M , j in zip(range(self.recharge_pointer,self.recharge_pointer + len(arr2)),range(0,len(arr2))):
                self.recharge[M]=arr2[j]
            self.recharge_pointer = self.recharge_pointer + len(arr2)

        self.OPS() #recalculate optimal solution

    def OPS(self):
        for N in range(1,self.schedule_pointer):    #loop from 1 to the schedule pointer to save time
            max = -9999999
            for M in range(N):
                if N - M > self.recharge_pointer-1: #N - M is greater than recharge pointer than we use the last inserted element in array recharge
                    if max <= self.solution[M] + min(self.schedule[N], self.recharge[self.recharge_pointer-1]):
                        max = self.solution[M] + min(self.schedule[N], self.recharge[self.recharge_pointer-1])
                        self.used[N] = M
                else:                               #otherwise we look for the element N-M to know recharge hours
                    if max <= self.solution[M] + min(self.schedule[N], self.recharge[N - M]):
                        max = self.solution[M] + min(self.schedule[N], self.recharge[N - M])
                        self.used[N] = M

            self.solution[N] =max                   #save the max number of object into array for each element N inside array schedule

    def optimal_for_n(self,n):
        print("Maximum number of objects: {}".format(self.solution[n]))       #print the maximum amount of object for hour n entered by the user that is saved in array solution
        print("Hours drone was used:",end=" ")
        h = n
        dummy_list = []
        dummy_list.append(h)
        while self.used[h] != 0:                    #save all hours the drone was used to achieve the maximum for hour n in dummy list
            h = self.used[h]
            dummy_list.append(h)
        for i in range(len(dummy_list)-1,-1,-1):    #print in reserve
            print(dummy_list[i], end =" ")


        print()

#after we finish the class we will create the main

d = Drones()    #intlize the class

while True:
    print("1- Enter 1 to insert hours")
    print("2- Enter 2 to find the maximum delivery for a given hour and find the hours the drone was used")
    print("3- Enter 3 to exit the program")
    x = int(input("\nEnter your choice: "))
    if x == 1:                             #ask the user to enter array to insert the element inside to the corrosponding array in the class
        print("The current hours entered in array schedule is {}".format(d.schedule_pointer - 1))
        N = list(map(int, input("Enter the amount of object schedule to deliver (remember your enteries will be saved in hour {} and onward)\nLeave space between your values: ".format(d.schedule_pointer)).strip().split())) # Use Space to enter your values
        print("The current hours entered in array recharge is {}".format(d.recharge_pointer - 1))
        M = list(map(int, input("Enter the amount the drone able to deliver for amount of hours the drone was charged (remember your enteries will be saved in hour {} and onward)\nLeave space between your values: ".format(d.recharge_pointer)).strip().split()))
        d.insert(N,M)
    elif x == 2:                           #ask the user the hour he wish to find the maximum amount for
        print("the current amount of hours entered is {} ".format(d.schedule_pointer-1))
        n = int(input("Enter the hour you wish to find the maximum amount of delivery and the hours the drone operated to achieve it: "))
        d.optimal_for_n(n)
        print()
    elif x == 3:                           #exit the program
        break
    else:
        print("Invalid Input!\n")

