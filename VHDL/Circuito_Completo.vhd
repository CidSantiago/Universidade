LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY circuit IS
	PORT(A, B, C: IN std_logic;
		D: OUT std_logic);
END circuit;

ARCHITECTURE arch OF circuit IS
	SIGNAL not_out: std_logic;
	SIGNAL and1_out: std_logic;
	SIGNAL and2_out: std_logic;
BEGIN
	port1: ENTITY work.p_not(arch)
		PORT MAP(input => A, 
				output => not_out);
	
	port2: ENTITY work.p_and(arch)
		PORT MAP(input1 => not_out, 
				input2 => B, 
				output => and1_out);
	
	port3: ENTITY work.p_and(arch)
		PORT MAP(input1 => B, 
				input2 => C,
				output => and2_out);
		
	port4: ENTITY work.p_or(arch)
		PORT MAP(input1 => and1_out, 
				input2 => and2_out, 
				output => D);
	
END arch;