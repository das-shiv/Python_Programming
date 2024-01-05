# Modules = Modules are collection of functions, classes that can be imported into different programs.
# help("modules") =  list all the available python modules
import messages

messages.hello()
messages.bye()
'''
import messages as msg
msg.hello()
msg.bye()
'''
'''
from messages import hello,bye
#from messages import * #imports all the functions in the module
hello()
bye()
'''


