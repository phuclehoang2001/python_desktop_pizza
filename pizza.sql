-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th3 23, 2023 lúc 04:49 PM
-- Phiên bản máy phục vụ: 10.4.17-MariaDB
-- Phiên bản PHP: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `pizza`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `base`
--

CREATE TABLE `base` (
  `id` int(11) NOT NULL,
  `display` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `base`
--

INSERT INTO `base` (`id`, `display`) VALUES
(1, 'Dày'),
(2, 'Mỏng giòn'),
(3, 'Viền phô mai'),
(5, 'Viền phô mai xúc xích'),
(4, 'Viền tôm nướng');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `display` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `category`
--

INSERT INTO `category` (`id`, `display`) VALUES
(1, 'Mới'),
(2, 'Công Thức Đặc Biệt'),
(3, 'Hải Sản Cao Cấp'),
(4, 'Thập Cẩm Cao Cấp'),
(5, 'Truyền Thống'),
(7, 'new 2');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `group`
--

CREATE TABLE `group` (
  `id` int(11) NOT NULL,
  `display` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `group`
--

INSERT INTO `group` (`id`, `display`) VALUES
(1, 'Mặc định'),
(3, 'Nhân viên'),
(4, 'Quản trị viên'),
(5, 'Quét rác'),
(2, 'Thành viên');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `group_permission`
--

CREATE TABLE `group_permission` (
  `id` int(11) NOT NULL,
  `group_id` int(11) DEFAULT NULL,
  `permission` varchar(255) DEFAULT NULL,
  `value` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `group_permission`
--

INSERT INTO `group_permission` (`id`, `group_id`, `permission`, `value`) VALUES
(1, 4, 'admin.login', 1),
(2, 4, 'admin.group', 1),
(3, 4, 'admin.user', 1),
(4, 4, 'admin.category', 1),
(5, 4, 'admin.size', 1),
(6, 4, 'admin.base', 1),
(7, 4, 'admin.topping', 1),
(8, 4, 'admin.pizza', 1),
(9, 4, 'admin.order', 1),
(10, 4, 'admin.statistic', 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `order`
--

CREATE TABLE `order` (
  `id` int(11) NOT NULL,
  `customer` varchar(32) DEFAULT NULL,
  `handler` varchar(32) DEFAULT NULL,
  `total_price` decimal(16,2) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `fullname` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `payment_type` int(11) DEFAULT NULL,
  `order_type` int(11) DEFAULT NULL,
  `order_time` time DEFAULT NULL,
  `note` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `order`
--

INSERT INTO `order` (`id`, `customer`, `handler`, `total_price`, `quantity`, `fullname`, `address`, `phone`, `payment_type`, `order_type`, `order_time`, `note`) VALUES
(1, 'hoangphuc', 'admin', '388000.00', 2, 'Phúc Lý', 'ABCD a', '0963852741', 2, 0, '00:00:00', ''),
(2, 'hoangphuc', NULL, '987000.00', 3, '123', 'ABCD b', '0963852741', 0, 0, '00:00:00', ''),
(3, 'hoangphuc', 'admin', '219000.00', 1, '123', 'ABCD c', '0963852741', 0, 0, '00:00:00', ''),
(4, 'admin54', NULL, '516000.00', 4, 'Lê Phúc', 'ABCD, ABCDEF', '0852753156', 1, 1, '10:30:08', ''),
(5, 'admin54', 'admin', '3109000.00', 11, 'Lê Phúc', 'ABCD, ABCDEF', '0852753156', 4, 0, '00:00:00', 'helo'),
(6, '3119410300', NULL, '169000.00', 1, 'Lê Phúc', 'ABCD, ABCDEF', '0147852963', 1, 1, '11:50:08', '1324');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `order_detail`
--

CREATE TABLE `order_detail` (
  `id` int(11) NOT NULL,
  `order_id` int(11) DEFAULT NULL,
  `pizza_detail_id` int(11) DEFAULT NULL,
  `price` decimal(16,2) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `order_detail`
--

INSERT INTO `order_detail` (`id`, `order_id`, `pizza_detail_id`, `price`, `quantity`) VALUES
(1, 1, 74, '219000.00', 1),
(2, 1, 45, '169000.00', 1),
(3, 2, 74, '219000.00', 1),
(4, 2, 81, '369000.00', 1),
(5, 2, 53, '399000.00', 1),
(6, 3, 74, '219000.00', 1),
(7, 4, 12, '129000.00', 4),
(8, 5, 65, '119000.00', 1),
(9, 5, 74, '219000.00', 1),
(10, 5, 75, '219000.00', 1),
(11, 5, 23, '119000.00', 1),
(12, 5, 12, '129000.00', 1),
(13, 5, 13, '209000.00', 1),
(14, 5, 33, '419000.00', 5),
(15, 6, 45, '169000.00', 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `pizza`
--

CREATE TABLE `pizza` (
  `id` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `display` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `pizza`
--

INSERT INTO `pizza` (`id`, `category_id`, `display`, `description`, `image`) VALUES
(1, 2, 'Pizza Hải Sản Đào', 'Tôm, Giăm bông, Đào hòa quyện bùng nổ cùng sốt Thousand Island', 'haisandao.png'),
(2, 3, 'Pizza Hải Sản Cocktail', 'Tôm, cua, giăm bông,... với sốt Thousand Island', 'haisancocktail.png'),
(3, 4, 'Pizza Aloha', 'Thịt nguội, xúc xích tiêu cay và dứa hòa quyện với sốt Thousand Island', 'aloha.png'),
(4, 4, 'Pizza Thịt Xông Khói', 'Thịt giăm bông, thịt xông khói và hai loại rau của ớt xanh, cà chua', 'thitxongkhoi.png'),
(5, 2, 'Pizza Hải Sản Pesto Xanh', 'Tôm, cua, mực và bông cải xanh tươi ngon trên nền sốt Pesto Xanh', 'haisanpestoxanh.png'),
(6, 3, 'Pizza Hải Sản Nhiệt Đới', 'Tôm, nghêu, mực, cua, dứa với sốt Thousand Island', 'haisannhietdoi.png'),
(7, 5, 'Pizza Gà Nướng Dứa', 'Thịt gà mang vị ngọt của dứa kết hợp với vị cay nóng của ớt', 'ganuongdua.png'),
(8, 1, 'Pizza Phượng Hoàng', 'Sự kết hợp giữa thịt Ức ngỗng xông khói châu Âu, cải tím và các loại ớt tạo nên một chiếc bánh tràn đầy hương vị mở ra một năm mới nhiều khởi sắc', 'phuonghoang.png'),
(10, 1, '3r3w', 'dsgsdh', 'haisandao.png');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `pizza_detail`
--

CREATE TABLE `pizza_detail` (
  `id` int(11) NOT NULL,
  `pizza_id` int(11) DEFAULT NULL,
  `size_id` int(11) DEFAULT NULL,
  `base_id` int(11) DEFAULT NULL,
  `price` decimal(16,2) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `pizza_detail`
--

INSERT INTO `pizza_detail` (`id`, `pizza_id`, `size_id`, `base_id`, `price`, `quantity`) VALUES
(1, 1, 1, 1, '169000.00', 0),
(2, 1, 2, 1, '249000.00', 0),
(3, 1, 2, 2, '249000.00', 0),
(4, 1, 2, 3, '299000.00', 0),
(5, 1, 2, 4, '349000.00', 0),
(6, 1, 2, 5, '349000.00', 0),
(7, 1, 3, 1, '329000.00', 0),
(8, 1, 3, 2, '329000.00', 0),
(9, 1, 3, 3, '399000.00', 0),
(10, 1, 3, 4, '469000.00', 0),
(11, 1, 3, 5, '469000.00', 0),
(12, 2, 1, 1, '129000.00', 4),
(13, 2, 2, 1, '209000.00', 4),
(14, 2, 2, 2, '209000.00', 5),
(15, 2, 2, 3, '259000.00', 0),
(16, 2, 2, 4, '309000.00', 0),
(17, 2, 2, 5, '309000.00', 0),
(18, 2, 3, 1, '289000.00', 5),
(19, 2, 3, 2, '289000.00', 5),
(20, 2, 3, 3, '359000.00', 0),
(21, 2, 3, 4, '429000.00', 0),
(22, 2, 3, 5, '429000.00', 0),
(23, 3, 1, 1, '119000.00', 4),
(24, 3, 2, 1, '199000.00', 5),
(25, 3, 2, 2, '199000.00', 5),
(26, 3, 2, 3, '249000.00', 5),
(27, 3, 2, 4, '299000.00', 5),
(28, 3, 2, 5, '299000.00', 5),
(29, 3, 3, 1, '279000.00', 5),
(30, 3, 3, 2, '279000.00', 5),
(31, 3, 3, 3, '349000.00', 5),
(32, 3, 3, 4, '419000.00', 5),
(33, 3, 3, 5, '419000.00', 0),
(34, 4, 1, 1, '119000.00', 5),
(35, 4, 2, 1, '199000.00', 5),
(36, 4, 2, 2, '199000.00', 5),
(37, 4, 2, 3, '249000.00', 5),
(38, 4, 2, 4, '299000.00', 5),
(39, 4, 2, 5, '299000.00', 5),
(40, 4, 3, 1, '279000.00', 5),
(41, 4, 3, 2, '279000.00', 5),
(42, 4, 3, 3, '349000.00', 5),
(43, 4, 3, 4, '419000.00', 5),
(44, 4, 3, 5, '419000.00', 5),
(45, 5, 1, 1, '169000.00', 4),
(46, 5, 2, 1, '249000.00', 5),
(47, 5, 2, 2, '249000.00', 5),
(48, 5, 2, 3, '299000.00', 5),
(49, 5, 2, 4, '349000.00', 5),
(50, 5, 2, 5, '349000.00', 5),
(51, 5, 3, 1, '329000.00', 5),
(52, 5, 3, 2, '329000.00', 5),
(53, 5, 3, 3, '399000.00', 5),
(54, 5, 3, 4, '469000.00', 5),
(55, 5, 3, 5, '469000.00', 5),
(56, 6, 1, 1, '139000.00', 5),
(57, 6, 2, 1, '219000.00', 5),
(58, 6, 2, 2, '219000.00', 5),
(59, 6, 2, 3, '269000.00', 5),
(60, 6, 2, 5, '319000.00', 5),
(61, 6, 3, 1, '299000.00', 5),
(62, 6, 3, 2, '299000.00', 5),
(63, 6, 3, 3, '369000.00', 5),
(64, 6, 3, 5, '439000.00', 5),
(65, 7, 1, 1, '119000.00', 4),
(66, 7, 2, 1, '199000.00', 5),
(67, 7, 2, 2, '199000.00', 5),
(68, 7, 2, 3, '249000.00', 5),
(69, 7, 2, 5, '299000.00', 5),
(70, 7, 3, 1, '279000.00', 5),
(71, 7, 3, 2, '279000.00', 5),
(72, 7, 3, 3, '349000.00', 5),
(73, 7, 3, 5, '349000.00', 5),
(74, 8, 2, 1, '219000.00', 2),
(75, 8, 2, 2, '219000.00', 4),
(76, 8, 2, 3, '269000.00', 5),
(77, 8, 2, 5, '269000.00', 5),
(78, 8, 3, 1, '299000.00', 5),
(79, 8, 3, 2, '299000.00', 5),
(80, 8, 3, 3, '369000.00', 5),
(81, 8, 3, 5, '369000.00', 5),
(93, 10, 3, 3, '10000000.00', 30);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `size`
--

CREATE TABLE `size` (
  `id` int(11) NOT NULL,
  `display` varchar(255) DEFAULT NULL,
  `priority` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `size`
--

INSERT INTO `size` (`id`, `display`, `priority`) VALUES
(1, 'Nhỏ 6\'\'', 1),
(2, 'Vừa 9\'\'', 2),
(3, 'Lớn 12\'\'', 3);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `status`
--

CREATE TABLE `status` (
  `id` int(11) NOT NULL,
  `display` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `status`
--

INSERT INTO `status` (`id`, `display`) VALUES
(1, 'Chờ xác nhận'),
(7, 'Hủy đơn'),
(6, 'Đã giao'),
(2, 'Đang chuẩn bị'),
(3, 'Đang nướng bánh'),
(5, 'Đang vận chuyển'),
(4, 'Đang đóng hộp');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `status_detail`
--

CREATE TABLE `status_detail` (
  `order_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  `time_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `status_detail`
--

INSERT INTO `status_detail` (`order_id`, `status_id`, `time_created`) VALUES
(1, 1, '2022-09-23 14:38:24'),
(1, 2, '2022-09-23 15:10:41'),
(1, 3, '2022-09-23 15:12:25'),
(2, 1, '2022-09-23 15:14:16'),
(2, 7, '2022-09-23 15:14:45'),
(3, 1, '2022-09-23 15:15:53'),
(3, 6, '2022-09-23 15:16:34'),
(4, 1, '2022-10-17 10:45:02'),
(4, 7, '2022-10-24 14:31:10'),
(5, 1, '2022-10-17 10:52:46'),
(5, 2, '2022-11-10 20:43:11'),
(6, 1, '2022-10-17 10:55:04');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `topping`
--

CREATE TABLE `topping` (
  `id` int(11) NOT NULL,
  `display` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `topping`
--

INSERT INTO `topping` (`id`, `display`) VALUES
(13, 'Bông cải xanh'),
(11, 'Cà chua'),
(17, 'Cải tím'),
(4, 'Cua'),
(7, 'Dứa'),
(2, 'Giăm bông'),
(12, 'Mực'),
(14, 'Nghêu'),
(10, 'Ớt xanh'),
(15, 'Thịt gà'),
(8, 'Thịt giăm bông'),
(5, 'Thịt nguội'),
(16, 'Thịt ứt ngỗng'),
(9, 'Thịt xông khói'),
(1, 'Tôm'),
(6, 'Xúc xích tiêu cay'),
(3, 'Đào');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `topping_detail`
--

CREATE TABLE `topping_detail` (
  `pizza_id` int(11) NOT NULL,
  `topping_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `topping_detail`
--

INSERT INTO `topping_detail` (`pizza_id`, `topping_id`) VALUES
(3, 5),
(3, 6),
(3, 7),
(4, 8),
(4, 9),
(4, 10),
(4, 11),
(5, 1),
(5, 4),
(5, 12),
(5, 13),
(6, 1),
(6, 4),
(6, 7),
(6, 12),
(6, 14),
(7, 7),
(7, 15),
(8, 16),
(8, 17);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `user`
--

CREATE TABLE `user` (
  `username` varchar(32) NOT NULL,
  `group_id` int(11) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `fullname` varchar(255) DEFAULT NULL,
  `birth` date DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `user`
--

INSERT INTO `user` (`username`, `group_id`, `password`, `fullname`, `birth`, `address`, `phone`, `email`) VALUES
('3119410300', 1, '$2y$10$fbIWqqqWuSaNxvKLPlXMQeYF62j/U4OABnt2rtzlyLzr3dJjey56y', 'Lê Phúc', '2022-10-08', 'ABCD HCM', '0147852963', 'abc@gmail.com'),
('admin', 4, '$2y$10$QXE8xnq.xDIsoGr1rdK6Hel7MCavVyJDQmUMvGBDYI5iZeZTyJiG6', 'Admin', '2001-01-01', 'TP.HCM', '0123456789', 'email@game.com'),
('admin54', 1, '$2y$10$Bi1fcBs3PhVPeFlZScussuJxAqvzgBoRCEpvL9jA028NftgVcB06q', 'Lê Phúc', '2022-10-06', 'HJS', '0852753156', 'lehoangphuc@gmail.com'),
('hoangphuc', 2, '$2y$10$UM3UWPUtp/l6DZwChNkNRe68okjYAo4iYLdcf2w6y/rus1bSBC/XG', '123', '2022-09-24', 'ABCDHN', '0963852741', 'abc@gmail.com'),
('nhatanh', 2, '$2y$10$QPRf.XycU3Jv9Ot7YHes4.ZhXQCwEIIXJp4X4kbSkh5U89t1CBinO', 'Trần Nhật Anh', '2001-01-01', 'TP.HCM', '0123456789', 'email@game.com');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `user_permission`
--

CREATE TABLE `user_permission` (
  `id` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `permission` varchar(255) DEFAULT NULL,
  `value` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Đang đổ dữ liệu cho bảng `user_permission`
--

INSERT INTO `user_permission` (`id`, `username`, `permission`, `value`) VALUES
(2, '3119410300', 'lock', 0);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `base`
--
ALTER TABLE `base`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `display` (`display`);

--
-- Chỉ mục cho bảng `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Chỉ mục cho bảng `group`
--
ALTER TABLE `group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `display` (`display`);

--
-- Chỉ mục cho bảng `group_permission`
--
ALTER TABLE `group_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `group_permission_fk_id` (`group_id`);

--
-- Chỉ mục cho bảng `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `order_fk_customer` (`customer`),
  ADD KEY `order_fk_handler` (`handler`);

--
-- Chỉ mục cho bảng `order_detail`
--
ALTER TABLE `order_detail`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `order_detail_fk_order_id` (`order_id`),
  ADD KEY `order_detail_fk_pizza_detail_id` (`pizza_detail_id`);

--
-- Chỉ mục cho bảng `pizza`
--
ALTER TABLE `pizza`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `display` (`display`),
  ADD KEY `pizza_fk_category_id` (`category_id`);

--
-- Chỉ mục cho bảng `pizza_detail`
--
ALTER TABLE `pizza_detail`
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `pizza_detail_fk_pizza_id` (`pizza_id`),
  ADD KEY `pizza_detail_fk_size_id` (`size_id`),
  ADD KEY `pizza_detail_fk_base_id` (`base_id`);

--
-- Chỉ mục cho bảng `size`
--
ALTER TABLE `size`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `display` (`display`);

--
-- Chỉ mục cho bảng `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `display` (`display`);

--
-- Chỉ mục cho bảng `status_detail`
--
ALTER TABLE `status_detail`
  ADD PRIMARY KEY (`order_id`,`status_id`),
  ADD KEY `status_details_fk_status_id` (`status_id`);

--
-- Chỉ mục cho bảng `topping`
--
ALTER TABLE `topping`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `display` (`display`);

--
-- Chỉ mục cho bảng `topping_detail`
--
ALTER TABLE `topping_detail`
  ADD PRIMARY KEY (`pizza_id`,`topping_id`),
  ADD KEY `status_details_fk_topping_id` (`topping_id`);

--
-- Chỉ mục cho bảng `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `user_permission_fk_group_id` (`group_id`);

--
-- Chỉ mục cho bảng `user_permission`
--
ALTER TABLE `user_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `user_permission_fk_name` (`username`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `base`
--
ALTER TABLE `base`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT cho bảng `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT cho bảng `group`
--
ALTER TABLE `group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT cho bảng `group_permission`
--
ALTER TABLE `group_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `order`
--
ALTER TABLE `order`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT cho bảng `order_detail`
--
ALTER TABLE `order_detail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT cho bảng `pizza`
--
ALTER TABLE `pizza`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `pizza_detail`
--
ALTER TABLE `pizza_detail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94;

--
-- AUTO_INCREMENT cho bảng `size`
--
ALTER TABLE `size`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT cho bảng `status`
--
ALTER TABLE `status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT cho bảng `topping`
--
ALTER TABLE `topping`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT cho bảng `user_permission`
--
ALTER TABLE `user_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `group_permission`
--
ALTER TABLE `group_permission`
  ADD CONSTRAINT `group_permission_fk_id` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`);

--
-- Các ràng buộc cho bảng `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `order_fk_customer` FOREIGN KEY (`customer`) REFERENCES `user` (`username`),
  ADD CONSTRAINT `order_fk_handler` FOREIGN KEY (`handler`) REFERENCES `user` (`username`);

--
-- Các ràng buộc cho bảng `order_detail`
--
ALTER TABLE `order_detail`
  ADD CONSTRAINT `order_detail_fk_order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`),
  ADD CONSTRAINT `order_detail_fk_pizza_detail_id` FOREIGN KEY (`pizza_detail_id`) REFERENCES `pizza_detail` (`id`);

--
-- Các ràng buộc cho bảng `pizza`
--
ALTER TABLE `pizza`
  ADD CONSTRAINT `pizza_fk_category_id` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`);

--
-- Các ràng buộc cho bảng `pizza_detail`
--
ALTER TABLE `pizza_detail`
  ADD CONSTRAINT `pizza_detail_fk_base_id` FOREIGN KEY (`base_id`) REFERENCES `base` (`id`),
  ADD CONSTRAINT `pizza_detail_fk_pizza_id` FOREIGN KEY (`pizza_id`) REFERENCES `pizza` (`id`),
  ADD CONSTRAINT `pizza_detail_fk_size_id` FOREIGN KEY (`size_id`) REFERENCES `size` (`id`);

--
-- Các ràng buộc cho bảng `status_detail`
--
ALTER TABLE `status_detail`
  ADD CONSTRAINT `status_details_fk_order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`),
  ADD CONSTRAINT `status_details_fk_status_id` FOREIGN KEY (`status_id`) REFERENCES `status` (`id`);

--
-- Các ràng buộc cho bảng `topping_detail`
--
ALTER TABLE `topping_detail`
  ADD CONSTRAINT `status_details_fk_pizza_id` FOREIGN KEY (`pizza_id`) REFERENCES `pizza` (`id`),
  ADD CONSTRAINT `status_details_fk_topping_id` FOREIGN KEY (`topping_id`) REFERENCES `topping` (`id`);

--
-- Các ràng buộc cho bảng `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_permission_fk_group_id` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`);

--
-- Các ràng buộc cho bảng `user_permission`
--
ALTER TABLE `user_permission`
  ADD CONSTRAINT `user_permission_fk_name` FOREIGN KEY (`username`) REFERENCES `user` (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
