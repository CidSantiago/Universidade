library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

ENTITY Encode4x2cod IS
	
PORT(Y0,Y1,Y2,Y3,EN:IN std_logic;
A0,A1: OUT std_logic);

END Encode4x2cod;

ARCHITECTURE enc42cod OF Encode4x2cod IS

BEGIN
	A0 <= '1' WHEN ((Y1='1' OR Y3='1') AND EN='1') ELSE
	      '0';	
	
	A1 <= '1' WHEN ((Y2='1' OR Y3='1') AND EN='1') ELSE
              '0';

END enc42cod;
