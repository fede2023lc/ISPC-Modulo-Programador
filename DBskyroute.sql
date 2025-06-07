CREATE DATABASE IF NOT EXISTS skyroute;
USE skyroute;

CREATE TABLE clientes (
  cuit BIGINT,
  razon_social varchar(60),
  mail varchar(60),
  PRIMARY KEY (Cuit)
);

CREATE TABLE destinos (
  codigo_destino int AUTO_INCREMENT,
  precio int,
  ciudad varchar(60),
  pais varchar(60),
  PRIMARY KEY (codigo_destino)
);
CREATE TABLE ventas (
  codigo_venta int AUTO_INCREMENT,
  codigo_destino int,
  cuit int,
  fecha_de_venta date, 
  cant_dias_de_viaje int,
  Estado varchar(20),
  PRIMARY KEY (codigo_venta),
  FOREIGN KEY (codigo_destino) REFERENCES destinos(codigo_destino),
  FOREIGN KEY (cuit) REFERENCES clientes(cuit)
);

