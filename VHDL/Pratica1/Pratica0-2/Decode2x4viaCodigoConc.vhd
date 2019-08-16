library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

ENTITY Decode2x4Cod IS
	
PORT(A0,A1,EN:IN std_logic;
Y0,Y1,Y2,Y3: OUT std_logic);

END Decode2x4Cod;

ARCHITECTURE dec24cod OF Decode2x4Cod IS

BEGIN

Y0 <= '1' WHEN (A0='0' AND A1='0' AND EN='1') ELSE
      '0';

Y1 <= '1' WHEN (A0='1' AND A1='0' AND EN='1') ELSE
      '0';

Y2 <= '1' WHEN (A0='0' AND A1='1' AND EN='1') ELSE
      '0';

Y3 <= '1' WHEN (A0='1' AND A1='1' AND EN='1') ELSE
      '0';
	
END dec24cod;
