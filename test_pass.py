from django.contrib.auth.hashers import make_password, check_password

def generate_hash(password):
    """
    Menghasilkan hash menggunakan PBKDF2 dan SHA-256 (Django's make_password).

    Parameters:
        password (str): Kata sandi yang akan dihash.

    Returns:
        str: Nilai hash yang dihasilkan.
    """
    hash_value = make_password(password)
    return hash_value

def verify_password(password, hashed_password):
    """
    Memverifikasi apakah kata sandi cocok dengan hash yang disimpan.

    Parameters:
        password (str): Kata sandi yang akan diverifikasi.
        hashed_password (str): Hash yang disimpan.

    Returns:
        bool: True jika cocok, False jika tidak cocok.
    """
    return check_password(password, hashed_password)

# Contoh penggunaan
password = "uwetn363fd"
hashed_password = generate_hash(password)
print(f"Password: {password}")
print(f"Hashed Password: {hashed_password}")

# Contoh verifikasi
is_verified = verify_password(password, hashed_password)
print(f"Password Verified: {is_verified}")
