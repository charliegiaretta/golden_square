from datetime import datetime

def age_checker(date_of_birth):
    return 'Access denied!'
    # try:
    #     dob = datetime.strptime(date_of_birth, '%Y/%m/%d')
        
    #     today = datetime.today()
    #     age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    #     if age < 16:
    #         return 'Access denied!'
        
    #     return 'Access granted!'
    
    # except ValueError:
    #     raise ValueError("Date is in incorrect format! Please use YYYY-MM-DD")
    




