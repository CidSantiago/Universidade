LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY mux IS

PORT(a, b, c, d: IN std_logic;
sel: IN std_logic_vector(1 DOWNTO 0);
y: OUT std_logic);
END mux;

ARCHITECTURE arch OF mux IS
BEGIN
y <= a WHEN sel = "00" ELSE
b WHEN sel = "01" ELSE
c WHEN sel = "10" ELSE
d;
END arch;
