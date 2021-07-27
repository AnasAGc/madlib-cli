import re

# words=["adjective","adjective","first name", "past tens verb","first name","adjective","adjective","plural noun","large anamile","small anamile","girl name","adjective","plural noun","adjective","plural noun","Number 1-50","first name","number","plural noun","number","plural noun"]
# print("wlcome to midlib game")

# answer=[]
# def user_anwser():
#     for i in words:
#         answer.append(input(f"enter {i} "))
 


  


def read_template(file_path:str)->str:
 """
This function Taks The file Path as Strain and Reture The content of the TEXT 
"""

 try:
    
    with open (file_path) as file:
        content=file.read()
    return content.strip()
 except FileNotFoundError:
     raise(FileNotFoundError)




def parse_template(word:str)->str:
 """
This Function Take Strain as An In put and Return the Seprated body of TEXT and The Holding Values of Them 
"""
 actual_part=re.findall(r'{(.*?)}',word)

 actual_stripped=re.sub('{.*?}','{}',word)

 return actual_stripped,tuple(actual_part)
 
# print(parse_template("It was a {Adjective} and {Adjective} {Noun}."))

    


def merge(string_text:str,word_to_add:tuple)->str :
    """
    THis Function Takes Body oF the Teks as Strain and Words Inputed as Strain and Return The same Works inupts 
    """
    updatedText=string_text.format(*word_to_add)

    with open('assets/result.txt','w') as output:
        output.write(updatedText)
    return updatedText




input_list=[]
def gameStart():
    """
    THis Function Handle The Game For This Lab 
    """
    print("""
    Hello and Welcome To MADLIB Game 
    Please Follow The Instructions 

    
    """)

    all_contant=read_template('assets/Text_game.txt')
    text_body,list_of_words=parse_template(all_contant)

    for i in list_of_words:
         user_input=input(f'Enter a {i} ')
         input_list.append(user_input)

     
    return merge(text_body,tuple(input_list))
    




if __name__=="__main__":
  print(gameStart())