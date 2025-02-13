print("Hello world")
print("Hello world")
def shortenPath(path):
    stack = []
    if path[0]=="/":
        stack.append("")
    elements = filter(get_chars,path.split("/"))
    
    for ele in elements:
        if ele == "..":
            if len(stack)==0 or stack[-1]=="..":
                stack.append(ele)
            elif stack[-1]!="":
                stack.pop()
        else:
            stack.append(ele)
    if len(stack)==0 or stack[-1]=="":
        return "/"
    return "/".join(stack)

def get_chars(element):
    return len(element) > 0 and element!="."

