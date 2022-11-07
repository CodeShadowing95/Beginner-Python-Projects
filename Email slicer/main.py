import re

def validate_email(email):
    email = email.strip()
    p = r"\b[A-Za-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Z|a-z]{2,}\b"
    if(re.fullmatch(p, email)):
        return True
    return False


def email_slice(email):
    i = email.index('@')
    username = email[:i]
    domain_name = email[i+1:]
    return (''.join(username), ''.join(domain_name))


if __name__ == "__main__":
    t = input("Enter your email address: ")
    while not validate_email(t):
        t = input("Enter a correct email address: ")
    params = email_slice(t)
    print(f"The username is {params[0]} and the domain name is {params[1]}")
    
    # Sendmail functionality