def convert_numbers_words(number):
    #Lists of each digit numbers
    num = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    special_nums = ['Ten','Eleven','Twelve','Therteen','Fourteen','Fiveteen','Sixteen','Seventeen','Eighteen','nineteen']
    tens = ['' , 'Ten','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninty']
    thousands = [''] + ['Thousand','Million','Billion','Trillion','Quadrillion','Quintillion']#empty qoutus to hold a place

    #Fristly make a function to convert two numbers
    def convert_two_num(n):
        if n < 10:
            return num[n] #number less than 10
        elif n < 20:
            return special_nums[n-10] #number more than ten & less than 20
        else:
            return tens[n // 10] + (' ' + num [n % 10] if n % 10 !=0 else '')
        
    #Secondly make a func to convert Three nums
    def convert_three_nums(n):
        hundreds = n // 100
        remind = n % 100
        if hundreds == 0:
            return convert_two_num(remind) 
        else:
            return num [hundreds] + 'hundred' + (' ' + convert_two_num(remind) if remind !=0 else '')

    #Main Func 
    if number == 0:
        return num[0]  

    words = ''
    for x in range(len(thousands)):
        block = number % 1000
        if block !=0:
            words = convert_three_nums(block) + ' ' + thousands[x] + ' ' + words
        number //= 1000
    return words.strip()



#Input numbers by the user
number = int(input("Plz, enter the number need to covert to words: "))
print("The number is: ",convert_numbers_words(number))