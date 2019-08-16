LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY p_and IS
	PORT(input1, input2: IN std_logic;
		output: OUT std_logic);
END p_and;

ARCHITECTURE arch OF p_and IS

BEGIN
	output <= input1 AND input2;
	
END arch;