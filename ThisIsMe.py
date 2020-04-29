def love(who):
    if who == "family":
        response = "Joanna loves her family"
    elif who == "husband":
        response = "Joanna loves Juan"
    elif who == "church life":
        response = "Joanna loves the church life"
    else:
        response = "I'm only in love with three entities so far. What else shall I fall in love with?"
    return response

loves = str(input("Who do you love the most right now - family, husband, or church life?"))
print(type(loves), loves)

#print(love(loves))
