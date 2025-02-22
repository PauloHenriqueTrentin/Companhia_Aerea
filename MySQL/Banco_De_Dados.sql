CREATE database Companhia_Aerea;
USE Companhia_Aerea;

CREATE TABLE Cliente (
    CPF CHAR(11) PRIMARY KEY,
    RG CHAR(9),
    Nome VARCHAR(100),
    DataNascimento DATE,
    Email VARCHAR(100) UNIQUE,
    CidadeResidencia VARCHAR(100),
    UnidadeFederal CHAR(2)
);

CREATE TABLE Voo (
    CodigoVoo CHAR(6) PRIMARY KEY,
    Origem VARCHAR(100),
    Destino VARCHAR(100),
    TipoAeronave VARCHAR(50)
);

CREATE TABLE TrechoVoo (
    CodigoTrecho CHAR(6) PRIMARY KEY,
    DataHoraPartida DATETIME,
    DataHoraChegada DATETIME,
    Classe ENUM('Economica', 'Executiva', 'PrimeiraClasse'),
    CodigoVoo CHAR(6),
    FOREIGN KEY (CodigoVoo) REFERENCES Voo(CodigoVoo)
);

CREATE TABLE Reserva (
    CodigoReserva CHAR(10) PRIMARY KEY,
    CPF CHAR(11),
    Status ENUM('Efetivada', 'NaoEfetivada'),
    DataReserva DATE,
    DataValidade DATE,
    FOREIGN KEY (CPF) REFERENCES Cliente(CPF)
);

CREATE TABLE Pagamento (
    CodigoPagamento CHAR(10) PRIMARY KEY,
    CodigoReserva CHAR(10),
    DataPagamento DATE,
    OperadoraCartaoCredito VARCHAR(50),
    NumeroParcelas INT,
    ValorTotal DECIMAL(10, 2),
    FOREIGN KEY (CodigoReserva) REFERENCES Reserva(CodigoReserva)
);

CREATE TABLE ReservaTrecho (
    CodigoReserva CHAR(10),
    CodigoTrecho CHAR(6),
    PRIMARY KEY (CodigoReserva, CodigoTrecho),
    FOREIGN KEY (CodigoReserva) REFERENCES Reserva(CodigoReserva),
    FOREIGN KEY (CodigoTrecho) REFERENCES TrechoVoo(CodigoTrecho)
);

INSERT INTO Cliente (CPF, RG, Nome, DataNascimento, Email, CidadeResidencia, UnidadeFederal) VALUES 
('12345678910', 'MG1234567', 'João Silva', '1980-01-01', 'joao.silva@example.com', 'Belo Horizonte', 'MG'),
('98765432100', 'SP7654321', 'Maria Oliveira', '1990-02-02', 'maria.oliveira@example.com', 'São Paulo', 'SP'),
('11122233344', 'RJ1122334', 'Carlos Pereira', '1975-03-03', 'carlos.pereira@example.com', 'Rio de Janeiro', 'RJ');

INSERT INTO Voo (CodigoVoo, Origem, Destino, TipoAeronave) VALUES 
('VOO123', 'Porto Alegre', 'São Paulo', 'Boeing 737'),
('VOO456', 'São Paulo', 'Rio de Janeiro', 'Airbus A320'),
('VOO789', 'Rio de Janeiro', 'Brasília', 'Embraer 195');

INSERT INTO TrechoVoo (CodigoTrecho, DataHoraPartida, DataHoraChegada, Classe, CodigoVoo) VALUES 
('T001', '2023-07-01 08:00:00', '2023-07-01 10:00:00', 'Economica', 'VOO123'),
('T002', '2023-07-01 12:00:00', '2023-07-01 14:00:00', 'Executiva', 'VOO123'),
('T003', '2023-07-02 09:00:00', '2023-07-02 10:30:00', 'PrimeiraClasse', 'VOO456'),
('T004', '2023-07-03 11:00:00', '2023-07-03 13:00:00', 'Economica', 'VOO789');

INSERT INTO Reserva (CodigoReserva, CPF, Status, DataReserva, DataValidade) VALUES 
('R001', '12345678910', 'Efetivada', '2023-06-15', '2023-07-15'),
('R002', '98765432100', 'NaoEfetivada', '2023-06-20', '2023-07-20'),
('R003', '11122233344', 'Efetivada', '2023-06-25', '2023-07-25');

INSERT INTO Pagamento (CodigoPagamento, CodigoReserva, DataPagamento, OperadoraCartaoCredito, NumeroParcelas, ValorTotal) VALUES 
('P001', 'R001', '2023-06-15', 'Visa', 3, 1200.00),
('P002', 'R003', '2023-06-25', 'MasterCard', 1, 500.00);

INSERT INTO ReservaTrecho (CodigoReserva, CodigoTrecho) VALUES 
('R001', 'T001'),
('R001', 'T002'),
('R002', 'T003'),
('R003', 'T004');

SELECT t.DataHoraPartida, t.DataHoraChegada, t.Classe, v.Origem, v.Destino
FROM TrechoVoo t
JOIN Voo v ON t.CodigoVoo = v.CodigoVoo
WHERE t.DataHoraPartida BETWEEN '2023-01-01' AND '2023-01-31';

SELECT c.CPF, c.Nome, r.CodigoReserva, t.DataHoraPartida, t.DataHoraChegada, v.Origem, v.Destino, t.Classe
FROM Cliente c
JOIN Reserva r ON c.CPF = r.CPF
JOIN ReservaTrecho rt ON r.CodigoReserva = rt.CodigoReserva
JOIN TrechoVoo t ON rt.CodigoTrecho = t.CodigoTrecho
JOIN Voo v ON t.CodigoVoo = v.CodigoVoo
WHERE c.CPF = '12345678900' AND r.DataReserva BETWEEN '2023-01-01' AND '2023-12-31';

SELECT c.Nome, c.Email, v.Origem, v.Destino
FROM Cliente c
JOIN Reserva r ON c.CPF = r.CPF
JOIN ReservaTrecho rt ON r.CodigoReserva = rt.CodigoReserva
JOIN TrechoVoo t ON rt.CodigoTrecho = t.CodigoTrecho
JOIN Voo v ON t.CodigoVoo = v.CodigoVoo
WHERE v.CodigoVoo = 'VOO123' AND r.DataReserva = CURDATE();

SELECT SUM(ValorTotal) AS TotalPagamentos
FROM Pagamento
WHERE OperadoraCartaoCredito = 'Visa' AND MONTH(DataPagamento) = 1 AND YEAR(DataPagamento) = 2023;

DELIMITER //
CREATE PROCEDURE CopiarEEliminarReservasNaoEfetivadas()
BEGIN
    INSERT INTO ReservasNaoEfetivadas (CodigoReserva, CPF, Status, DataReserva, DataValidade)
    SELECT CodigoReserva, CPF, Status, DataReserva, DataValidade
    FROM Reserva
    WHERE Status = 'NaoEfetivada' AND DataValidade < CURDATE();

    DELETE FROM Reserva
    WHERE Status = 'NaoEfetivada' AND DataValidade < CURDATE();
END //

DELIMITER ;

DELIMITER //

CREATE FUNCTION CalcularIdade(CPF CHAR(11))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE idade INT;
    SELECT TIMESTAMPDIFF(YEAR, DataNascimento, CURDATE()) INTO idade
    FROM Cliente
    WHERE Cliente.CPF = CPF;
    RETURN idade;
END //

DELIMITER ;

SELECT Nome, Email
FROM Cliente
WHERE DATE_FORMAT(DataNascimento, '%m-%d') = DATE_FORMAT('2023-06-25', '%m-%d');

SELECT t.CodigoTrecho, t.DataHoraPartida, t.DataHoraChegada, t.Classe, t.CodigoVoo
FROM TrechoVoo t
WHERE t.CodigoVoo IN ('VOO123', 'VOO456')
GROUP BY t.CodigoTrecho
HAVING COUNT(t.CodigoTrecho) > 1;

SELECT c.Nome, c.Email
FROM Cliente c
LEFT JOIN Reserva r ON c.CPF = r.CPF
LEFT JOIN ReservaTrecho rt ON r.CodigoReserva = rt.CodigoReserva
LEFT JOIN TrechoVoo t ON rt.CodigoTrecho = t.CodigoTrecho
WHERE t.CodigoTrecho IS NULL OR YEAR(t.DataHoraPartida) < YEAR(CURDATE()) - 1;

DELIMITER //

CREATE FUNCTION ContarReservas(CPF CHAR(11), dataInicio DATE, dataFim DATE)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE numeroReservas INT;
    SELECT COUNT(*)
    INTO numeroReservas
    FROM Reserva
    WHERE Reserva.CPF = CPF AND Reserva.DataReserva BETWEEN dataInicio AND dataFim;
    RETURN numeroReservas;
END //

DELIMITER ;

