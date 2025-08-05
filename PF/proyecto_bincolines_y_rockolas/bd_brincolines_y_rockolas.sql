-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-08-2025 a las 19:04:20
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_brincolines_y_rockolas`
--
CREATE DATABASE IF NOT EXISTS `bd_brincolines_y_rockolas` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `bd_brincolines_y_rockolas`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `brincolines`
--

CREATE TABLE `brincolines` (
  `id` int(11) NOT NULL,
  `nombre_cliente` varchar(100) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `fecha` date DEFAULT curdate(),
  `duracion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rockolas`
--

CREATE TABLE `rockolas` (
  `id` int(11) NOT NULL,
  `nombre_cliente` varchar(100) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `fecha` date DEFAULT curdate(),
  `duracion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `apellidos` varchar(60) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` date NOT NULL,
  `fecha` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `apellidos`, `email`, `password`, `fecha`) VALUES
(1, 'ANTONIO', 'ASDASD', 'añoña@gmail.com', '0000-00-00', '2025-07-23 22:31:48'),
(2, 'ALONDRA', 'GONZALEZ', 'alo@gmail.com', '0000-00-00', '2025-07-24 08:44:18'),
(3, 'ANTONIO', 'QWEQWE', 'antonio1', '0000-00-00', '2025-07-24 21:57:32'),
(4, 'O', 'O', 'o', '0000-00-00', '2025-07-28 19:35:03'),
(5, 'DIEGO', '123', 'diego', '0000-00-00', '2025-07-28 19:48:30'),
(6, 'PEPE', 'AS', 'pepe', '0000-00-00', '2025-08-05 11:00:56');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `brincolines`
--
ALTER TABLE `brincolines`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `rockolas`
--
ALTER TABLE `rockolas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `brincolines`
--
ALTER TABLE `brincolines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `rockolas`
--
ALTER TABLE `rockolas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
