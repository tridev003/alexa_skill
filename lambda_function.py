import logging
import ask_sdk_core.utils as ask_utils
import random
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
hou_num=[]
housenumber =0
condn = 0
d={2:"Me and you luckey number 2",3:"Happy family of 3 number is 3",5:"fingers in your hand is 5 next number is 5",7:"God’s in Heaven Lucky number Seven",11:"two beautiful legs like 11 next number is 11",13:"13 reasons why you played this game it number 13",17:"the sum of first four prime numbers is 17 next number is 17",19:"Last of the teens is 19",23:"20 + 3 23",29:"Gin & Wine next number is 29",31:"Time for fun number 31",37:"Lime and leamons 37",41:"Kiss and run 41",43:"Climb a tree 43",47:"Year of Independence 47",53:"Stuck in a tree 53",59:"just retired 59",61:"bakers bun 61",67:"Made in heaven 67",71:"Bang the drum 71",73:"Under the tree 73",79:"7 plus 9 79",83:"India wins Cricket World Cup in 83",89:"Nearly there 89"}

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "yay,yay!! lets play housie. shall we start the game? or do you want to know the rules?  "
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )    
    
class RulesIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RulesIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The rules are self made not for you of the game are very simple, all players must purchase a ticket to enter the game. The objective of the game is to mark all the numbers found in the ticket. The player who first marks all the numbers in a winning pattern. And to win the call, after checking his ticket, he is declared as the winner of that pattern and verified it with the numbers drawn."
        reprompt_text="should i start the game now?"
        return (
            handler_input.response_builder.speak(speak_output).ask(reprompt_text).response
        )

class GameStartIntentHandler(AbstractRequestHandler):
    """Handler for  Start Game Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GameStartIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "are you guys ready for the fun?"

        return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
        )

class NumSpeakIntentHandler(AbstractRequestHandler):
    
    """Handler for  Start Game Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NumSpeakIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        num = random.randint(1, 90)
        if num not in hou_num:
            hou_num.append(num)
            if num in d.keys():
                speak_output = d[num]
            elif(num in range(1,11)):
                speak_output="you lucky number is "+" "+str(num)
                return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response )
            else:
                speak_output="your number is "+" "+str(num)
                return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response)
        else:
            sb.add_request_handler(NumSpeakIntentHandler())

        '''speak_output="23"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )'''  
class PreviousIntentHandler(AbstractRequestHandler):
    """Handler for  Start Game Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PreviousIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = str(hou_num[len(hou_num)-2])

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        ) 
class RepeatIntentHandler(AbstractRequestHandler):
    """Handler for  Start Game Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RepeatIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = str(hou_num[len(hou_num)-1])

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        ) 
'''class HousefullIntentHandler(AbstractRequestHandler):
    """handler for checking game intent"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HousefullIntent")(handler_input)
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "are you sure?if yes then please tell me all your numbers else we can resume our game. You will be disqualified if your numbers didn't match."
        housenumber=15
        return ( 
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
            )'''
class CheckIntentHandler(AbstractRequestHandler):
    """handler for checking game intent"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CheckIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        number = slots["hosi"].value
        '''if housenumber == 15:
            if int(number) in hou_num:
                speak_output = "no is matched."
                condn=condn+1
                if condn == 15:
                    speak_output = "all numbers are matched. we got our winner. & the winner is"
                else:
                    housenumber = 0
                    speak_output = "number did not matced.you are disqualified from this game"
        else:'''
        if int(number) in hou_num:
            speak_output = "yes. i have said {}".format(number)
        else:
            speak_output = "noo. i didn't said this" 
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
            )
'''class NameIntentHandler(AbstractRequestHandler):
    """handler for checking game intent"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NameIntent")(handler_input)
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "now tell me your numbers one by one"
        housenumber=15
        slots1 = handler_input.request_envelope.request.intent.slots
        fname = slots1["firstname"].value
        slots2 = handler_input.request_envelope.request.intent.slots
        lname = slots2["lastname"].value
        return ( 
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
            )'''
class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for skill session end."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")
        print("Session ended with reason: {}".format(
            handler_input.request_envelope))
        return handler_input.response_builder.response

class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Game had finished. it was a very amazing game. hope you enjoyed it. if you like this skill please rate it at amazon store and shared with your families and friends.thank you.good bye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        ) 

class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(NumSpeakIntentHandler())
sb.add_request_handler(CheckIntentHandler())
sb.add_request_handler(PreviousIntentHandler())
sb.add_request_handler(RepeatIntentHandler())
sb.add_request_handler(GameStartIntentHandler())
sb.add_request_handler(RulesIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
