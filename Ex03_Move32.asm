; Chapter 10 Exercise 3          (Ex03_Move32.asm)

Comment !
Description: Write a macro named mMove32 that receives two 32-bit
memory operands. The macro should move the source operand to the
destination operand.
!
INCLUDE Irvine32.inc

mMove32 MACRO destination,source
	push eax
	mov	eax,source
	mov	destination,eax
	pop	eax
ENDM

.data
var1 DWORD 12345678h
var2 DWORD 0

.code
main PROC

	mMove32 var2,var1
	
	mov  eax,var2	
	call WriteHex		; display var2
	call Crlf

	exit
main ENDP
END main