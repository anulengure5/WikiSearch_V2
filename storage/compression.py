def delta_encode(numbers):
    if not numbers:
        return []

    encoded = [numbers[0]]

    for i in range(1, len(numbers)):
        encoded.append(numbers[i] - numbers[i - 1])

    return encoded

def delta_decode(numbers):
    if not numbers:
        return []

    decoded = [numbers[0]]

    for i in range(1, len(numbers)):
        decoded.append(decoded[-1] + numbers[i])

    return decoded


def vb_encode_number(n):
    bytes_list = []

    while True:
        bytes_list.insert(0, n % 128)

        if n < 128:
            break

        n //= 128

    bytes_list[-1] += 128
    return bytes_list

def vb_encode(numbers):
    bytestream = []

    for n in numbers:
        bytestream.extend(vb_encode_number(n))

    return bytes(bytestream)

def vb_decode(bytestream):
    numbers = []
    n = 0

    for byte in bytestream:
        if byte < 128:
            n = 128 * n + byte
        else:
            n = 128 * n + (byte - 128)
            numbers.append(n)
            n = 0

    return numbers


