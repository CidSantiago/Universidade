library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

ENTITY portaAnd IS
	
PORT(input1,input2,input3:IN std_logic;
output: OUT std_logic);

END portaAnd;

ARCHITECTURE pAnd OF portaAnd IS

BEGIN
	output <= input1 AND input2 AND input3;
END PAnd;