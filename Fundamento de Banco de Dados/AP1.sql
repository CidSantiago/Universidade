CREATE DATABASE AP1v2;

use AP1v2;

CREATE TABLE Departamento(
    cod_dept int IDENTITY(1,1),
    nome varchar(20),
    ender varchar(40) NOT NULL,
    cod_dept_chefia int NOT NULL,

    CONSTRAINT PK_Dept PRIMARY KEY (cod_dept),
    CONSTRAINT UK_DeptChefe UNIQUE (cod_dept_chefia)
);


CREATE TABLE Divisao(
    cod_dept int NOT NULL,
    cod_div int IDENTITY(1,1),
    nome varchar(20) ,
    cod_div_chefia int NOT NULL,
    
    CONSTRAINT PK_Div PRIMARY KEY (cod_div),
    CONSTRAINT FK_DivDept
    	FOREIGN KEY(cod_dept) REFERENCES Departamento(cod_dept) ON DELETE NO ACTION,
        FOREIGN KEY(cod_dept) REFERENCES Departamento(cod_dept) ON UPDATE CASCADE,
    CONSTRAINT UK_DivChefe UNIQUE (cod_div_chefia)
);


CREATE TABLE Fone(
    cod_dept int NOT NULL,
    fone int NOT NULL,
    
    CONSTRAINT PK_Fone PRIMARY KEY (cod_dept, fone),
    CONSTRAINT FK_FoneDiv 
    	FOREIGN KEY (cod_dept) REFERENCES Departamento(cod_dept) ON DELETE CASCADE,
);


CREATE TABLE Empregado(
    cod_div int NOT NULL,
    matr int IDENTITY(1,1) NOT NULL,
    nome varchar(20),
    dt_lotacao date NOT NULL,
    cod_dept_chefia int,
    cod_div_chefia int,
    
    CONSTRAINT PK_Emp PRIMARY KEY (matr),
    CONSTRAINT FK_EmpDiv
    	FOREIGN KEY (cod_div) REFERENCES Divisao(cod_div) ON DELETE NO ACTION,
    	FOREIGN KEY (cod_div) REFERENCES Divisao(cod_div) ON UPDATE NO ACTION,
    CONSTRAINT FK_EmpDivChefe
    	FOREIGN KEY (cod_div_chefia) REFERENCES Divisao(cod_div_chefia) ON DELETE NO ACTION,
    	FOREIGN KEY (cod_div_chefia) REFERENCES Divisao(cod_div_chefia) ON UPDATE NO ACTION,
    CONSTRAINT FK_EmpDeptChefe
    	FOREIGN KEY (cod_dept_chefia) REFERENCES Departamento(cod_dept_chefia) ON DELETE NO ACTION,
    	FOREIGN KEY (cod_dept_chefia) REFERENCES Departamento(cod_dept_chefia) ON UPDATE NO ACTION,
);


CREATE TABLE Dependente(
    matr_resp int NOT NULL,
    nome varchar(20),
    dt_nascimento DATE NOT NULL,

    CONSTRAINT PK_Depend PRIMARY KEY (matr_resp, nome),
    CONSTRAINT FK_Depend 
    	FOREIGN KEY (matr_resp) REFERENCES Empregado(matr) ON DELETE CASCADE,
);


CREATE TABLE Vencimento (
    cod_venc int NOT NULL,
    nome varchar(20),
    valor decimal(10,2) NOT NULL,
            
    CONSTRAINT PK_Venc PRIMARY KEY (cod_venc),
);

CREATE TABLE Desconto (
    cod_desc int NOT NULL,
    nome varchar(20),
    valor decimal(10,2) NOT NULL,
            
    CONSTRAINT PK_DESCONTO PRIMARY KEY (COD_DESC),
);

CREATE TABLE Emp_Venc(
    matr int NOT NULL,
    cod_venc int NOT NULL,
            
    CONSTRAINT PK_EV PRIMARY KEY (matr, cod_venc),
    CONSTRAINT FK_EVEmp
    	FOREIGN KEY (matr) REFERENCES Empregado(matr) ON DELETE CASCADE,
    CONSTRAINT FK_EVVenc
        FOREIGN KEY (cod_venc) REFERENCES Vencimento(cod_venc) ON DELETE NO ACTION,
        FOREIGN KEY (cod_venc) REFERENCES Vencimento(cod_venc) ON UPDATE CASCADE,
);

CREATE TABLE Emp_Desc(
    matr int NOT NULL,
    cod_desc int NOT NULL,

    CONSTRAINT PK_ED PRIMARY KEY (matr,cod_desc),
    CONSTRAINT FK_EDEmp
    	FOREIGN KEY (matr) REFERENCES Empregado(matr) ON DELETE CASCADE,
    CONSTRAINT FK_EDDesc
        FOREIGN KEY (cod_desc) REFERENCES Desconto(cod_desc) ON DELETE NO ACTION,
        FOREIGN KEY (cod_desc) REFERENCES Desconto(cod_desc) ON UPDATE CASCADE,
);