from src.Enigma import Enigma

print("---------Enigmatic----------")
run_enigma = 1
while run_enigma == 1:
    print("Welcome to enigmatic")
    user_response = -1
    while not -1 < user_response < 2:
        print("\n\n==OPTIONS==")
        print("0: Exit Enigmatic")
        print("1: Create Enigma Machine")
        try:
            user_response = int(input())
        except ValueError:
            print("Only numbers 1 and 0 are valid inputs")

    if user_response == 0:
        break

    user_secret = ""
    while user_secret == "":
        print(
            "\n\nEnter a secret text. This will be used to build your enigma machine!"
        )
        user_secret = input()

    wheel_configuration = []
    user_response = -1
    while len(wheel_configuration) < 5 and user_response != 1:
        print(
            "\n\nConfigure wheel positions. Enter numbers from 1 to 5, or enter Y to save config."
        )
        print("Current config " + str(wheel_configuration))
        raw_input = input()
        try:
            wheel_choice = int(raw_input)
            if not 1 <= wheel_choice <= 5:
                print("Only choices between 1 and 5 are valid")
            elif wheel_choice in wheel_configuration:
                print("Wheel " + str(wheel_choice) + " has already been selected")
            else:
                wheel_configuration.append(wheel_choice)
        except ValueError as e:
            if raw_input.upper() == "Y":
                user_response = 1
            else:
                print("Invalid input, only numbers between 1 and 5 are valid")

    plugboard_configuration = []
    user_response = -1
    while len(plugboard_configuration) < 12 and user_response != 1:
        print(
            "\n\nConfigure Plugboard matching. Enter alphabet pairs like A-Z or K-L, or enter Y to save config."
        )
        print("Current config " + str(plugboard_configuration))
        raw_input = input()
        if len(raw_input) == 3 and raw_input.upper() not in plugboard_configuration:
            wheel_choice = raw_input.upper()
            plugboard_configuration.append(wheel_choice)
        elif raw_input.upper() == "Y":
            user_response = 1
        else:
            print(
                "Invalid input, match must be between only two characters eg: Q-P and not repeated!"
            )

    # TODO add logic to configure wheel positions

    machine = Enigma(
        secret=user_secret,
        wheel_config=wheel_configuration,
        plugboard_config=plugboard_configuration,
    )

    user_response = -1
    while user_response in [1, 2, -1]:
        print("\n==OPTION==")
        print("1: Make cyper text")
        print("2: Reset enigma machine")
        print("3: Exit")

        try:
            user_response = int(input())
            if user_response == 1:
                print("Enter a text to encypher:")
                machine.cypher(input())
            elif user_response == 2:
                machine = machine = Enigma(
                    secret=user_secret,
                    wheel_config=wheel_configuration,
                    plugboard_config=plugboard_configuration,
                )
            else:
                break
        except ValueError as e:
            print("Invalid input")

    # exit enigma loop
    i = -1
    while not -1 < i < 2:
        print("\n==OPTIONS==")
        print("0: Exit Enigmatic")
        print("1: Re run Enigmatic")
        try:
            i = int(input())
        except ValueError:
            print("Only numbers 1 and 0 are valid inputs")

    run_enigma = i
