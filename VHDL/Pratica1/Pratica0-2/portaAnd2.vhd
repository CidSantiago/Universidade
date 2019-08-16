library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

ENTITY portaAnd2 IS
	
PORT(input1, input2:IN std_logic;
output: OUT std_logic);

END portaAnd2;

ARCHITECTURE and2 OF portaAnd2 IS

BEGIN
	output <= input1 AND input2;
END and2;