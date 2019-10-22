/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 80012
Source Host           : localhost:3306
Source Database       : shopping

Target Server Type    : MYSQL
Target Server Version : 80012
File Encoding         : 65001

Date: 2019-10-16 14:07:22
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for goods
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `price` float DEFAULT NULL,
  `link` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO `goods` VALUES ('1', '华为huaweiP30', '3660', 'static\\images\\huaweiP30.png');
INSERT INTO `goods` VALUES ('2', '苹果iphoneXR', '5999', 'static\\images\\iphoneXR.png');
INSERT INTO `goods` VALUES ('4', '小米xiaomi9', '1999', 'static\\images\\xiaomi9.png');
INSERT INTO `goods` VALUES ('5', 'OPPO Reno Ace 8GB+128GB 星际蓝 65W超级闪充 90Hz电竞屏 高通骁龙855Plus ', '3199', 'static\\images\\oppo1.png');
INSERT INTO `goods` VALUES ('6', '荣耀10青春版 幻彩渐变 2400万AI自拍 全网通版', '999', 'static\\images\\rongyao.png');
INSERT INTO `goods` VALUES ('7', '荣耀8X 千元屏霸 91%屏占比 2000万AI双摄 4GB+64GB', '999', 'static\\images\\rongyao2.png');
INSERT INTO `goods` VALUES ('8', '一加 OnePlus 7 骁龙855旗舰性能 4800万超清双摄 8GB+256GB ', '2999', 'static\\images\\yijia.png');
INSERT INTO `goods` VALUES ('9', 'Apple iPhone 11 Pro Max (A2220) 256GB 暗夜绿色 移动联通电信4G手', '10899', 'static\\images\\iphone2.png');
INSERT INTO `goods` VALUES ('10', '荣耀20i 3200万AI自拍 超广角三摄 全网通版6GB+64GB 渐变蓝 移动联通', '1099', 'static\\images\\rongyao3.png');
INSERT INTO `goods` VALUES ('11', '荣耀10青春版 幻彩渐变 2400万AI自拍 全网通版', '999', 'static\\images\\rongyao.png');

-- ----------------------------
-- Table structure for login
-- ----------------------------
DROP TABLE IF EXISTS `login`;
CREATE TABLE `login` (
  `user` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `psd` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `country` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sex` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `like` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of login
-- ----------------------------
INSERT INTO `login` VALUES ('admin', '123', 'england', 'male', 'PE,music');
