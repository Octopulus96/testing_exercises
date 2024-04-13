import random
import string


def generate_promocode(promocode_len: int = 8) -> str:
    return "".join(random.choice(string.ascii_uppercase) for _ in range(promocode_len))
