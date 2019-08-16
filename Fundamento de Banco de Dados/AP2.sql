1)
create view v1 (nome_vendedor) as
	select v.nome
	From Vendedores v
		inner join Filiais f ON v.codfil = f.codfil
		inner join Historico h ON v.matr = h.matrvend
		inner join Estoque e ON h.coditem = e.cod
		inner join Fornecedor fo ON e.cod_for = fo.codfor
	WHERE f.nome = 'Fortaleza' AND fo.nome = 'São Paulo'

2)
create view v2 (Nome_Fornecedor,Item) as
SELECT f.nome, e.cod
FROM Fornecedor f 
	INNER JOIN Estoque e ON f.codfor = e.cod_for
	INNER JOIN Historico h ON e.cod = h.coditem
	INNER JOIN Vendedores v ON v.matr = h.matrvend
GROUP BY e.cod, v.matr, f.nome
HAVING count(v.matr) > 5

3) 
Create Trigger tr1 on Vendedores
for insert,update
as
if (select sum(i.salario)
	from inserted i 
	inner join Filiais f ON i.codfil = f.codfil
	GROUP BY i.codfil) > 0.4 *
	(select sum(v.salario)
	from Vendedores v)
	
	begin
	raiserror('salario invalido',16,1)
	rollback transaction
	end

4)
Create Trigger tr2 on Historico
for insert, update as
if ( select i.prvend
	from inserted i) < 0.9*
	(select e.pr_unit_ven
	from Estoque e, inserted i
	where e.cod = i.coditem)

	begin
	raiserror('Valor invalido',14,1)
	rollback transaction
	end

