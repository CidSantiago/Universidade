library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

ENTITY portaOr IS
	
PORT(input1, input2:IN std_logic;
output: OUT std_logic);

END portaOr;

ARCHITECTURE por OF portaOr IS

BEGIN
	output <= input1 OR input2;
END por;