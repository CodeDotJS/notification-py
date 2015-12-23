import notify2
from time import *

notify2.init('')
n = notify2.Notification('Started', ' Damn! You can\'t stop it')
n.show()

while True:
    for i in [('Thought of the Day', 'Code in Node'), ('Code in Python', 'Thug Life'), ('Do not forget to write code in Native JavaScript', 'Fuck Bitches')]:
        n.update(i[0], i[1])
        sleep(15 * 2)
        n.show()
