def raodenoba(text):
    qmovnebi = ['a', 'e', 'i', 'u', 'o']
    count = 0
    for i in text.lower(): 
        if i in qmovnebi:
            count += 1
    return count

print(raodenoba("GOAL ORIENTED ACADEMY"))
