import itertools as it

# Gets the number of currencies from user as an integer
def getnum():
    
    while True:
        try:
            n = int(input("Enter number of currencies: "))
            if n>2:
                break
            else:
                print("Value must be integer greater than 2. Please retry.")
                continue
        except ValueError:
            print(":( An error occured. Please try again.")
            continue
    return n
n = getnum()

currencies = []

for g in range(n):
   while True:
      cur = input('Enter currency ticker: ')
      if cur not in currencies:
         currencies.append(cur)
         break
      else:
         print("Error! That currency has already been registered. Please try again!")
    
    
base = input('Select base currency: ')
while base not in currencies:
    print('currency not found. Please try again')
    base = input('Select base currency: ')
currencies.append(base)

orders = []
if n>=3 :   
    for order in range(3 , n + 1):#for an order n, the list of currencies in permutations = n+1
        orders.append(order)

mc = [list(set([k for k in it.permutations(currencies, order + 1) if k[0]==k[order]])) for order in orders]


quotes = {}
unavailable_quotes = []

indeterminate_permutations = [[] for order in orders]

for combs in mc:

    g = mc.index(combs)
    #if a comb is at g, then the indeterminate comb should also be at g
    
    for per in combs :
        
        for i in range(len(per)-1):
            pair = per[i]+'/'+per[i+1]
            
            if pair in quotes:
                continue
            
            elif pair in unavailable_quotes:
                indeterminate_permutations[g].append(per)
                break
            
            else:
                value = input('Enter ask price for '+str(per[i])+'/'+str(per[i+1])+'(How much ' +str(per[i+1])+ ' can 1' +str(per[i]) +' buy?\n...')
                
                if value == 'nil' or value == 'Nil' or value == 'None' or value == None:
                    indeterminate_permutations[g].append(per)
                    unavailable_quotes.append(pair)
                    break
                
                else:
                    while True:
                        try:
                            value = float(value)
                            quotes[pair] = value
                            break
                        except ValueError:
                            if value == 'nil' or value == 'Nil' or value == 'None' or value == None:
                                indeterminate_permutations[g].append(per)
                                unavailable_quotes.append(pair)
                                break
                            else:
                                value = input(' An error occured. Please try again.\n...')
                           

#now the calculations
#first delete the indeterminate_permutations

nmc = [list(set(mc[i]).difference(set(indeterminate_permutations[i]))) for i in range(len(orders))]

#now down to business

returns = []
for order in nmc:
    returns.append([])

for combs in nmc:
    
    for per in combs:
        num = 1
        for i in range(len(per)):
            if i+1 != len(per):
                pair = per[i]+'/'+per[i+1]
                num *= quotes[pair]
            else:
                returns[nmc.index(combs)].append(num)

#the printing business
#It should be noted that an adoption of the MVC application design would render this section irrelevant

combs_to_print = [[] for o in range(len(nmc))]
for combs in nmc:
    for per in combs:
        n= ''
        for i in range(len(per)):
            if i != len(per)-1:
                n+= per[i] + ' >> '
            else:
                n+= per[i]
        combs_to_print[nmc.index(combs)].append(n)
    

returns_to_print = [[] for o in range(len(nmc))]

for returnlist in returns:
    for n in returnlist:
        n -= 1
        n *= 100
        returns_to_print[returns.index(returnlist)].append(n)
    
formatguy = '{:<'+str(len(combs_to_print[len(combs_to_print)-1]))+'s}'


d = len(combs_to_print[len(combs_to_print)-1][0]) - len('Conversions\n\n')
youngone = '{:>'+str(d)+'s}'

print('\n\n'+formatguy.format('Conversions') + youngone.format('') + '{:>11s}'.format('ROI')+'\n')

for returnlist in returns:
    i = returns.index(returnlist)
    for k in range(len(returnlist)):
        d = len(combs_to_print[len(combs_to_print)-1][0]) - len(combs_to_print[i][k])
        
        youngone = '{:>'+str(d)+'s}'
        print(combs_to_print[i][k]+ youngone.format('')+str('{0:>10,.2f}'.format(returns_to_print[i][k]))+'%')
