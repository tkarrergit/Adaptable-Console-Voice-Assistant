

API_Token = "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"

from hugchat.hugchat import ChatBot
from hugchat.login import Login
import re
import sys

def huggingface_chatbot():    
    try:
        # Einloggen bei Huggingface und Autorisieren von HugChat
        sign = Login("sandburg.registrierung@mail.de", "Strand42!")
        cookies = sign.login()
        #if debug_mode == True: print(cookies)
        # Cookies im lokalen Verzeichnis speichern
        cookie_path_dir = "./cookies_snapshot"
        sign.saveCookiesToDir(cookie_path_dir)
        # Neue HugChat-Verbindung starten
        chatbot = ChatBot(cookies=cookies)
        chatbot.switch_llm(6)
        return chatbot
    except Exception as e:
        print(f"Fehler bei der Initialisierung von Huggingface: {e}")
        return None

def initialize_hugchat_conversation_and_chatbot():
        try:
            chatbot = huggingface_chatbot()
            tomconversation = chatbot.new_conversation() 
            return tomconversation, chatbot
        except Exception as e:
             print(f"Fehler : {e}")

def sprich_Hugchat_stream_chat_satz(chatbot, user_input, conversation):
    #Spricht jeden vollständigen Satz der Antwort einen nach dem anderen.
    # Initialisiere eine leere Zeichenkette für den zusammenhängenden Text    
    full_response = ""
    current_sentence = ""
    try: #chatbot.chat for websearch
        for resp in chatbot._stream_query(

            user_input,                 
            conversation = conversation,
            web_search = True,
        ):  
            if resp:
                #print("YES")
                #print(resp)
                pass
            # Überprüfe, ob resp nicht None ist, bevor auf resp['type'] zugegriffen wird
            if resp is not None and resp.get('type') == 'stream':
                token = resp['token']
                current_sentence += token
                try:    
                    # Check if the current token ends with a sentence-ending punctuation
                    if re.search(r'[.!?]', token):
                        
                        # Print and speak the complete sentence
                        cleaned_sentence = re.sub(r'\x00', '', current_sentence)  # Remove NULL characters
                        #print(cleaned_sentence, end=" ")                
                        sys.stdout.flush()
                        full_response += cleaned_sentence
                        if True == True:                                                                                
                
                            print(f"{cleaned_sentence}\n")
                          
                        current_sentence = ""
                except Exception as e:
                    print(f"sprich_stream_chat_satz ERROR_1: {e}")
                    
    except Exception as e:
                    print(f"sprich_stream_chat_satz ERROR_2: {e}")             
                            
conversation, chatbot = initialize_hugchat_conversation_and_chatbot()
chatbot.switch_llm(6)
sprich_Hugchat_stream_chat_satz(chatbot, "Wie heißt dein llm Model und wie wird das Wetter morgen in Köln?", conversation)