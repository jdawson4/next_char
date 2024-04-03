# next_char
Given a character, which character should come next? This program will make decisions like that based on a dataset!

In other words, this program will look at a corpus of text. For every letter in that text, the program will record the number of times the following letter was used. Using this sentence:

>I literally like it.

the program will record that the letter "i" was followed by "SPACE" one time, by "t" twice, and by "k" one time. The program will do the same thing for "SPACE", for "l", and so on until the end of the text.

Using this, we will be able to choose a letter and see *which letter is most likely to follow* in that corpus. We can then generate text of some indeterminate length; we will have created the dumbest possible language model!
