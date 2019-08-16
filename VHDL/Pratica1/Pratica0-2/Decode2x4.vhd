library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

ENTITY Decode2x4 IS
	
PORT(A0,A1,EN:IN std_logic;
Y0,Y1,Y2,Y3: OUT std_logic);

END Decode2x4;

ARCHITECTURE dec24 OF Decode2x4 IS
SIGNAL invA0, invA1: std_logic;

BEGIN
	notA0: ENTITY work.portaInversora(dec24)
		PORT MAP ( input => A0,
			output => invA0);
	notA1: ENTITY work.portaInversora(dec24)
		PORT MAP ( input => A1,
			output => invA1);
	portY0: ENTITY work.portaAnd3(dec24)
		PORT MAP (inputA => EN,
			inputB => invA0,
			inputC => invA1,
			outputA => Y0);
	portY1: ENTITY work.portaAnd3(dec24)
		PORT MAP (inputA => EN,
			inputB => A0,
			inputC => invA1,
			outputA => Y1);
	portY2: ENTITY work.portaAnd3(dec24)
		PORT MAP (inputA => EN,
			inputB => invA0,
			inputC => A1,
			outputA => Y2);
	portY3: ENTITY work.portaAnd3(dec24)
		PORT MAP (inputA => EN,
			inputB => A0,
			inputC => A1,
			outputA => Y3);
	
END dec24;