; Chapter 10 Exercise 2			(Ex02_WriteString.asm)

Comment !
Description: Create a macro that writes a null-terminated 
string to the console with a given text color.
!
INCLUDE Irvine32.inc

mWritestringAttr MACRO aString,color
	push eax
	push edx
	mov  eax,color
	call SetTextColor
	mov  edx,OFFSET aString
	call WriteString
	pop  edx
	pop  eax
ENDM

.data
myString BYTE "This string is in color",0

.code
main PROC

	; Blue text on a white background:
	mWritestringAttr myString, (white SHL 4) + blue
	call Crlf

	; White text on a blue background:
	mWritestringAttr myString, (blue SHL 4) + white
	call Crlf

	mov	eax,lightGray		; normal screen color
	call SetTextColor

	exit
main ENDP
END main