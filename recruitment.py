# Rana Bakri
# 27/9/2022
# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
def get_skills():
    skills =["java","python","c++"]
    # new_skill = input("Please enter a skill name:\n")
    # skills.append(new_skill)
    
    return skills

 


# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
     
       print("Skills:")
       for count, skills in enumerate(skills, start=1):
         
          print(count, skills)
         
    


# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
   
   show_skills(skills)
   skill_one = int(input("Enter the number of skill you know"))
   skill_two = int(input("Enter the number of skill you know"))
   skill_one = skills[skill_one-1]
   skill_two =skills[skill_two-1] 
   user_skills = [skill_one,skill_two]
   return user_skills
#    print(user_skills)
 




# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    cv = {}
    cv["name"]=input("enter your name")
    cv["age"]=int(input("Enter your age"))
    cv["experience"]=int(input("How many years of experience do you have?"))
    cv["skills"]=get_user_skills(skills)
    print(cv)

    


# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    if 25 <=cv["age"]<=40 and cv["experience"]>=3 and   desired_skill in cv["skills"]:
        return True
    else:
        return False    


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
     #print(get_skills())

     
#user_skills=(get_user_skills(get_skills()))
 print ("Welcome to the special recruitment program, please answer the following questions:")
 skills = get_skills()
 user_cv = get_user_cv(skills)
 is_accepted = check_acceptance(user_cv["skills"], "java")
 if is_accepted:
    print ("you have been accepted")
 else:
    print("sorry not accepted")



if __name__ == "__main__":
    main()
