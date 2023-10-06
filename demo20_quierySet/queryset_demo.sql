-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 03, 2023 at 04:01 PM
-- Server version: 8.0.32
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `queryset_demo`
--

-- --------------------------------------------------------

--
-- Table structure for table `app1_employee`
--

DROP TABLE IF EXISTS `app1_employee`;
CREATE TABLE IF NOT EXISTS `app1_employee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `emp_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `salary` int DEFAULT NULL,
  `city` varchar(50) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `app1_employee`
--

INSERT INTO `app1_employee` (`id`, `emp_id`, `name`, `salary`, `city`, `date`) VALUES
(1, 101, 'Ankit', 1023214565, 'Mars', '2023-10-03'),
(2, 102, 'Saurabh', 1023564778, 'Jupiter', '2023-10-03'),
(3, 103, 'Rahul', 356478956, 'Venus', '2023-10-03'),
(4, 104, 'Karan', 1023, 'no mans land', '2023-10-03'),
(5, 105, 'Abhishek', 1023457895, 'Neptune', '2023-10-03'),
(6, 106, 'Vijay', 1266547895, 'Uranus', '2023-10-03'),
(7, 107, 'Sunil', 10236547, 'Pluto', '2023-10-03'),
(8, 108, 'Rajesh', 102365, 'Mumbai', '2023-10-03'),
(9, 109, 'Ramesh', 102365478, 'Delhi', '2023-10-03'),
(10, 110, 'Brijesh', 102364, 'Jaipur', '2023-10-03');

-- --------------------------------------------------------

--
-- Table structure for table `app1_employee2`
--

DROP TABLE IF EXISTS `app1_employee2`;
CREATE TABLE IF NOT EXISTS `app1_employee2` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `emp_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `salary` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `stu_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `app1_employee2`
--

INSERT INTO `app1_employee2` (`id`, `emp_id`, `name`, `city`, `date`, `salary`) VALUES
(1, 101, 'Vibhuti Narayan Mishra', 'Kanpur', '2023-10-03', 456546),
(2, 102, 'Manmohan Tiwari', 'Kanpur', '2023-10-03', 456545654),
(3, 103, 'Happu Singh', 'Kanpur', '2023-10-03', 4564654),
(4, 104, 'Champak laal jayanti laal gada', 'Mumbai', '2023-10-03', 45656),
(5, 105, 'Jethalal Champak Laal gada', 'Mumbai', '2023-10-03', 44525),
(6, 106, 'Taarak Mehta', 'Mumbai', '2023-10-03', 2121),
(7, 107, 'Ankit', 'Delhi', '2023-10-03', 1236544),
(8, 108, 'Abhishek', 'Delhi', '2023-10-03', 1256547895),
(9, 109, 'Saurabh', 'Jhakarkatti', '2023-10-03', 545987458),
(10, 110, 'Mustafa', 'Jhakkarkati', '2023-10-03', 2211);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add employee', 7, 'add_employee'),
(26, 'Can change employee', 7, 'change_employee'),
(27, 'Can delete employee', 7, 'delete_employee'),
(28, 'Can view employee', 7, 'view_employee'),
(29, 'Can add student', 8, 'add_student'),
(30, 'Can change student', 8, 'change_student'),
(31, 'Can delete student', 8, 'delete_student'),
(32, 'Can view student', 8, 'view_student'),
(33, 'Can add employee2', 8, 'add_employee2'),
(34, 'Can change employee2', 8, 'change_employee2'),
(35, 'Can delete employee2', 8, 'delete_employee2'),
(36, 'Can view employee2', 8, 'view_employee2');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$VCNCNMamwyINhMTvfUDL0H$JEOI3Qr0FNmm4x8Ij49EMK7t+hBtbGUl+kQrTpbtDKI=', '2023-10-03 15:45:37.376891', 1, 'admin', '', '', 'admin123@gmai.com', 1, 1, '2023-10-03 15:45:20.061482');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-10-03 15:46:02.695871', '1', 'Employee object (1)', 1, '[{\"added\": {}}]', 7, 1),
(2, '2023-10-03 15:46:19.187142', '2', 'Employee object (2)', 1, '[{\"added\": {}}]', 7, 1),
(3, '2023-10-03 15:46:44.776349', '3', 'Employee object (3)', 1, '[{\"added\": {}}]', 7, 1),
(4, '2023-10-03 15:47:07.034240', '4', 'Employee object (4)', 1, '[{\"added\": {}}]', 7, 1),
(5, '2023-10-03 15:47:29.953014', '5', 'Employee object (5)', 1, '[{\"added\": {}}]', 7, 1),
(6, '2023-10-03 15:48:25.945681', '6', 'Employee object (6)', 1, '[{\"added\": {}}]', 7, 1),
(7, '2023-10-03 15:48:52.615913', '7', 'Employee object (7)', 1, '[{\"added\": {}}]', 7, 1),
(8, '2023-10-03 15:49:15.652064', '8', 'Employee object (8)', 1, '[{\"added\": {}}]', 7, 1),
(9, '2023-10-03 15:49:37.312694', '9', 'Employee object (9)', 1, '[{\"added\": {}}]', 7, 1),
(10, '2023-10-03 15:50:19.754620', '10', 'Employee object (10)', 1, '[{\"added\": {}}]', 7, 1),
(11, '2023-10-03 15:50:50.131742', '1', 'Student object (1)', 1, '[{\"added\": {}}]', 8, 1),
(12, '2023-10-03 15:51:15.681334', '2', 'Student object (2)', 1, '[{\"added\": {}}]', 8, 1),
(13, '2023-10-03 15:51:34.265479', '3', 'Student object (3)', 1, '[{\"added\": {}}]', 8, 1),
(14, '2023-10-03 15:52:33.655044', '4', 'Student object (4)', 1, '[{\"added\": {}}]', 8, 1),
(15, '2023-10-03 15:52:52.247250', '5', 'Student object (5)', 1, '[{\"added\": {}}]', 8, 1),
(16, '2023-10-03 15:53:21.456125', '6', 'Student object (6)', 1, '[{\"added\": {}}]', 8, 1),
(17, '2023-10-03 15:54:40.403413', '7', 'Student object (7)', 1, '[{\"added\": {}}]', 8, 1),
(18, '2023-10-03 15:57:28.537658', '7', 'Student object (7)', 2, '[{\"changed\": {\"fields\": [\"Salary\"]}}]', 8, 1),
(19, '2023-10-03 15:57:35.281262', '6', 'Student object (6)', 2, '[{\"changed\": {\"fields\": [\"Salary\"]}}]', 8, 1),
(20, '2023-10-03 15:57:40.346684', '5', 'Student object (5)', 2, '[{\"changed\": {\"fields\": [\"Salary\"]}}]', 8, 1),
(21, '2023-10-03 15:57:43.856594', '5', 'Student object (5)', 2, '[]', 8, 1),
(22, '2023-10-03 15:57:46.921222', '4', 'Student object (4)', 2, '[{\"changed\": {\"fields\": [\"Salary\"]}}]', 8, 1),
(23, '2023-10-03 15:57:50.521028', '2', 'Student object (2)', 2, '[{\"changed\": {\"fields\": [\"Salary\"]}}]', 8, 1),
(24, '2023-10-03 15:57:53.512893', '1', 'Student object (1)', 2, '[{\"changed\": {\"fields\": [\"Salary\"]}}]', 8, 1),
(25, '2023-10-03 15:57:58.977542', '7', 'Student object (7)', 2, '[]', 8, 1),
(26, '2023-10-03 15:58:01.530957', '6', 'Student object (6)', 2, '[]', 8, 1),
(27, '2023-10-03 15:58:03.480990', '5', 'Student object (5)', 2, '[]', 8, 1),
(28, '2023-10-03 15:58:04.976873', '4', 'Student object (4)', 2, '[]', 8, 1),
(29, '2023-10-03 15:58:11.112189', '3', 'Student object (3)', 2, '[{\"changed\": {\"fields\": [\"Salary\"]}}]', 8, 1),
(30, '2023-10-03 15:58:13.250185', '3', 'Student object (3)', 2, '[]', 8, 1),
(31, '2023-10-03 15:58:15.606867', '4', 'Student object (4)', 2, '[]', 8, 1),
(32, '2023-10-03 15:58:17.185801', '3', 'Student object (3)', 2, '[]', 8, 1),
(33, '2023-10-03 15:58:19.666235', '2', 'Student object (2)', 2, '[]', 8, 1),
(34, '2023-10-03 15:58:21.200879', '1', 'Student object (1)', 2, '[]', 8, 1),
(35, '2023-10-03 15:58:42.786408', '8', 'Student object (8)', 1, '[{\"added\": {}}]', 8, 1),
(36, '2023-10-03 15:59:09.786623', '9', 'Student object (9)', 1, '[{\"added\": {}}]', 8, 1),
(37, '2023-10-03 15:59:25.920237', '10', 'Student object (10)', 1, '[{\"added\": {}}]', 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'app1', 'employee'),
(8, 'app1', 'employee2'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-10-03 15:42:14.370462'),
(2, 'auth', '0001_initial', '2023-10-03 15:42:14.652226'),
(3, 'admin', '0001_initial', '2023-10-03 15:42:14.745972'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-10-03 15:42:14.761597'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-10-03 15:42:14.761597'),
(6, 'app1', '0001_initial', '2023-10-03 15:42:14.777221'),
(7, 'app1', '0002_students', '2023-10-03 15:42:14.792845'),
(8, 'app1', '0003_alter_students_result', '2023-10-03 15:42:14.808471'),
(9, 'app1', '0004_rename_students_student', '2023-10-03 15:42:14.824094'),
(10, 'app1', '0005_employee_date_student_date_alter_student_result', '2023-10-03 15:42:14.855344'),
(11, 'contenttypes', '0002_remove_content_type_name', '2023-10-03 15:42:14.917842'),
(12, 'auth', '0002_alter_permission_name_max_length', '2023-10-03 15:42:14.949090'),
(13, 'auth', '0003_alter_user_email_max_length', '2023-10-03 15:42:14.980339'),
(14, 'auth', '0004_alter_user_username_opts', '2023-10-03 15:42:14.995962'),
(15, 'auth', '0005_alter_user_last_login_null', '2023-10-03 15:42:15.042841'),
(16, 'auth', '0006_require_contenttypes_0002', '2023-10-03 15:42:15.042841'),
(17, 'auth', '0007_alter_validators_add_error_messages', '2023-10-03 15:42:15.058461'),
(18, 'auth', '0008_alter_user_username_max_length', '2023-10-03 15:42:15.105334'),
(19, 'auth', '0009_alter_user_last_name_max_length', '2023-10-03 15:42:15.152208'),
(20, 'auth', '0010_alter_group_name_max_length', '2023-10-03 15:42:15.167833'),
(21, 'auth', '0011_update_proxy_permissions', '2023-10-03 15:42:15.183457'),
(22, 'auth', '0012_alter_user_first_name_max_length', '2023-10-03 15:42:15.214706'),
(23, 'sessions', '0001_initial', '2023-10-03 15:42:15.245955'),
(24, 'app1', '0006_rename_stu_id_student_emp_id_remove_student_result_and_more', '2023-10-03 15:56:51.297562'),
(25, 'app1', '0007_rename_student_employee2', '2023-10-03 16:00:11.400984');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('rw2iokxpxuuah5zewjv91a99es6oc219', '.eJxVjEEOwiAQRe_C2hCggIxL9z0DGYZBqoYmpV0Z765NutDtf-_9l4i4rTVunZc4ZXERWpx-t4T04LaDfMd2myXNbV2mJHdFHrTLcc78vB7u30HFXr81BbDgikXrNGjl0CijUyjgjNYmFDoDEHmjbPGuMDokNfhAA1tOXlnx_gC4AjcU:1qnhab:EFRa5xYFqEEHHWFBPXy2rjntu9EhHQTK8k-uxz9UGVo', '2023-10-17 15:45:37.378889');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
