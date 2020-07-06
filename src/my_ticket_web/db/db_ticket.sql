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
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for `t_left_ticket`
-- ----------------------------
DROP TABLE IF EXISTS `t_left_ticket`;
CREATE TABLE `t_left_ticket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `query_time` datetime DEFAULT NULL,
  `train_no` varchar(50) DEFAULT NULL COMMENT '列车号',
  `train_code` varchar(50) DEFAULT NULL COMMENT '车次',
  `start_station_code` varchar(50) DEFAULT NULL COMMENT '始发站代码',
  `end_station_code` varchar(50) DEFAULT NULL,
  `from_station_code` varchar(50) DEFAULT NULL COMMENT '出发站代码',
  `dest_station_code` varchar(50) DEFAULT NULL COMMENT '目的地代码',
  `start_time` varchar(50) DEFAULT NULL,
  `arrive_time` varchar(50) DEFAULT NULL,
  `run_time` varchar(50) DEFAULT NULL COMMENT '历时',
  `can_buy` varchar(50) DEFAULT NULL COMMENT '能否购买',
  `start_station_date` datetime DEFAULT NULL COMMENT '起始站发车日期',
  `gr_num` varchar(50) DEFAULT NULL COMMENT '高级软卧',
  `qt_num` varchar(50) DEFAULT NULL COMMENT '其他',
  `rw_num` varchar(50) DEFAULT NULL COMMENT '软卧，一等卧',
  `rz_num` varchar(50) DEFAULT NULL COMMENT '软座',
  `tz_num` varchar(50) DEFAULT NULL COMMENT '特等？未知。。。',
  `wz_num` varchar(50) DEFAULT NULL COMMENT '无座',
  `yw_num` varchar(50) DEFAULT NULL COMMENT '硬卧，二等卧',
  `yz_num` varchar(50) DEFAULT NULL COMMENT '硬座',
  `edz_num` varchar(50) DEFAULT NULL COMMENT '二等座',
  `ydz_num` varchar(50) DEFAULT NULL COMMENT '一等座',
  `swz_num` varchar(50) DEFAULT NULL,
  `dw_num` varchar(50) DEFAULT NULL COMMENT '动卧',
  `remark` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for `t_train`
-- ----------------------------
DROP TABLE IF EXISTS `t_train`;
CREATE TABLE `t_train` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `train_date` date DEFAULT NULL,
  `train_type` varchar(4) DEFAULT NULL,
  `train_no` varchar(40) DEFAULT NULL,
  `train_code` varchar(20) DEFAULT NULL,
  `start_station` varchar(40) DEFAULT NULL,
  `end_station` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;