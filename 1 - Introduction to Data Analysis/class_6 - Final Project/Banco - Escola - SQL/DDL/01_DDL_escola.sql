PRAGMA foreign_keys = ON;

-- ============================================================
-- DDL - Criação das tabelas em SQLite
-- ============================================================

CREATE TABLE Professor (
    id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_professor VARCHAR(80) NOT NULL,
    departamento VARCHAR(50) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    ano_contratacao INT NOT NULL
);

CREATE TABLE Curso (
    id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_curso VARCHAR(50) NOT NULL,
    duracao INT NOT NULL,
    coordenador INT NOT NULL,

    CONSTRAINT fk_curso_professor 
        FOREIGN KEY (coordenador) 
        REFERENCES Professor(id_professor)
);

CREATE TABLE Aluno (
    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_aluno VARCHAR(80) NOT NULL,
    ano_nascimento INT NOT NULL,
    ano_ingresso INT NOT NULL,
    id_curso INT NOT NULL,

    CONSTRAINT fk_aluno_curso 
        FOREIGN KEY (id_curso) 
        REFERENCES Curso(id_curso)
);

CREATE TABLE Disciplina (
    id_disciplina INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_disciplina VARCHAR(80) NOT NULL,
    id_professor INT NOT NULL,
    carga_horaria INT NOT NULL,
    id_curso INT NOT NULL,

    CONSTRAINT fk_disciplina_professor 
        FOREIGN KEY (id_professor) 
        REFERENCES Professor(id_professor),

    CONSTRAINT fk_disciplina_curso 
        FOREIGN KEY (id_curso) 
        REFERENCES Curso(id_curso)
);
