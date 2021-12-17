import hashlib
import string


class Wheel:
    def __init__(self, name="", circuit={}, position=0, notch_index=0):
        self.name = name
        self.circuit = circuit
        self.postion = position
        self.notch = notch_index

    def flow(self, value):
        return self.circuit[value]

    def spin(self):
        self.position = (self.position + 1) % 26
        # return True if at notch
        return self.postion == self.notch

    def set_position(self, new_position):
        self.postion = new_position % 26

    def __str__(self):
        return self.name


def MakeWheels(secret, numberOfWheels=5):
    # deterministically make a set of wheels from a secret text
    wheels = []

    for wheel_count in range(1, numberOfWheels + 1):
        secret = secret * wheel_count
        hashed_secret = hashlib.sha384(secret.encode())
        dec = int(hashed_secret.hexdigest(), 16)
        hash_string = str(dec)
        notch_index = dec % 26
        circuit = {}
        for index, alphabet in enumerate(string.ascii_lowercase):
            if alphabet not in circuit:
                index_key = int(hash_string[(index * 2) : (index * 2 + 2)])
                maps_to = string.ascii_lowercase[index_key % 26]
                circuit[alphabet] = maps_to
                circuit[maps_to] = alphabet

        wheel = Wheel(name=str(wheel_count), circuit=circuit, notch_index=notch_index)
        wheels.append(wheel)

    return wheels
