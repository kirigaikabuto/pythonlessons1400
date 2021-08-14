s = "Modern Singapore was founded in 1819 by Sir Stamford Raffles as a trading post of the British Empire. In 1867, the colonies in Southeast Asia were reorganised and Singapore came under the direct control of Britain as part of the Straits Settlements. During the Second World War, Singapore was occupied by Japan in 1942, and returned to British control as a separate crown colony following Japan's surrender in 1945. Singapore gained self-governance in 1959 and in 1963 became part of the new federation of Malaysia, alongside Malaya, North Borneo, and Sarawak. Ideological differences led to Singapore being expelled from the federation two years later and it became an independent country."
s = s.replace(",", "")
s = s.replace(".", "")
words = s.split(" ")
alpha = []
numbers = []
others = []
for i in words:
    if i.isalpha():
        alpha.append(i)
    elif i.isnumeric():
        numbers.append(i)
    else:
        others.append(i)
print(alpha)
print(numbers)
print(others)
