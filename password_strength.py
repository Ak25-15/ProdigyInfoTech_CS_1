import re
def password_strength(password):
    s = 0
    f = []
    if len(password) >= 8:
        s += 1
    else:
        f.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        s += 1
    else:
        f.append("Password should include at least one uppercase letter.")
        
    if re.search(r"[a-z]", password):
        s += 1
    else:
        f.append("Password should include at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        s += 1
    else:
        f.append("Password should include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        s += 1
    else:
        f.append("Password should include at least one special character.")

    if s == 5:
        f.append("Password is very strong.")
    elif s == 4:
        f.append("Password is strong.")
    elif s == 3:
        f.append("Password is moderate.")
    else:
        f.append("Password is weak.")
    return f
password = input("Enter your password: ")
result = password_strength(password)
print("\n".join(result))
