INSERT INTO Departamento(nome,ender,cod_dept_chefia)
VALUES ('DETI', 'AC Publico,725',024)

INSERT INTO Divisao(cod_dept,cod_div_chefia,nome)
VALUES (01, 25,'GTEL')

INSERT INTO Empregado(cod_dept_chefia,cod_div,cod_div_chefia,dt_lotacao,nome)
VALUES (024, 01, 025, getdate(), 'Walter')

INSERT INTO Empregado(cod_dept_chefia,cod_div,cod_div_chefia,dt_lotacao,nome)
VALUES (024, 01, 025, getdate(), 'Tarcisio')

INSERT INTO Empregado(cod_dept_chefia,cod_div,cod_div_chefia,dt_lotacao,nome)
VALUES (024, 01, 025, getdate(), 'Joao Cesar')

INSERT INTO Empregado(cod_dept_chefia,cod_div,cod_div_chefia,dt_lotacao,nome)
VALUES (024, 01, 025, getdate(), 'Yvo')

INSERT INTO Empregado(cod_dept_chefia,cod_div,cod_div_chefia,dt_lotacao,nome)
VALUES (024, 01, 025, getdate(), 'Rubens')

INSERT INTO Empregado(cod_dept_chefia,cod_div,cod_div_chefia,dt_lotacao,nome)
VALUES (024, 01, 025, getdate(), 'Charles')

insert into Desconto(cod_desc, nome, valor)
values
(1, 'FGTS', 100),
(2, 'Aposentadoria', 100),
(3, 'Im_Estadual', 100),
(4, 'Im_Federal', 200);

insert into Vencimento(cod_venc, nome, valor)
values
(1, 'Graduado', 1000),
(2, 'Mestre', 500),
(3, 'Doutor', 550),
(4, 'Pós Doutor', 600),
(5, 'Chefe de Dpt', 4000),
(6, 'Chefe de Divisão', 3000);

insert into Emp_Desc(matr,cod_desc)
values
(1, 1),(1, 2),(1, 3),(1, 4),
(2, 1),(2, 2),(2, 3),
(3, 1),(3, 2),
(4, 1);



insert into Emp_Venc(matr, cod_venc)
values
(1, 1),(1, 2),(1, 3),(1, 4),(1, 5),
(2, 1),(2, 2),(2, 3),(2, 4),
(3, 1),(3, 2),(3, 3),(3, 4),(3, 6),
(4, 1),
(5, 1), (5, 2),(5, 3),(5, 4);

SELECT (sum(vencimento.valor) -(select sum(desconto.valor) from empregado e, Emp_Desc, desconto 
						where e.matr = Emp_Desc.matr and Emp_Desc.cod_desc = desconto.cod_desc and e.matr = Emp_Desc.matr)) as ' Teste'
						
						
		 from empregado emp, Emp_Venc, vencimento 
where emp.matr = Emp_Venc.matr and Emp_Venc.cod_venc = vencimento.cod_venc
group by emp.matr, emp.cod_div

select sum(Vencimento.valor)
from Vencimento, Empregado, Emp_Venc
Where Vencimento.cod_venc = Emp_Venc.cod_venc AND Emp_Venc.matr = Empregado.matr
GROUP by Empregado.matr

select sum(Desconto.valor)
from  Empregado,  Emp_Desc, Desconto
Where Emp_Desc.matr = Empregado.matr and Emp_Desc.cod_desc = Desconto.cod_desc
GROUP by Empregado.matr

