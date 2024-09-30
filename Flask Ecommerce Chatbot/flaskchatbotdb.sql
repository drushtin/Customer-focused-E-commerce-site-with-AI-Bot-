-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 18, 2023 at 03:11 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flaskchatbotdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `userdata`
--

CREATE TABLE `userdata` (
  `id` int(11) NOT NULL,
  `Userid` varchar(50) DEFAULT NULL,
  `Fname` varchar(50) DEFAULT NULL,
  `Lname` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Pswd` varchar(50) DEFAULT NULL,
  `Phone` varchar(50) DEFAULT NULL,
  `Addr` varchar(4000) DEFAULT NULL,
  `Pcode` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userdata`
--

INSERT INTO `userdata` (`id`, `Userid`, `Fname`, `Lname`, `Email`, `Pswd`, `Phone`, `Addr`, `Pcode`) VALUES
(1, 'User41559', 'sinchu', 'hs', 'armonishashetty@gmail.com', '12345', '9876543210', 'hnp', '573201'),
(2, 'User64118', 'sinchu', 'hs', 'sinch@gmail.com', '12345', '6876543210', 'hnp', '573201'),
(3, 'User76350', 'sinchu', 'hs', 'sinnch@gmail.com', 'zxcv', '9876543210', 'hnp', '573201'),
(4, 'User18480', 'monisha', 't m', 'monisha22@gmail.com', 'azsxdc', '9874561239', 'hsn', '572312'),
(5, 'User26650', 'deepguru', 'grs', 'dg123@gmail.com', 'deep', '8277198006', 'hnp', '573211'),
(6, 'User14216', 'sinchu', 'hs', 'sinchh@gmail.com', 'zxcvb', '9876543210', 'hnp', '573201');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `userdata`
--
ALTER TABLE `userdata`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `userdata`
--
ALTER TABLE `userdata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
