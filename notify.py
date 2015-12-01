import notify2
from time import *

notify2.init('')
n = notify2.Notification('Started', ' Damn! You can\'t stop it')
n.show()

while True:
    for i in [('Thought of the Day', 'Bitch Please'), ('Thought of the Day', 'Thug Life'), ('Thought of the Day', 'Fuck Bitches')]:
        n.update(i[0], i[1])
        sleep(15 * 2)
        n.show()
