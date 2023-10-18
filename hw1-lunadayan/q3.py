"""
Question 3
The function total calculates the total amoun that John will have to pa over the life of his mortage. 
The function takes three parameters into account: principal (principal amount of mortage), rate(annual interest for mortage as decimal), and monthly payment (fixed monthly paymet that John in making).

"""

def total(principal, rate, monthly_payment):
    total_payment = 0 #start of the total payment
    
    while principal >0:
        remaining_principal_last = principal
        #calculat remaining principal for this month
        principal = principal *(1+rate/12)-monthly_payment
        total_payment += monthly_payment  #add monthly payment tot he total amount

        if principal > remaining_principal_last:
            #handle overpaymnet in the last month
            total_payment += remaining_principal_last
            break
    return total_payment


def main():
    principal = 30000
    rate = 0.069 #6.9%
    payment = 510.04
    total_payment = round(total(principal, rate, payment),2)
    print(f"the total amount to pay over the life of the mortage is ${total_payment}")


if __name__ == "__main__":
    main()

"""
The total_2 function will take an extra parameter called "extra paymnet". The extra_payment parameter represents the extra payment John will 
be making the first 12 months. The function calculates the total amount paid and the number of months it took John to pay the mortage.
The program will print the total amount paid and the number of months taking into account the extra payment for the first 12 months.
"""
def total_2(principal, rate, monthly_payment, extra_payment):
    total_payment = 0
    months = 0 #count number of months   
    
    while principal > 0:
        remaining_principal_last = principal
        
         #Calculate monthly payment, including the extra payment for the first 12 months
        if months < 12:
            monthly_payment_extra = monthly_payment + extra_payment
        
        else:
            monthly_payment_extra = monthly_payment
    
        principal = principal *(1+rate/12)-monthly_payment_extra
        total_payment += monthly_payment_extra
        months += 1
    
    print(f"The total amount paid is ${round(total_payment,2)} in {months} months")

def main():
    principal = 30000
    rate = 0.069
    monthly_payment = 510.04
    extra_payment = 200
    
    total_2(principal, rate, monthly_payment, extra_payment)

if __name__ == "__main__":
    main()

"""
The function total_3 now has two new parameters called "starting_month" and "ending_month", they represent the starting and ending months for the extra payment.
The funciton calculates the total amount paid, and the number of total months considering the extra paymnet during some periods. 
The funciton will print the total amount paid, the total months, when the extra payment began and ended and for how much that extra payment was. 
"""

def total_3(principal, rate, monthly_payment, extra_payment, starting_month, ending_month):
    total_payment = 0
    months = 0
    
    while principal >0:
        remaining_principal_last = principal

        #Calculate  monthly payment, including the extra payment during the specified months
        if starting_month <= months +1 <= ending_month:
            monthly_payment_extra = monthly_payment + extra_payment
        else:
            monthly_payment_extra = monthly_payment
        
        principal = principal *(1+rate/12)-monthly_payment_extra
        total_payment += monthly_payment_extra
        months += 1
    

    print(f'The total amount paid is ${round(total_payment,2)} in {months} months. From the month {starting_month} until the {ending_month}, there was an extra payment of ${extra_payment}.')

def main():
    principal = 30000
    rate = 0.069
    monthly_payment = 510.04
    extra_payment = 300
    starting_month = 13
    ending_month = 36
    
    total_3(principal, rate, monthly_payment, extra_payment, starting_month, ending_month)

if __name__ == "__main__":
    main()

"""
function total_4 uses the same parameters as total_3, but also prints a table with the month number, 
total amount paid of the mortage, and the remaining principal balance of each month. 
"""

def total_4(principal, rate, monthly_payment, extra_payment, starting_month, ending_month):
    total_payment = 0
    months = 0

    while principal >0:
        remaining_principal_last = principal

        # Calculate the monthly payment, including the extra payment during the specified months
        if starting_month <= months +1 <= ending_month:
            monthly_payment_extra = monthly_payment + extra_payment
        
        else:
            monthly_payment_extra = monthly_payment
        
        principal = principal*(1+rate/12)-monthly_payment_extra
        total_payment+= monthly_payment_extra
        months += 1

        #Print month number, total paid amount, and remaining principal in a x format
        print(f"{months}, $ {round(total_payment,2)}, $ {round(principal,2)}")


def main():
    principal = 30000
    rate = 0.069
    monthly_payment = 510.04
    extra_payment = 300
    starting_month = 13
    ending_month = 36
    
    total_4(principal, rate, monthly_payment, extra_payment, starting_month, ending_month)

if __name__ == "__main__":
    main()