-- ----------------------------
-- Table structure for `t_station`
-- ----------------------------
DROP TABLE IF EXISTS `t_station`;
CREATE TABLE `t_station` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `short_name` varchar(20) DEFAULT NULL,
  `full_name` varchar(20) DEFAULT NULL,
  `station_code` varchar(10) DEFAULT NULL,
  `station_pin` varchar(50) DEFAULT NULL,
  `short_name2` varchar(20) DEFAULT NULL,
  `num_code` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3019 DEFAULT CHARSET=utf8mb4;


