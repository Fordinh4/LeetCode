def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # MY FIRST ATTEMPT BUT THE TIME EXCEED:
    # anagram_groups = []
    # used_words_index = []
    # for index_word in range(len(strs)):
    #     temp_list = []
    #     word_list = sorted(strs[index_word])


    #     for index_letters, letters in enumerate(strs):
    #         letters_list = sorted(letters)
    #         if word_list == letters_list and index_letters not in used_words_index:
    #             temp_list.append(letters)
    #             used_words_index.append(index_letters)

    #     if temp_list != []:
    #         anagram_groups.append(temp_list)

    # return anagram_groups


    # MY SECOND ATTEMPT AFTER LOOKING AT THE DISCUSSION:
    # Use dictionary and 1 for loops:
    anagram_groups = {}
    for word in strs:
        sorted_letters = str(sorted(word))
        if sorted_letters in anagram_groups:
            anagram_groups[sorted_letters].append(word)
        else:
            anagram_groups[sorted_letters] = [word]
            
    return list(anagram_groups.values())

a = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# strs = ["eat","tea","tan","ate","nat","bat"]
print(a)