#!/usr/bin/env python
# coding: utf-8

# # Using Python for Research Homework: Week 3, Case Study 1
# 
# A cipher is a secret code for a language.  In this case study, we will explore a cipher that is reported by contemporary Greek historians to have been used by Julius Caesar to send secret messages to generals during times of war.

# ### Exercise 1
# 
# A cipher is a secret code for a language. In this case study, we will explore a cipher that is reported by contemporary Greek historians to have been used by Julius Caesar to send secret messages to generals during times of war.
# 
# The Caesar cipher shifts each letter of a message to another letter in the alphabet located a fixed distance from the original letter. If our encryption key were `1`, we would shift `h` to the next letter `i`, `i` to the next letter `j`, and so on. If we reach the end of the alphabet, which for us is the space character, we simply loop back to `a`. To decode the message, we make a similar shift, except we move the same number of steps backwards in the alphabet.
# 
# Over the next five exercises, we will create our own Caesar cipher, as well as a message decoder for this cipher. In this exercise, we will define the alphabet used in the cipher.
# 
# #### Instructions
# - The `string` library has been imported. Create a string called `alphabet` consisting of the space character `' '` followed by (concatenated with) the lowercase letters. Note that we're only using the lowercase letters in this exercise.

# In[1]:


import string
# write your code here!
alphabet = " " + string.ascii_lowercase


# ### Exercise 2 
# 
# In this exercise, we will define a dictionary that specifies the index of each character in `alphabet`.
# 
# #### Instructions 
# - `alphabet` has already defined in the last exercise. Create a dictionary with keys consisting of the characters in alphabet and values consisting of the numbers from 0 to 26.
# - Store this as `positions`.

# In[2]:


# write your code here!
positions = {}
index = 0
for char in alphabet:
    positions[char] = index
    index += 1
print(positions['n'])


# ### Exercise 3
# 
# In this exercise, we will encode a message with a Caesar cipher.
# 
# #### Instructions 
# 
# - `alphabet` and `positions` have already been defined in previous exercises. Use `positions` to create an encoded message based on message where each character in message has been shifted forward by 1 position, as defined by positions.
# - **Note that you can ensure the result remains within 0-26 using result % 27**
# - Store this as `encoded_message`.

# In[3]:


message = "hi my name is caesar"
# write your code here!

encoding_list = []
for char in message:
    position = positions[char]
    encoded_position = (position + 1) % 27
    encoding_list.append(alphabet[encoded_position])
encoded_message = "".join(encoding_list)

print(encoded_message)


# ### Exercise 4
# 
# In this exercise, we will define a function that encodes a message with any given encryption key.
# 
# #### Instructions 
# - `alphabet`, `position` and `message` remain defined from previous exercises. Define a function `encoding` that takes a message as input as well as an int encryption key `key` to encode a message with the Caesar cipher by shifting each letter in message by key positions.
# - Your function should return a string consisting of these encoded letters.
# - Use `encoding` to encode message using `key = 3` and save the result as `encoded_message`.
# Print `encoded_message`.

# In[4]:


# write your code here 
def encoding(message, key = 0):
    encoding_list = []
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoding_list.append(alphabet[encoded_position])
    encoded_string = "".join(encoding_list)
    return encoded_string

encoded_message = encoding(message, 3)
print(encoded_message)


# ### Exercise 5
# 
# In this exercise, we will decode an encoded message.
# 
# #### Instructions 
# - Use `encoding` to decode `encoded_message`.
# - Store your encoded message as `decoded_message`.
# - Print `decoded_message`. Does this recover your original message?

# In[5]:


# write your code here!
decoded_message = encoding(encoded_message, -3)
print(decoded_message)


# In[ ]:




