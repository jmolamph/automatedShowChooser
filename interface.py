# jmolamph
import logging
import generator


def start_user_interface():
    """
    Terminal text UI system; grabs user input to interact with the show generator

    Future: open visual UI in new window
    """

    last_show = call_input_loop()
    return last_show


def call_input_loop():
    """
    The main interaction loop between the user and the generator.

    Future: Window UI with form inputs and filters to choose from
    """

    print("Welcome to Automatic Show Chooser!\nDo you want me to choose a show for you? (Y = Yes, N = No)")
    chosen_show = "N/A"
    user_input = input()

    while user_input != "N":
        # if yes, generate a show
        if user_input == "Y":
            chosen_show = generator.run_generator()
            text = "We have chosen {show}.\nDo you want to choose another show? (Y = Yes, N = No)"
            print(text.format(show=chosen_show))
        # if other command, say that is invalid
        else:
            print("Invalid command received; please tell me a valid command: (Y = Yes, N = No)")

        user_input = input()

    # thank the user for using the program
    print("Thanks for using Automatic Show Chooser!")

    return chosen_show
