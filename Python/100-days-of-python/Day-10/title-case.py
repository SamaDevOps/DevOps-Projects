f_name = input("Enter your first name : ")
s_name = input("Enter your sir name : ")

def title_case(f_name,s_name):
    if f_name == "" or s_name == "":
        return "Enter valid input."
    t_f_name = f_name.title()
    t_s_name = s_name.title()
    return (f"{t_f_name} {t_s_name}")

out = title_case(f_name=f_name, s_name=s_name)

print(out)