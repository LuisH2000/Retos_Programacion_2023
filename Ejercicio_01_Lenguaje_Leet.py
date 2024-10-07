'''
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''

#lista donde cada posicion representa el caracter a sustituir del abecedario. la posicion 0 es para la A
leet_list = ('4', 'I3', '[', ')', '3', "|=", '&', '#', '1', ",_|", ">|", '1', "/\\/\\", "^/", "0", "|*", "(_,)", "I2", "5", "7", "(_)", "\\/", "\\/\\/", "><", "j", "2")

my_string = input("Introduce el texto que quieras convertir: ")
my_new_string = ""

for char in my_string.upper():
    if char.isalpha():
        my_new_string += leet_list[ord(char) - ord('A')]
    else:
        my_new_string += char

print(my_new_string)