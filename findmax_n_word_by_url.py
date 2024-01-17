import pandas as pd

class Findmaxrepeatedn:    
    def by_url(path,n=int) :    

        data=pd.read_excel(path,header=0)

        dict_address={}
        #Split the url "/" sign and "-" sign and process with the last part
        for address in data["Address"]:
            address=str(address)
            address=address.split("/")[-1].split("-")
            
            for word in address:
                #Ignore short words and numbers 
                if len(word)>=4 and not word.isdigit():

                    #add word to the dict as value=1,if is already in dict add 1
                    if word in dict_address:
                        dict_address[word]+=1
                    else:
                        dict_address[word]=1

        # Sort and get top 'n' words  
        sorted_list=sorted(dict_address.items(), key=lambda t:t[1], reverse=True)[:n]
        df_address=pd.DataFrame(data=sorted_list,columns=["Words","Frequencies"])

         # Write to an Excel file  
        writing_path="Word_Frequencies.xlsx"
        with pd.ExcelWriter(writing_path) as writer:
            df_address.to_excel(writer, sheet_name='URL Count Page')
        


