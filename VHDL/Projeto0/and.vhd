library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

ENTITY portaAnd IS
	
PORT(a,b:IN std_logic;
c: OUT std_logic);

END portaAnd;

ARCHITECTURE pAnd OF portaAnd IS

BEGIN
	c <= b AND a;
END PAnd;