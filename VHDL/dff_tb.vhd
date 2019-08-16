LIBRARY ieee;
USE ieee.std_logic_1164.all;

entity dff_tb is
end dff_tb;

architecture teste of dff_tb is
	signal d: std_logic := '0';
	signal clk: std_logic := '0';
	signal q: std_logic := '0';
	signal qbar: std_logic := '0';
	signal q2: std_logic := '0';
	signal qbar2: std_logic := '0';
begin
	dut1: entity work.dff(not_ok)
		PORT MAP(d => d,
				clk => clk,
				q => q,
				qbar => qbar);
	dut2: entity work.dff(ok)
		PORT MAP(d => d,
				clk => clk,
				q => q2,
				qbar => qbar2);
				
	clock: process is
	begin
		wait for 50 ns;
		clk <= not clk;
	end process clock;
	
	sti: process is
	begin
		wait for 100 ns;
		d <= '1';
		wait for 100 ns;
		d <= '0';
		wait for 100 ns;
		d <= '1';
	end process sti;
end teste;