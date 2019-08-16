library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

ENTITY inversor IS
	
PORT(a:IN std_logic;
b: OUT std_logic);

END inversor;

ARCHITECTURE inv OF inversor IS

BEGIN
	b <= NOT a;
END inv;

