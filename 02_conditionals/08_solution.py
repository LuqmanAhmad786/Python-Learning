password = "amazsdajdljaklsjdl"

if len(password) < 6:
  status = "Weak"
elif len(password) <= 10:
  status = "Medium"
else:
  status = "Strong"

print(status)