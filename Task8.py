# task_8
class Messagetask8:
    def __init__(self, id=10000000, subject='Title', text='Sample Text ', created_at='11.11.11',
                 support_group='sample text'):
        self.id = id
        self.subject = subject
        self.text = text
        self.created_at = created_at
        self.support_group = support_group
message = Messagetask8(5775575, 'Order Telephone', 'The order is: SE ', 'Created at://///////',
               'Account: Kim2030 \nTech: Eldorado \nBilling: 5169147129584558 \nOrder: 28048')
file = open('testfile.txt', 'w')
file.write(str(message.id))
file.write(message.subject)
file.write(message.text)
file.write(message.created_at)
file.write(message.support_group)

file.close()
