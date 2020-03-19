def main():
    global name  #this is variable name
    total_tr = 0  #Ini Variable awal si total_tr
    displayIntroductionMessage() #for display intro
    name = input(" What Is Your Name? (<enter>) to quit : ") #for looping and ask name 
    while name != "": #to repeat the 'name' in while and looping function  
        picture__4r, picture__5r = getInput() #call get_input
        total_transactions = computeValues(picture__4r, picture__5r)#call computevalues
        name = input(" What Is Your Name? (<enter>) to quit : ")
        total_tr = total_tr + total_transactions#total transaction formula
    displayFinalResult(total_tr)#display final result
def displayIntroductionMessage():
 print("=============================================")
 print("    This Program For Assigment Python        ")
 print("=============================================")
     #the above function to display"

def getInput():
    picture__4r, picture__5r = eval(input("Enter number of 4R followed by 5R photo to print (e.g. 10, 0): "))
    "to insert functions and input data how much picture"
    while picture__4r < 0 and picture__5r < 0: #looping if positive
        print("You must enter both positive integers!")
        picture__4r, picture__5r = eval(input("Enter number of 4R followed by 5R photo to print (e.g. 10, 0): "))
    while picture__4r == 0 and picture__5r == 0:#looping if insert 0,0
        print("User will notenter both zeros for the number of photos to be printed.")
        picture__4r, picture__5r = eval(input("Enter number of 4R followed by 5R photo to print (e.g. 10, 0): "))
    while picture__4r < 0:#looping if insert <0
        picture__4r = eval(input("Enter number of 4R photo: ")) 
    while picture__5r < 0:#looping if insert <0
        picture__5r = eval(input("Enter number of 5R photo: "))
    return picture__4r, picture__5r #return 2 variable
 
def computeValues(picture__4r, picture__5r): #this is the calculation formula
    picture__4rberhasil = format(picture__4r * 0.25, '.2f')
    picture__5rberhasil = format(picture__5r * 0.35, '.2f')
    total_all_pic = format(picture__4r * 0.25 + picture__5r * 0.35,'.2f')
    total = picture__4r + picture__5r
    dilevery_cost = 13.55
    if total  > 60: #formula if >60
        total_2 = total - 50
        dilevery_total_1 = int(total / 10 - 5)
        dilevery_cost_2 = dilevery_total_1 * 1.75
        total_transactions = (picture__4r * 0.25) + (picture__5r * 0.35) + dilevery_cost + dilevery_cost_2
    elif total  > 50: #formula if >50
        total_2 = total - 50
        dilevery_total_1 = 1
        dilevery_cost_2 = dilevery_total_1 * 1.75
        total_transactions = (picture__4r * 0.25) + (picture__5r * 0.35) + dilevery_cost + dilevery_cost_2
    
    elif total <= 50: #formula if <50
        total_2 = total - 50
        dilevery_total_1 = int(total_2 / 10)
        dilevery_cost_2 = dilevery_total_1 * 1.75
        total_transactions = (picture__4r * 0.25) + (picture__5r * 0.35) + dilevery_cost
    
    printComputedValues(name, picture__4r, picture__5r, picture__4rberhasil, picture__5rberhasil, total_all_pic, total, total_2, dilevery_cost, dilevery_total_1, dilevery_cost_2, total_transactions)
        #The function above to reset parameters then calls the function
    return total_transactions

def printComputedValues(name, picture__4r, picture__5r, picture__4rberhasil, picture__5rberhasil, total_all_pic, total, total_2, dilevery_cost, dilevery_total_1, dilevery_cost_2, total_transactions):
   
    print("Bill for ", name)
    print("---------------------------------------------")
    if total < 100: #formula if < 100
        print(total,"photos",format(total_all_pic, ">35"))
        
    elif total > 100: #formula if > 100
        print(total,"photos",format(total_all_pic, ">33"))
        print("-",picture__4r," 4R photos @$0.25",format(picture__4rberhasil, ">12")) 
        print("-",picture__5r," 5R photos @$0.35",format(picture__5rberhasil, ">12"))
    
    if total <= 50: #formula if <=50
        print("Delivery cost",format(dilevery_cost, ">30"))
        print("~ First 50 or part of: ",format(dilevery_cost,">10"))
        
    elif total > 50: #formula if > 50
        print("\nDelivery cost",format(dilevery_cost + dilevery_cost_2, ">31"'.2f'))
        print("~ First 50 or part of:         ",dilevery_cost)
        print("~",dilevery_total_1," x 10 or part of @$1.75 ","{:>7}".format(dilevery_cost_2, '.2f'))
    
    print("---------------------------------------------")
    print("Total $",format(total_transactions, ">37"'.2f'))
    print("=============================================")

 
def displayFinalResult(total_tr):
    if total_tr <= 0:
        print("\nNo Transactions For The Today.")
        #for display if you not input some transactions 'enter'
    else:
        print("Total collection: $", format(total_tr, '.2f'))
        #displayFinalResult(total_tr)
main()
        #close the program