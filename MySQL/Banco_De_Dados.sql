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

