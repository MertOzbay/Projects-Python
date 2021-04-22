Interactive Cipher Displayer
==================

This is an interactive tool which lets the use encipher/decipher a desired text using a key and a cipher method of choice. Currently, the 
supported cipher methods are:
* Caesar Cipher
* Vignere Cipher

The user should select a cipher method by clicking on the buttons, input a key, input a text, and then click on encipher/decipher buttons 
to retrieved the ciphered text. The input text should only contain alphabetic characters (only English) and spaces. Spaces will be removed in the output. 
Current implementation preserves upper/lowercase distinction.

#### CAESAR CIPHER

A very old cipher method that works by performing a shift specified by the key value. If the key is 2, each character of the text will be shifted two letters 
to the right, meaning it will be replaced by the second letter that follows it in the alphabet. If we generalize this cipher, we get: 
> **_Ciphertext = (Plaintext+key) mod 26_**

For example:
> **_caesar_cipher.encipher("example", 3)_**

returns *"hadspoh"*.

Caesar cipher preserves letter frequencies and is quite easy to crack.

#### VIGNERE CIPHER

Vignere cipher is an improved version of the Caesar cipher. Instead of applying the same shifts to all letters, characters of a keyword is used one by one in a 
loop to get alternating shift values. If we generalize this cipher, we get:
> **_Ciphertext = (Plaintext+ keyword\[curr\_key\_idx\]) mod 26_**

For example:
> **_vigenere_cipher.encipher("example", "aa")_**

returns *"example"*.
> **_vigenere_cipher.encipher("example", "ab")_**

returns *"eyanpme"*.
