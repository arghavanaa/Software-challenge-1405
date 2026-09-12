def BalancedBrackets(text):
    result = ""

    for char in text:
        if char in "()[]{}":
            result += char

    #print(f"Text after removing extra characters:\n{result}")    
    stop = False
    if len(result) == 0:
        print( f"There are no brackets in {text}")
    else:
        LastLength = len(result) 
        while (len(result) > 0):
            for index, char in enumerate(result):
                if char in ")]}":
                    if char == ")":
                        if index > 0 and result[index-1] == "(" :
                            result = result[:index-1] + result[index+1:]
                            #print(result)
                            break
                        else:
                            print( f"The brackets in {text} are not balanced")
                            stop = True
                            break
                    elif char == "}":
                        if index > 0 and result[index-1] == "{" :
                            result = result[:index-1] + result[index+1:]
                            #print(result)
                            break
                        else:
                            print( f"The brackets in {text} are not balanced")
                            stop = True
                            break

                    elif char == "]":
                        if index > 0 and result[index-1] == "[" :
                            result = result[:index-1] + result[index+1:]
                            #print(result)
                            break
                        else:
                            print( f"The brackets in {text} are not balanced")
                            stop = True
                            break

            if stop :
                break
            if len(result) == LastLength:
                print( f"The brackets in {text} are not balanced")
                break
            else:
                LastLength = len(result)
            
        if len(result) == 0 :
            print( f"The brackets in {text} are balanced")


BalancedBrackets("")
BalancedBrackets("abc")
BalancedBrackets("([)]")
BalancedBrackets("(([]){})")
BalancedBrackets("{[()]}]")
BalancedBrackets("[{()}](){}")
BalancedBrackets("abc{def[ghi(jkl)]}")

print("end")
