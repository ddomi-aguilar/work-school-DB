#CREATE DATABASE vehiculos;

CREATE TABLE `vehiculos`.`autos` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `Marca` VARCHAR(40) NOT NULL,
    `Modelo` VARCHAR(40) NOT NULL,
    `Precio` INT NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;


INSERT INTO vehiculos.autos (Marca, Modelo, Precio) VALUES
("seat", "ibiza", 5000),
("renault", "clio", 18000),
("citroen", "saxo", 2000),
("mercedes", "class", 25000);

#ACTUALIZAR
#UPDATE vehiculos.autos SET Modelo='class' WHERE Modelo='classG';



#VER TABLA
SELECT * FROM vehiculos.autos;
#SELECT Marca FROM vehiculos.autos;

#salir
#exit;

