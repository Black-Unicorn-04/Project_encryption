#Hash Browns!

   ######
 #########
############
 ##########
  #######

# (๑ᵔ⤙ᵔ๑)


#CREATE A HASH   (Aka: Get cooking!)


import hashlib

ingredients = input("Enter plaintext:")

input_data = "ingredients"
hash_object = hashlib.sha256(input_data.encode())
hash_hex = hash_object.hexdigest()


print(hash_hex)

#</Black_Unicorn>