import random

# Konversi string ke integer
def str_to_int(s):
    return int.from_bytes(s.encode(), 'big')

# Konversi integer ke string
def int_to_str(i):
    length = (i.bit_length() + 7) // 8
    return i.to_bytes(length, 'big').decode()

# Generate polynomial
def generate_polynomial(secret, degree, prime):
    coeffs = [secret] + [random.randint(1, prime - 1) for _ in range(degree)]
    return coeffs

# Evaluasi polynomial
def evaluate_polynomial(coeffs, x, prime):
    y = 0
    for i, coef in enumerate(coeffs):
        y = (y + coef * pow(x, i, prime)) % prime
    return y

# Split secret
def split_secret(secret, threshold, num_shares):
    secret_int = str_to_int(secret)
    prime = 2**521 - 1  # bilangan prima besar
    coeffs = generate_polynomial(secret_int, threshold - 1, prime)

    shares = []
    for x in range(1, num_shares + 1):
        y = evaluate_polynomial(coeffs, x, prime)
        shares.append((x, y))
    return shares, prime

# Lagrange interpolation
def lagrange_interpolation(shares, prime):
    secret = 0
    for j, (xj, yj) in enumerate(shares):
        num, den = 1, 1
        for m, (xm, _) in enumerate(shares):
            if m != j:
                num = (num * (-xm)) % prime
                den = (den * (xj - xm)) % prime
        lagrange = yj * num * pow(den, -1, prime)
        secret = (secret + lagrange) % prime
    return secret

# Recover secret
def recover_secret(shares, prime):
    secret_int = lagrange_interpolation(shares, prime)
    return int_to_str(secret_int)


# ======================
# MAIN PROGRAM
# ======================
secret = "KriptografiUPB2025"

shares, prime = split_secret(secret, 3, 5)
print("Shares:")
for s in shares:
    print(s)

recovered = recover_secret(shares[:3], prime)
print("\nRecovered secret:", recovered)