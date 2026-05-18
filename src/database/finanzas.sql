-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.28-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.15.0.7171
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para ges_finanzas
CREATE DATABASE IF NOT EXISTS `ges_finanzas` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `ges_finanzas`;

-- Volcando estructura para tabla ges_finanzas.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL DEFAULT '',
  `password` varchar(300) NOT NULL DEFAULT '',
  `nombre` varchar(300) NOT NULL DEFAULT '',
  `fecha_registro` datetime DEFAULT NULL,
  `ultimo_registro` datetime DEFAULT NULL,
  `foto` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla ges_finanzas.usuario: ~3 rows (aproximadamente)
DELETE FROM `usuario`;
INSERT INTO `usuario` (`id_usuario`, `email`, `password`, `nombre`, `fecha_registro`, `ultimo_registro`, `foto`) VALUES
	(1, 'admin@gmail.com', '$2b$12$0kVL5yxk7kJ1M6QTLjxTleTJvDQm.YgxC6zTfpHXwTI9v5LyCWVbK', 'Admin', '2026-05-14 00:00:00', '2026-05-14 10:45:27', 'Default.webp'),
	(2, '23308060610335@cetis61.edu.mx', '$2b$12$/BUePOsjWU6YJFzhnKNPeuojjwfTPJFihWqUgCr1WXurraGzU09vC', 'Antonio', '2026-05-18 00:00:00', '2026-05-18 08:42:57', 'Default.webp'),
	(3, '23308060610320@cetis61.edu.mx', '$2b$12$2Cv1v6vx0Loo50hIi2aa0upN1X8OVwl3f0BOr/CUdwU8sYHNrMpIu', 'Luis Angel', '2026-05-18 00:00:00', NULL, 'Default.webp');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
