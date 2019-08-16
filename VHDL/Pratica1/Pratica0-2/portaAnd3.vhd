library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

ENTITY portaAnd3 IS
	
PORT(inputA,inputB,inputC:IN std_logic;
outputA: OUT std_logic);

END portaAnd3;

ARCHITECTURE and3 OF portaAnd3 IS
SIGNAL sig: std_logic;

BEGIN
	port1: ENTITY work.portaAnd2(and3)
		PORT MAP (input1 => inputA,
			input2 => inputB,
			output => sig);

	port2: ENTITY work.portaAnd2(and3)
		PORT MAP (input1 => sig,
			input2 => inputC,
			output => outputA);
  
END and3;