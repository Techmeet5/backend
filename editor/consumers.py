# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import requests


class ChatConsumer(WebsocketConsumer):

    write_permission = False
    language         = 'python'

    # Defaults
    default_code_python = """
# Python Program
# Write Python 3 code in this online editor and run it.
print('Hello world')  """

    default_code_cpp = """
// Your First C++ Program

#include <iostream>

int main() {
    std::cout << "Hello World!";
    return 0;
} """

    default_code_java = """
// Java Program
class Simple{
    public static void main(String args[]){
    System.out.println("Hello Java");
    }
} """

    current_code = ""

    compiled_output = ""

    group_members = 0

    room_members = []



    def connect(self):
        
        
        print("\n\n New Connection")
        #self.room_name = self.scope['url_route']['kwargs']['room_name']
        
        self.id = "user"
        self.room_name       = 'users'
        self.room_group_name = 'chat_%s' % self.room_name

        print(" room_name -> ",self.room_name)
        print(" room_group_name -> ",self.room_group_name)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        ChatConsumer.room_members.append(self.id)
        self.accept()
        print(" Connection Accepted")
        print(" Current Room Members -> ",ChatConsumer.room_members)
        self.default_code()



    def default_code(self):
        ChatConsumer.group_members += 1

        if ChatConsumer.group_members==1:
            self.send(text_data=json.dumps({
                'code': ChatConsumer.default_code_python,
                'lang': ChatConsumer.language,
                'output': ChatConsumer.compiled_output,
                'perm': True
            }))
        else:
            self.send(text_data=json.dumps({
                'code': ChatConsumer.default_code_python,
                'lang': ChatConsumer.language,
                'output': ChatConsumer.compiled_output,
                'perm': False
            }))
        
        print(" Default Data sent")
        


    def disconnect(self, close_code):
        # Leave room group

        print("Disconecting ...............!!!!!!")
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        print("\n\n\n\n",text_data_json)
        

        # Store Code on every change
        if text_data_json['lang']=='null':
            ChatConsumer.current_code = text_data_json['code']
            print(" current_code changed")
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_broadcast_code',
                    'broadcast_code': ChatConsumer.current_code
                }
            )
        
        
        #Compile code
        elif text_data_json['lang']=='compile':

            url = 'https://api.jdoodle.com/v1/execute'

            lang_map = {
                "cpp": ["cpp", ChatConsumer.default_code_cpp],
                "java": ["java", ChatConsumer.default_code_java],
                "python3": ["python", ChatConsumer.default_code_python]
            }

            if ChatConsumer.language=="python":
                modified_language = "python3"
            else:
                modified_language = ChatConsumer.Language

            myobj = { "script"      : ChatConsumer.current_code,
                      "language"    : modified_language,
                      "versionIndex": "0",
                      "clientId"    : "4ecbe1de83c55b2ed7dd221760779ef3",
                      "clientSecret":"89da25df05d144bb14817b939889f8577732bb3cd90da121b32fdce5e8dedc09"
                    }

            
            head = {  "Content-Type": "application/json" }

            x = requests.post(url, headers=head , json=myobj)

            x = x.json()
        
            if "error" in x.keys():
                
                print(x['error'])
                print(x['statusCode'])

                #result = x['error'] + x['statusCode']
                #print(" Error recieved -> ",result)

                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'chat_broadcast_output',
                        'broadcast_code': result,
                        'output': False
                    }
                )
                #return Response(result)

            else:
                print(" output -> ",x['output'])
                result = x['output'] 
                print(" Successful output recieved")

                ChatConsumer.output = result
                
                async_to_sync(self.channel_layer.group_send)(
                        self.room_group_name,
                        {
                            'type': 'chat_broadcast_output',
                            'broadcast_code': ChatConsumer.output,
                            'output': True
                        }
                    )

                #return Response(result)








        #Change language
        elif text_data_json['lang']!=ChatConsumer.language:

            ChatConsumer.language = text_data_json['lang']

            print(" Language changed to - ",ChatConsumer.language)
            
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_lang',
                    'message': ChatConsumer.language
                }
            )


############################################### 

    # Events
    
    #Normal code transfer
    def chat_broadcast_output(self,event):
        broadcast_code = event['broadcast_code']

        if event['output'] == True:

            self.send(text_data=json.dumps({
                'code': ChatConsumer.current_code,
                'lang': ChatConsumer.language,
                'output': ChatConsumer.output,
            }))
            print(" Output Broadcasted to other users")
        
        elif event['output'] == False:

            self.send(text_data=json.dumps({
                'code': ChatConsumer.current_code,
                'lang': ChatConsumer.language,
                'output': result,
            }))
            print(" Error Broadcasted to other users")


    #Normal code transfer
    def chat_broadcast_code(self,event):
        broadcast_code = event['broadcast_code']


        self.send(text_data=json.dumps({
            'code': ChatConsumer.current_code,
            'lang': ChatConsumer.language
        }))
        print(" Broadcasted to other users")


    # Receive message from room group
    def chat_lang(self, event):
        message = event['message']

        print(" Recieved -",message)
        if ChatConsumer.language=="python":
            ChatConsumer.current_code=ChatConsumer.default_code_python
        elif ChatConsumer.language=="java":
            ChatConsumer.current_code=ChatConsumer.default_code_java
        elif ChatConsumer.language=="cpp":
            ChatConsumer.current_code=ChatConsumer.default_code_cpp 

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'code': ChatConsumer.current_code,
            'lang': ChatConsumer.language
        }))
        print(" new lang and code sent")