import string

import Wheels
import Plugboard


# TODO: add logic to handle wheel position configuration
class Enigma:
    def __init__(
        self,
        secret="default",
        wheel_config=[1, 2, 3],
        plugboard_config=["A-Z", "D-G", "V-S"],
    ):
        # make wheels
        self.wheels = Wheels.MakeWheels(secret=secret, numberOfWheels=5)
        # make plugboard and configure it
        plugboard = Plugboard.Plugboard()
        for config in plugboard_config:
            plugboard.make_connection(config)
        self.plugboard = plugboard
        # set wheel configuration
        active_wheels = list(map(lambda wheel: (wheel - 1) % 5, wheel_config))
        self.active_wheels = active_wheels

    def cypher(self, input):
        input = input.upper()
        cypher_text = ""
        alphabet = list(string.ascii_uppercase)
        # convert input to integer
        for character in input:
            if character in alphabet:
                character_int = alphabet.index(character)
                character_int = self.plugboard.flow(character_int)

                spin_next = False
                for index, wheel_index in enumerate(self.active_wheels):
                    wheel = self.wheels[wheel_index]
                    character_int = wheel.flow(character_int)
                    # TODO: Fix bug in wheel spining logic
                    # if index == 0 or spin_next:
                    #     spin_next = wheel.spin()

                # pass through cap
                character_int = (character_int + 13) % 26

                for index, wheel_index in enumerate(self.active_wheels[::-1]):
                    wheel = self.wheels[wheel_index]
                    character_int = wheel.flow(character_int)

                character_int = self.plugboard.flow(character_int)
                cypher_text += alphabet[character_int]

            else:
                cypher_text += character

        # convert output to alphabet
        print(cypher_text)

    def reset_plugboard(self):
        plugboard = Plugboard.Plugboard()
        self.plugboard = plugboard

    def configure_plugboard(self, inputs):
        # parse through inputs and make plugboard configs
        for config in inputs:
            self.plugboard.make_connection(config)

    def remake_wheels(self, secret):
        self.wheels = Wheels.MakeWheels(secret=secret, numberOfWheels=5)

    def configure_wheels(self, configuration):
        active_wheels = map(lambda wheel: (wheel - 1) % 5, configuration)
        self.active_wheels = active_wheels

    def show_config(self):
        print(self.active_wheels)
        self.plugboard.show_connections()


machine = Enigma()
machine.cypher("VFYYB RBWYX")
