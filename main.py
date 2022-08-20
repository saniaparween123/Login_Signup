import json


print("\n                Welcome              \n")
print("............Login / Sign Up..............")
user=int(input("""
        if you wat to login so press 1 ,
        if you wat to Sign Up so press 2,
        press :-   """))
 
 
special="@$&*#_."
dict={}
user_det={}
dict['User_Details']=user_det

if user==2:
    user_name=input("Create your ussername :-- ")
    password=input("Create a strong password :-- ")
    
    upper, lower, special, digit=0, 0, 0,0
    spe="@$&*#_."
    i=0
    while i < len(password):
        
        if (password[i].isupper()):
            upper+=1
        if password[i].islower():
            lower+=1
        if password[i].isdigit():
            digit+=1
        if password[i] in spe:
            special+=1
        i+=1    

    if upper>=1 and lower>=1 and digit>=1 and special>=1 :
        
        c_pass =input("enter confirom password :-- ")
        if c_pass != password :
            print("""
                Both passwords are not same
                ------ Try again later------
                \n""")
        else:
            first=input("Enter Your First Name :-- ")
            last=input("Enter Your Last Name :-- ")
            Gender=input("Male or Female :-- ")
            DOB=input("Your Date-of-Birth:-- ")
            Hobbies=input("Your Hobbies :-- ")
            email=(last+first+"@gmail.com")
            print("\n....Your Email i'd.......\n"+(email).lower())
            
            user_det['User_Name']=user_name
            user_det['Password']=c_pass
            user_det['First_Name']=first
            user_det['Last_Name']=last
            user_det['Gender']=Gender
            user_det['Date-of-Birth']=DOB
            user_det['Hobbies']=Hobbies
            user_det["Email i'd"]=(email).lower()

            a=json.dumps(dict, indent=4)
            file=open("user_details.json","w")
            convert=file.write(a)
            file.close()
            
            print(F"""
                ------ CONGRATULATION {(first)}{(last)} ---------
                    ------YOU ARE SIGN UP SUCCESSFULLY-------
                  """)
        

            
    else:
        print("""
            -----------------Please create a Strong Password---------------------------
            Password should be one upper one lowwer one digit and one special charecter
            -------------------------Try Again Latter----------------------------------
            """)
        
elif user==1:
    username=input("Enter your username :--  ")
    f=open("user_details.json","r")
    read=f.read()
    a=json.loads(read)
 
    c1=0
    c2=0
    for i in a:
        for j in a[i]:
            length=len(a[i])
            if j == "User_Name":
                if username == a[i][j]:
                    pass_=input("Enter your password :-- ")
                    for k in a:
                        for l in a[k]:
                            if l == "Password":
                                if pass_ == a[k][l]:
                                    print("-------------Log In Succesfully------------")
                                    
                                else:
                                    print(pass_,"""
                                    This is incorrect password 
                                    Please Try again latter :)
                                            """)
                else:
                    print(username, """
                    This user name is not founded
                    Please try again latter :)
                    """)
                    
                    
else:
    print("""
             You have only two options
          ......option 1 and option 2......
               please Try again latteroption
          """)
      
