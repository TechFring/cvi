DROP SCHEMA IF EXISTS `database_cvi`;

CREATE SCHEMA `database_cvi`
DEFAULT CHARACTER SET utf8;

USE `database_cvi`;

CREATE TABLE IF NOT EXISTS `secretaria`(
	`id` INT AUTO_INCREMENT,
    `nome` VARCHAR(255),
    `nome_usuario` VARCHAR(100) UNIQUE NOT NULL,
	`email` VARCHAR(100) UNIQUE NOT NULL,
	`senha` VARCHAR(100) NOT NULL,
    `token` VARCHAR(255),
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `corretor`(
	`id` INT AUTO_INCREMENT,
    `creci` VARCHAR(50) UNIQUE NOT NULL,
    `nome` VARCHAR(255) NOT NULL,
    `email` VARCHAR(100) UNIQUE NOT NULL,
	`senha` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `imovel`(
	`id` INT AUTO_INCREMENT,
    `endereco` VARCHAR(255) NOT NULL,
    `latitude` VARCHAR(100),
    `longitude` VARCHAR(100),
    `tamanho` INT NOT NULL,
    `quartos` INT NOT NULL,
    `banheiros` INT NOT NULL,
    `garagem` INT NOT NULL,
    `descricao` VARCHAR(255) NOT NULL,
    `doc_imovel` VARCHAR(255),
    `doc_proprietario` VARCHAR(255),
    `capa` VARCHAR(255),
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `foto_interior`(
	`id` INT AUTO_INCREMENT,
    `id_imovel` INT,
	`foto` VARCHAR(255),
    PRIMARY KEY(`id`),
	FOREIGN KEY(`id_imovel`) REFERENCES `imovel`(`id`)
    ON DELETE CASCADE
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `visita`(
	`id` INT AUTO_INCREMENT,
    `id_imovel` INT,
    `id_corretor` INT,
    `dia` DATETIME NOT NULL,
    `nome_cliente` VARCHAR(255),
    `telefone_cliente` VARCHAR(100),
    PRIMARY KEY(`id`),
    FOREIGN KEY(`id_imovel`) REFERENCES `imovel`(`id`)
    ON DELETE CASCADE,
    FOREIGN KEY(`id_corretor`) REFERENCES `corretor`(`id`)
    ON DELETE CASCADE
) ENGINE = InnoDB;