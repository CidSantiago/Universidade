create table Departamento(
	cod_dept int NOT NULL,
	nome char(50),
	matr int NOT NULL,

	CONSTRAINT PK_Dept PRIMARY KEY (cod_dept),
	CONSTRAINT FK_DeptEmp FOREIGN KEY (matr) REFERENCES Empregados(matr) 
);

create table Divisao(
	cod_div int NOT NULL,
	nome char(50),
	matr int NOT NULL,
	dept_assoc int NOT NULL,

	CONSTRAINT PK_Div PRIMARY KEY (cod_div),
	CONSTRAINT FK_DivEmp FOREIGN KEY (matr) REFERENCES Empregados(matr),
	CONSTRAINT FK_DivDept FOREIGN KEY (dept_assoc) REFERENCES Departamento(cod_dept) 
);

create table Empregados(
	matr int NOT NULL,
	nome char(50),
	dt_lotacao smalldatetime NOT NULL,
	cod_div int NOT NULL,

	CONSTRAINT PK_Emp PRIMARY KEY (matr),
	CONSTRAINT FK_EmpDiv FOREIGN KEY (cod_div) REFERENCES Divisao(cod_div) 
);

SELECT d.nome
FROM Divisao d, Empregados e
WHERE d.matr = e.matr AND e.matr = ANY(SELECT emp_desc.matr FROM emp_desc where e.matr = emp_desc.matr)

SELECT e.nome
FROM Empregados e LEFT OUTER JOIN Dependentes d
WHERE d.nome = NULL
