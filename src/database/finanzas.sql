/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE IF NOT EXISTS `ges_finanzas` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `ges_finanzas`;

CREATE TABLE IF NOT EXISTS `dinero` (
    `id_dinero` int(11) NOT NULL AUTO_INCREMENT,
    `presupuesto` float NOT NULL DEFAULT 0,
    `id_usuario` int(11) NOT NULL,
    PRIMARY KEY (`id_dinero`),
    KEY `id_usuario` (`id_usuario`),
    CONSTRAINT `dinero` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DELETE FROM `dinero`;

CREATE TABLE IF NOT EXISTS `gastos` (
    `id_gasto` int(11) NOT NULL AUTO_INCREMENT,
    `titulo` varchar(50) DEFAULT NULL,
    `descripcion` varchar(50) DEFAULT NULL,
    `tipo_gasto` varchar(50) DEFAULT NULL,
    `gasto_aprox` float DEFAULT NULL,
    `dinero_usar` int(11) DEFAULT NULL,
    `id_usuario` int(11) DEFAULT NULL,
    PRIMARY KEY (`id_gasto`),
    KEY `id_usuario` (`id_usuario`),
    KEY `dinero` (`dinero_usar`) USING BTREE,
    CONSTRAINT `dinero_gasto` FOREIGN KEY (`dinero_usar`) REFERENCES `dinero` (`id_dinero`) ON DELETE NO ACTION ON UPDATE NO ACTION,
    CONSTRAINT `usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DELETE FROM `gastos`;

CREATE TABLE IF NOT EXISTS `usuario` (
    `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(100) NOT NULL DEFAULT '',
    `password` varchar(300) NOT NULL DEFAULT '',
    `nombre` varchar(300) NOT NULL DEFAULT '',
    `fecha_registro` datetime DEFAULT NULL,
    `ultimo_registro` datetime DEFAULT NULL,
    `foto` varchar(200) DEFAULT NULL,
    PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DELETE FROM `usuario`;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;