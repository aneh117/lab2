def display_main_menu():
    print("display_main_menu")

def get_user_input():
    
    user=input('enter an input integer').split(",")
    print (user) 
    #convert str list to float
    listValues = list(map(float,user))
    return listValues
 
def main():
    display_main_menu()
    numlist=get_user_input()
    calc_average_temperature(numlist)
    


def calc_average_temperature(numlist):
    print("calc_average")
    total=sum(numlist)
    avg = total/len(numlist)
    print(avg)
    return avg










if __name__ == "__main__":
    main()
