
#One of the applications we will use in this notebook is Random User Generator. RandomUser is an open-source, free API providing developers with randomly generated users to be used as placeholders for testing purposes. This makes the tool similar to Lorem Ipsum, but is a placeholder for people instead of text. The API can return multiple results, as well as specify generated user details such as gender, email, image, username, address, title, first and last name, and more. More information on RandomUser can be found here.

import sys
sys.stdout.reconfigure(encoding='utf-8')

from randomuser import RandomUser
import pandas as pd

#create an instance /object of the RandomUser class
r = RandomUser()
random_users_list = r.generate_users(10)#generate a list of 10 random users and store it in the variable random_users_list
print(random_users_list)

name = r.get_full_name()#get the full name of a random user and store it in the variable name
print(name)

for user in random_users_list:
    print (user.get_full_name()," ",user.get_email())
    
for user in random_users_list:
    print (user.get_picture())  
    
    
#getting a dataframe from the random users list
def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     
df = get_users()
print(df)      
