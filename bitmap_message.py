""" Bit map message  
     Displays a text message according to the provided bitmap image. """

import sys 

# try changing this multiline string to any image you like: 
# There are 68 periods along the top and bottom of this string:

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
.................................................................... """

print(' Bitmap Message, by Al Sweigart al@inventwithphython.com') 
print(' Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()
#loop over each line in the bitmap:
for line in bitmap.splitlines():
    #loop over each character in the line: 
    for i, bit in enumerate(line):
         if bit == ' ':
             # Print an empty space since there's a space in the bitmap:
             print(' ', end='')
         else:
             # print a character from the message:
             print(message[i % len(message)], end='')
    print() # print a new line 
  
