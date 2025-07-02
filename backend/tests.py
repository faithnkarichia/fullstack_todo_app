def checkPalindrome(str):
    cleaned=str.replace(" ", "").lower()
    if cleaned==cleaned[::-1]:
        print("is palindrome")

    else:
        print("not palindrome")
checkPalindrome("Madam")



def anagram_checker(a,b):

    cleaned_a=a.replace(" ","").lower()
    cleaned_b=b.replace(" ","").lower()
    if sorted(cleaned_a)==sorted(cleaned_b):
        print("is anagram")

    else:
        print("not anagram")
anagram_checker("silent","listen")
anagram_checker("hello", "world") 




# def count_vowels(words):
#     vowels=["a","e","i","o","u"]
    
#     count=0
    
#     for word in words:
#         if word.lower() in vowels:
#             count+=1

#     print(count)
# count_vowels("PAaradise")



def count_vowels(words):
    vowels=["a","e","i","o","u"]
    vowel_dict={}
    
    
    for word in words.lower():
        if word in vowels:
            if word in vowel_dict:
                vowel_dict[word] +=1
            else:
                vowel_dict[word]=1

    print(vowel_dict)
count_vowels("PAaradise")




def count_words(sentence):
   

    word_dict={}
    print(sentence.split())
    sentence=sentence.lower()
    for word in sentence.split():
        if word in word_dict:
            word_dict[word] +=1

        else:
            word_dict[word]=1
    return word_dict

print(count_words("The cat and the dog and the bird"))




def find_largest(nums):
    
    return max(nums)

print(find_largest([4, 9, 2, 12, 6]))




def second_largest(nums):
    sorted_nums= sorted(nums)
    return sorted_nums[-2]

print(second_largest([4, 9, 2, 12, 6]))




def sum_evens(nums):
    evens=[]
    for num in nums:
        if num %2==0:
            evens.append(num)
    return sum(evens)


print(sum_evens([1, 2, 3, 4, 5, 6]))



def find_duplicates(nums):
    normal=[]
    duplicates=[]
    for num in nums:
        
        
        if num in normal:
            duplicates.append(num)
        normal.append(num)
        
    return duplicates

print(find_duplicates([1, 2, 3, 2, 4, 5, 3]) ) 
# ➡️ [2, 3]


def remove_duplicates(nums):
    return list(set(nums))
   

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]) ) 
# ➡️ [1, 2, 3, 4, 5]


def most_common(nums):

    pass


most_common([1, 2, 2, 3, 2, 4, 4])  
# ➡️ 2




