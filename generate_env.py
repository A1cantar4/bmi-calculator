import getpass

# To keep everything that is typed secret
secret_key = getpass.getpass("\nSay the SECRET_KEY to your aplication: ")

print("\nSupported Languages: pt, en, es, fr, de, ru, ar, hi, bn, ur, zh")
default_locale = input("\nSay the Language: ").strip().lower() # Strip and Lower to prevent error

# If don't say anything
if not default_locale:
    default_locale = "pt" # Portuguese

env_content = f"""SECRET_KEY={secret_key}

FLASK_ENV=development
FLASK_DEBUG=1

BABEL_DEFAULT_LOCALE={default_locale}
BABEL_SUPPORTED_LOCALES=pt,en,es,fr,de,ru,ar,hi,bn,ur,zh"""

# Using with to avoid errors when closing/saving a file
with open(".env", "w", encoding="utf-8") as generate_env:
    generate_env.write(env_content)
    
print("\nFile '.env' created!")