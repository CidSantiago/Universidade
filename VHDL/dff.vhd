LIBRARY ieee;
USE ieee.std_logic_1164.all;
---------------------------------------
ENTITY dff IS
	PORT ( d, clk: IN STD_LOGIC;
			q: BUFFER STD_LOGIC;
			qbar: OUT STD_LOGIC);
END dff;
---------------------------------------
ARCHITECTURE not_ok OF dff IS

BEGIN
	PROCESS (clk)
	BEGIN
		IF (clk'EVENT AND clk='1') THEN
			q <= d;
			qbar <= NOT q;
		END IF;
	END PROCESS;
END not_ok;

ARCHITECTURE ok OF dff IS
BEGIN
	PROCESS (clk)
	BEGIN
		IF (clk'EVENT AND clk='1') THEN
			q <= d;
		END IF;
	END PROCESS;
	qbar <= NOT q;
END ok;