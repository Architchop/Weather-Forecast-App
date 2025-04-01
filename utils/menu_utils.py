class MenuUtils:
    """
    Helper for menu related operations
    """
    
    def show_welcome_message(self):
        print("WELCOME TO WEATHER APP")
    
    def take_city_input(self):
        return self._take_string_input("Enter the city name: ")

    def show_exit_message(self):
        print("Thanks for using the application, see you soon!")
    
    def _take_string_input(self, prompt):
        inp = input(prompt)

        if(inp == ""):
            print("Input cannot be empty!")
            return self._take_string_input(prompt)
        else:
            return inp


    