import time
import datetime
#Skapar en tidsloggerfunktion
def logger(function_to_pass):
    """Loggingfunktion som kommer att ta in en annan funktion som inargument och utföra tidsloggning."""

    def wrapping_function(*args, **kwargs):
        """Wrappingfunktion som loggar tidsinformation, inargument, resultat  och gör function call."""
        time.sleep(0.1)
        value = function_to_pass(*args, **kwargs)

        with open("logs.txt","a") as f:
            f.write("Cool machine learning process finalized at " + str(datetime.datetime.now()) +
             " with arguments " + ", ".join([str(arg) for arg in args])+ " and results " + str(value) + ". \n")

        return value

    return wrapping_function

#Markerar här att vi ska skicka in detta till logger
@logger
def scientific_function(base: int, exponent: float) -> float:
    return(base**exponent)

for n in range(10):
    scientific_function(n, 2.5)

#Ha det klart för er varför nedanstående inte fungerar
#wrapper_value = wrapping_function(2, 2)