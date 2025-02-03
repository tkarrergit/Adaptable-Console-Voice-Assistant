from hugchat import hugchat
from hugchat.login import Login
import funktions
import variables_for_all

debug_mode = variables_for_all.debug_mode
"""
class hugchat:
    def __init__(self, email, passwd, chatbot, query_result_no_stream, query_result_web, conversation_list,  ):
        self.email = email
        self.passwd = passwd
        self.chatbot = chatbot
        self.query_result_no_stream = query_result_no_stream
        self.query_result_web = query_result_web
        self.conversation_list = conversation_list"""
        
def initialize_hugchat(email, passwd, debug_mode):    
    try:
        # Cookies im lokalen Verzeichnis speichern
        cookie_path_dir = funktions.resource_path("./cookies_snapshot")            
        # Einloggen bei Huggingface und Autorisieren von HugChat
        sign = Login(email, passwd)
        cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
        
        # Create your ChatBot
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

        return chatbot
    except Exception as e:
        if debug_mode == True: print(f"Fehler bei der Initialisierung von Huggingface: {e}")
        return None
    
#chatbot = initialize_hugchat(hugchat.email, hugchat.passwd)

def no_stream_chat(chatbot, user_input, conversation):
    # Non stream response
    query_result_no_stream = chatbot.chat(user_input, conversation)
    print(query_result_no_stream) # or query_result.text or query_result["text"]

def stream_chat(chatbot, user_input):
    # Stream response
    for resp in chatbot.query(
        user_input,
        stream=True
    ):
        print(resp)

def web_chat(chatbot, user_input):
    # Web search (new feature)
    query_result_web = chatbot.query(user_input, web_search=True)
    print(query_result_web)
    for source in query_result_web.web_search_sources:
        print(source.link)
        print(source.title)
        print(source.hostname)

def hugchat_new_conversation(chatbot):
    # Create a new conversation
    chatbot.new_conversation(switch_to = True) # switch to the new conversation
    
    print("New Conversation with Hugchat")

def all_conversation_list(chatbot):
    # Get conversations on the server that are not from the current session (all your conversations in huggingchat)
    conversation_list = chatbot.get_remote_conversations(replace_conversation_list=True)
    print(conversation_list)

def local_conversation_list(chatbot):
    # Get conversation list(local)
    conversation_list = chatbot.get_conversation_list()   
    print(conversation_list)

def get_hugchat_models(chatbot):
    # Get the available models (not hardcore)
    models = chatbot.get_available_llm_models()
    
    print(models)

def switch_to_hugchat_model(chatbot, index):
    # Switch model with given index
    chatbot.switch_llm(index) # Switch to the first model index = 0 # Switch to the second model Index = 1 usw.
    #print("Switched to Model mit Index= " + index)

def get_info_current_conversation(chatbot):
    # Get information about the current conversation
    info = chatbot.get_conversation_info()
    print(info.id, info.title, info.model, info.system_prompt, info.history)

def hugchat_assistent_list(chatbot):
    assistant_list = chatbot.get_assistant_list_by_page(page=0)
    print(assistant_list)

def new_conversation_assistent(chatbot, assistent_name):
    # Assistant
    assistant = chatbot.search_assistant(assistant_name=assistent_name) # assistant name list in https://huggingface.co/chat/assistants 
    print(assistant)       
    chatbot.new_conversation(assistant=assistant, switch_to=True) # create a new conversation with assistant
    print("New Conversation with Assistent: " + assistent_name)

def delete_all_hugchat_conversations(chatbot):
    input= input("Do you realy want to delete all coversations?Y/N")
    if input == "Y":
        input= input("Do you reeeeaaaaaaaly want to delete all coversations?yes/No")
        if input == "Yes":
            # [DANGER] Delete all the conversations for the logged in user
            chatbot.delete_all_conversations()
            print("All Conversation deleted")
        else:
            pass
    else:
        print("No Conversation deleted")


#Model Index = 0 ist CohereForAI/c4ai-command-r-plus
#Model Index = 1 ist meta-llama/Meta-Llama-3-70B-Instruct
#Model Index = 2 ist HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1
#Model Index = 3 ist mistralai/Mixtral-8x7B-Instruct-v0.1
#Model Index = 4 ist NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO
#Model Index = 5 ist google/gemma-1.1-7b-it
#Model Index = 6 ist mistralai/Mistral-7B-Instruct-v0.2
#Model Index = 7 ist microsoft/Phi-3-mini-4k-instruct

#hugchat_assistent_list(chatbot)
#get_hugchat_models(chatbot)
#input=input("Welches Model?")

def hugchat_assistent(user_input):
    Scrum_Master_Trainer_id: str = "6634c38f324a395ecb8af6fb"
    Scrum_Master_Meeting_Moderations_Trainer_id: str = "6634a1e513c8af7ae5965382"
    Coaching_Trainer_id: str = "663653221ed733523d962834"

    chatbot = initialize_hugchat("huggchat@proton.de", "Huggchat55%", debug_mode)    

    tomconversation = chatbot.new_conversation(assistant=Scrum_Master_Trainer_id)

    
    ausgabe = chatbot.chat(user_input, conversation = tomconversation)
    print(ausgabe)

import speech_recognition as sr
import time

def sr_speech_to_text():
    # Erstelle ein Recognizer-Objekt
    r = sr.Recognizer()
    text_flag = False
    while True:
        
        if text_flag == False:
            # Nehme Audio vom Mikrofon auf
            with sr.Microphone() as source:
                print("Sprich etwas:")                 
                start_time = time.time()
                try:
                    audio = r.listen(source, timeout=10, phrase_time_limit=10)
                    print("audio")
                except sr.WaitTimeoutError:
                    print("Zeitüberschreitung bei der Audioaufnahme.")
                    continue
                except:
                    print("Unerwarteter Fehler bei der Audioaufnahme.")
                    continue
                

            # Erkenne Sprache mithilfe von Google Speech Recognition
            try:
                print("vor text")
                text = r.recognize_google(audio, language="de-DE")
                print("Du hast gesagt: " + text)
                if text:
                    text_flag = True
                    return text
            except sr.UnknownValueError:
                print("Tut mir leid, ich habe das nicht verstanden.")
            except sr.RequestError as e:
                print("Fehler bei der Spracherkennung; {0}".format(e))
        if text_flag == True:
            break

while True:
    user_input = sr_speech_to_text()
    hugchat_assistent(user_input)