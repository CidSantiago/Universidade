library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

ENTITY Encode4x2 IS
	
PORT(Y0,Y1,Y2,Y3,EN:IN std_logic;
A0,A1: OUT std_logic);

END Encode4x2;

ARCHITECTURE enc42 OF Encode4x2 IS
SIGNAL Y1orY3, Y2orY3: std_logic;

BEGIN
	portY1Y3: ENTITY work.portaOr(por)
		PORT MAP( input1 => Y1,
			input2 => Y3,
			output => Y1orY3);
	portY2Y3: ENTITY work.portaOr(por)
		PORT MAP( input1 => Y2,
			input2 => Y3,
			output => Y2orY3);
	portA0: ENTITY work.portaAnd2(and2)
		PORT MAP( input1 => EN,
			input2 => Y1orY3,
			output => A0);
	portA1: ENTITY work.portaAnd2(and2)
		PORT MAP( input1 => EN,
			input2 => Y2orY3,
			output => A1);
END enc42;
