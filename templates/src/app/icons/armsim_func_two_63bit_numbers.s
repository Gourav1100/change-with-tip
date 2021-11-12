.section .data
@num1: .byte 0xFF, 0xFF, 0xFF, 0x20, 0xFF, 0xFF, 0xFF, 0x01
num1: .byte 0x08, 0x07, 0x06, 0x05, 0x04, 0x03, 0x02, 0x01
@num2: .byte 0xFF, 0xFF, 0xFF, 0x40, 0xFF, 0xFF, 0xFF, 0x03
num2: .byte 0x18, 0x17, 0x16, 0x15, 0x14, 0x13, 0x12, 0x11
result: .skip 8

.section .text
.global _start
funcAddBigNums: 
	stmfd sp!, {r0-r7,lr}
	ldr r7, =num1
	ldr r1, [r7]
	ldr r0, [r7, #4]!
	ldr r7, =num2
	ldr r3, [r7]
	ldr r2, [r7, #4]
	adds r5, r1, r3    @add lower 4 bytes
	adc r4, r0, r2     @add upper 4 bytes + carry flag
	ldr r7, =result
	str r5, [r7], #4
	str r4, [r7]
FinishFunc_funcAddBigNums:
	ldmfd sp!, {r0-r7,pc}

funcAddBigNumsBetter: 
	stmfd sp!, {r0-r7,lr}
	ldr r7, =num1
	ldmia r7, {r0,r1}
	ldr r7, =num2
	ldmia r7, {r2,r3}
	adds r4, r0, r2    @add lower 4 bytes
	adc r5, r1, r3     @add upper 4 bytes + carry flag
	ldr r7, =result
	stmia r7, {r4,r5}
FinishFunc_funcAddBigNumsBetter:
	ldmfd sp!, {r0-r7,pc}
	
_start:
	bl funcAddBigNums
	bl funcAddBigNumsBetter
	swi 0x11

@ num1: 0x01FFFFFF 20FFFFFF
@ num1: 0x01020304 05060708
@ add r7, #4