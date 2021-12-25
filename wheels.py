import hashlib


class Wheel:
    def __init__(self, name="", circuit={}, position=0, notch_index=0):
        self.name = name
        self.circuit = circuit
        self.position = position
        self.notch = notch_index

    def flow(self, value):
        return self.circuit[value + self.position % 26]

    def spin(self):
        self.position = (self.position + 1) % 26
        # return True if at notch
        return self.position == self.notch

    def set_position(self, new_position):
        self.position = new_position % 26

    def __str__(self):
        return self.name


def MakeWheels(secret, numberOfWheels=5):
    # deterministically make a set of wheels based on a secret text
    wheels = []

    for wheel_count in range(1, numberOfWheels + 1):
        secret = secret * wheel_count
        hashed_secret = hashlib.sha384(secret.encode())
        dec = int(hashed_secret.hexdigest(), 16)
        hash_string = str(dec)
        notch_index = dec % 26
        circuit = {}
        indices = list(range(26))
        for index in range(26):
            if index not in circuit:
                this_index = indices.pop(0)
                index_key = int(hash_string[(index * 2) : (index * 2 + 2)]) % len(
                    indices
                )
                maps_to = indices.pop(index_key)
                circuit[this_index] = maps_to
                circuit[maps_to] = this_index

        wheel = Wheel(name=str(wheel_count), circuit=circuit, notch_index=notch_index)
        wheels.append(wheel)

    return wheels
