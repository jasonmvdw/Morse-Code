#Initialise Morse Dictionary
morse_codes = {
    "a" : "•⁃",
    "b" : "⁃•••",
    "c" : "⁃•⁃•",
    "d" : "⁃••",
    "e" : "•",
    "f" : "••⁃•",
    "g" : "⁃⁃•",
    "h" : "••••",
    "i" : "••",
    "j" : "•⁃⁃⁃",
    "k" : "⁃•⁃",
    "l" : "•⁃••",
    "m" : "⁃⁃",
    "n" : "⁃•",
    "o" : "⁃⁃⁃",
    "p" : "•⁃⁃•",
    "q" : "⁃⁃•⁃",
    "r" : "•⁃•",
    "s" : "•••",
    "t" : "⁃",
    "u" : "••⁃",
    "v" : "•••⁃",
    "w" : "•⁃⁃",
    "x" : "⁃••⁃",
    "y" : "⁃•⁃⁃",
    "z" : "⁃⁃••",
    "1" : "•⁃⁃⁃⁃",
    "2" : "••⁃⁃⁃",
    "3" : "•••⁃⁃",
    "4" : "••••⁃",
    "5" : "••••",
    "6" : "⁃••••",
    "7" : "⁃⁃•••",
    "8" : "⁃⁃⁃••",
    "9" : "⁃⁃⁃⁃•",
    "0" : "⁃⁃⁃⁃⁃",   
}

#Get User Input to convert
text_to_convert = input("What would you like to convert to morse code? : \n").lower()

#Convert text to morse code

converted_text = ''
for letter in text_to_convert:
     if letter in morse_codes:
        morse_letter = morse_codes[letter]
        converted_text += morse_letter + ", "
    else:
        print(f"{letter} is an Invalid Character")
            
print(converted_text)
    
