PRAGMA foreign_keys = ON;

-- ============================================================
-- DML - Inserção de dados
-- ============================================================

INSERT INTO Professor (
    nome_professor,
    departamento,
    salario,
    ano_contratacao
) VALUES
    ('Carlos Silva', 'Ciências Exatas', 6500.00, 2018),
    ('Mariana Souza', 'Tecnologia', 7200.00, 2020),
    ('Roberto Lima', 'Humanas', 5800.00, 2016),
    ('Fernanda Oliveira', 'Ciências Biológicas', 6100.00, 2019),
    ('Paulo Henrique', 'Matemática', 7000.00, 2015),
    ('Juliana Costa', 'Administração', 5900.00, 2021),
    ('Ricardo Almeida', 'Engenharia', 7800.00, 2014),
    ('Patrícia Gomes', 'Direito', 6700.00, 2017),
    ('André Martins', 'Computação', 8200.00, 2022),
    ('Camila Ribeiro', 'Física', 6400.00, 2018);

INSERT INTO Curso (
    nome_curso,
    duracao,
    coordenador
) VALUES
    ('Engenharia Civil', 5, 7),
    ('Direito', 5, 8),
    ('Ciência de Dados', 4, 2),
    ('Administração', 4, 6),
    ('Matemática', 4, 5),
    ('Biologia', 4, 4),
    ('Computação', 4, 9),
    ('Física', 4, 10),
    ('Pedagogia', 4, 3),
    ('Engenharia de Software', 4, 9);

INSERT INTO Aluno (
    nome_aluno,
    ano_nascimento,
    ano_ingresso,
    id_curso
) VALUES
    ('Ana Beatriz Santos', 2002, 2021, 1),
    ('João Pedro Lima', 2001, 2020, 2),
    ('Lucas Martins Rocha', 2003, 2022, 3),
    ('Fernanda Alves Pereira', 2000, 2019, 4),
    ('Gabriel Souza Costa', 2004, 2023, 5),
    ('Mariana Ferreira Nunes', 2002, 2021, 6),
    ('Rafael Gomes Silva', 2001, 2020, 7),
    ('Isabela Ribeiro Almeida', 2003, 2022, 8),
    ('Bruno Henrique Dias', 2000, 2019, 9),
    ('Larissa Oliveira Martins', 2004, 2023, 10);

INSERT INTO Disciplina (
    nome_disciplina,
    id_professor,
    carga_horaria,
    id_curso
) VALUES
    ('Structural Mechanics', 7, 180, 1),
    ('Civil Law', 8, 80, 2),
    ('Introduction to Data Analysis', 2, 160, 3),
    ('Business Management', 6, 160, 4),
    ('Calculus I', 5, 80, 5),
    ('General Biology', 4, 160, 6),
    ('Database Fundamentals', 9, 60, 7),
    ('Classical Mechanics', 10, 180, 8),
    ('Educational Psychology', 3, 160, 9),
    ('Software Engineering', 9, 180, 10);
