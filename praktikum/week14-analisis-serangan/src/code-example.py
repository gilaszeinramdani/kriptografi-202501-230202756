import hashlib

password = "password123"
hash_md5 = hashlib.md5(password.encode()).hexdigest()

print("Password:", password)
print("MD5 Hash:", hash_md5)