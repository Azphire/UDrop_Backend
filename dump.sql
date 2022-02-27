CREATE DATABASE  IF NOT EXISTS `Yudi` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `Yudi`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 121.199.77.139    Database: Yudi
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CHNAuthor`
--

DROP TABLE IF EXISTS `CHNAuthor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CHNAuthor` (
  `CHNAuthorId` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `dynasty` varchar(45) DEFAULT NULL,
  `introduction` text,
  PRIMARY KEY (`CHNAuthorId`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CHNAuthor`
--

LOCK TABLES `CHNAuthor` WRITE;
/*!40000 ALTER TABLE `CHNAuthor` DISABLE KEYS */;
INSERT INTO `CHNAuthor` VALUES (0,'佚名','不详','此人作品遍地开花，跨越诸多朝代经久不衰，风格多变，神乎其神。'),(1,'李白','唐','李白（701年—762年12月），字太白，号青莲居士，又号“谪仙人”，唐代伟大的浪漫主义诗人，被后人誉为“诗仙”，与杜甫并称为“李杜”，为了与另两位诗人李商隐与杜牧即“小李杜”区别，杜甫与李白又合称“大李杜”。《旧唐书》记载李白为山东人；《新唐书》记载，李白为兴圣皇帝李暠九世孙，与李唐诸王同宗。其人爽朗大方，爱饮酒作诗，喜交友。\n李白有《李太白集》传世，诗作中多以醉时写的，代表作有《望庐山瀑布》《行路难》《蜀道难》《将进酒》《早发白帝城》等多首。李白所作词赋，宋人已有传记（如文莹《湘山野录》卷上），就其开创意义及艺术成就而言，“李白词”享有极为崇高的地位。'),(2,'杜甫','唐','杜甫（712年2月12日～770年），字子美，自号少陵野老，唐代伟大的现实主义诗人，与李白合称“李杜”。出生于河南巩县，原籍湖北襄阳。为了与另两位诗人李商隐与杜牧即“小李杜”区别，杜甫与李白又合称“大李杜”，杜甫也常被称为“老杜”。杜甫的思想核心是仁政思想，他有“致君尧舜上，再使风俗淳”的宏伟抱负。杜甫虽然在世时名声并不显赫，但后来声名远播，对中国文学和日本文学都产生了深远的影响。杜甫共有约1500首诗歌被保留了下来，大多集于《杜工部集》。 大历五年（770年）冬，病逝，享年五十九岁。杜甫在中国古典诗歌中的影响非常深远，被后人称为“诗圣”，他的诗被称为“诗史”。后世称其杜拾遗、杜工部，也称他杜少陵、杜草堂。'),(4,'王昌龄','唐',NULL),(5,'孟浩然','唐',NULL),(6,'贾岛','唐',NULL),(7,'王维','唐',NULL),(8,'王之涣','唐',NULL),(9,'王翰','唐',NULL),(10,'杜牧','唐',NULL),(11,'张继','唐',NULL),(12,'刘禹锡','唐','一段介绍。'),(13,'诸葛亮','汉','孔明大哥。'),(14,'屈原','先秦','端午节放假。'),(15,'陶渊明','东晋','快乐种田人');
/*!40000 ALTER TABLE `CHNAuthor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CHNPassage`
--

DROP TABLE IF EXISTS `CHNPassage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CHNPassage` (
  `CHNPassageId` int NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `grade` varchar(45) DEFAULT NULL,
  `version` varchar(45) DEFAULT NULL,
  `content` varchar(1000) NOT NULL,
  `category` int NOT NULL DEFAULT '0',
  `CHNAuthorId` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`CHNPassageId`),
  KEY `CHNPassage_CHNAuthor_CHNAuthorId_fk` (`CHNAuthorId`),
  CONSTRAINT `CHNPassage_CHNAuthor_CHNAuthorId_fk` FOREIGN KEY (`CHNAuthorId`) REFERENCES `CHNAuthor` (`CHNAuthorId`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CHNPassage`
--

LOCK TABLES `CHNPassage` WRITE;
/*!40000 ALTER TABLE `CHNPassage` DISABLE KEYS */;
INSERT INTO `CHNPassage` VALUES (1,'现代诗精选一篇','7','人教版','远看大石头，近看石头大',0,0),(2,'出塞','9','苏教版','秦时明月汉时关，万里长征人未还，但使龙城飞将在，不教胡马度阴山',0,4),(3,'春晓','1','苏教版','春眠不觉晓，处处闻啼鸟，夜来风雨声，花落知多少',0,5),(4,'早发白帝城','6','苏教版','朝辞白帝彩云间，千里江陵一日还，两岸猿声啼不住，轻舟已过万重山',0,1),(5,'杂诗','9','苏教版','君自故乡来，应知故乡事，来日绮窗前，寒梅著花未',0,7),(6,'寻隐者不遇','3','苏教版','松下问童子，言师采药去，只在此山中，云深不知处',0,6),(7,'九月九日忆山东兄弟','3','苏教版','独在异乡为异客，每逢佳节倍思亲，遥知兄弟登高处，遍插茱萸少一人',0,7),(8,'登鹳雀楼','4','苏教版','白日依山尽，黄河入海流，欲穷千里目，更上一层楼',0,8),(9,'凉州词','5','苏教版','葡萄美酒夜光杯，欲饮琵琶马上催，醉卧沙场君莫笑，古来征战几人回',0,9),(10,'赤壁','8','苏教版','折戟沉沙铁未销，自将磨洗认前朝，东风不与周郎便，铜雀春深锁二乔',0,10),(11,'相思','9','人教版','红豆生南国，春来发几枝，愿君多采颉，此物最相思',0,7),(12,'枫桥夜泊','5','苏教版','月落乌啼霜满天，江枫渔火对愁眠，姑苏城外寒山寺，夜半钟声到客船',0,11),(13,'春望','8','苏教版','国破山河在，城春草木深，感时花溅泪，恨别鸟惊心，烽火连三月，家书抵万金，白头搔更短，浑欲不胜簪',0,2),(15,'陋室铭',NULL,NULL,'山不在高，有仙则名。水不在深，有龙则灵。斯是陋室，惟吾德馨。苔痕上阶绿，草色入帘青。谈笑有鸿儒，往来无白丁。可以调素琴，阅金经。无丝竹之乱耳，无案牍之劳形。南阳诸葛庐，西蜀子云亭。孔子云：何陋之有？',1,12),(16,'黄鹤楼送孟浩然之广陵',NULL,NULL,'故人西辞黄鹤楼，烟花三月下扬州。孤帆远影碧空尽，唯见长江天际流。',0,1),(17,'静夜思',NULL,NULL,'床前明月光，疑是地上霜。举头望明月，低头思故乡。',0,1),(18,'出师表',NULL,NULL,'先帝创业未半而中道崩殂，今天下三分，益州疲弊，此诚危急存亡之秋也。然侍卫之臣不懈于内，忠志之士忘身于外者，盖追先帝之殊遇，欲报之于陛下也。诚宜开张圣听，以光先帝遗德，恢弘志士之气，不宜妄自菲薄，引喻失义，以塞忠谏之路也。',1,13),(19,'离骚',NULL,NULL,'长太息以掩涕兮，哀民生之多艰。余虽好修姱以鞿羁兮，謇朝谇而夕替。既替余以蕙纕兮，又申之以揽茝。亦余心之所善兮，虽九死其犹未悔。灵修之浩荡兮，终不察夫民心。众女嫉余之蛾眉兮，谣诼谓余以善淫。固时俗之工巧兮，偭规矩而改错。背绳墨以追曲兮，竞周容以为度。忳郁邑余侘傺兮，吾独穷困乎此时也。宁溘死以流亡兮，余不忍为此态也。鸷鸟之不群兮，自前世而固然。何方圜之能周兮，夫孰异道而相安？屈心而抑志兮，忍尤而攘诟。伏清白以死直兮，固前圣之所厚。悔相道之不察兮，延伫乎吾将反。回朕车以复路兮，及行迷之未远。步余马于兰皋兮，驰椒丘且焉止息。进不入以离尤兮，退将复修吾初服。制芰荷以为衣兮，集芙蓉以为裳。不吾知其亦已兮，苟余情其信芳。高余冠之岌岌兮，长余佩之陆离。芳与泽其杂糅兮，唯昭质其犹未亏。忽反顾以游目兮，将往观乎四荒。佩缤纷其繁饰兮，芳菲菲其弥章。民生各有所乐兮，余独好修以为常。虽体解吾犹未变兮，岂余心之可惩。',0,14),(20,'桃花源记',NULL,NULL,'晋太元中，武陵人捕鱼为业。缘溪行，忘路之远近。忽逢桃花林，夹岸数百步，中无杂树，芳草鲜美，落英缤纷。渔人甚异之，复前行，欲穷其林。林尽水源，便得一山，山有小口，仿佛若有光。便舍船，从口入。初极狭，才通人。复行数十步，豁然开朗。土地平旷，屋舍俨然，有良田、美池、桑竹之属。阡陌交通，鸡犬相闻。其中往来种作，男女衣着，悉如外人。黄发垂髫，并怡然自乐。见渔人，乃大惊，问所从来。具答之。便要还家，设酒杀鸡作食。村中闻有此人，咸来问讯。自云先世避秦时乱，率妻子邑人来此绝境，不复出焉，遂与外人间隔。问今是何世，乃不知有汉，无论魏晋。此人一一为具言所闻，皆叹惋。余人各复延至其家，皆出酒食。停数日，辞去。此中人语云：“不足为外人道也。”既出，得其船，便扶向路，处处志之。及郡下，诣太守，说如此。太守即遣人随其往，寻向所志，遂迷，不复得路。南阳刘子骥，高尚士也，闻之，欣然规往。未果，寻病终，后遂无问津者。',1,15),(21,'蜀道难',NULL,NULL,'噫吁嚱，危乎高哉！蜀道之难，难于上青天！蚕丛及鱼凫，开国何茫然！尔来四万八千岁，不与秦塞通人烟。西当太白有鸟道，可以横绝峨嵋巅。地崩山摧壮士死，然后天梯石栈方钩连。上有六龙回日之高标，下有冲波逆折之回川。黄鹤之飞尚不得过，猿猱欲度愁攀援。青泥何盘盘，百步九折萦岩峦。扪参历井仰胁息，以手抚膺坐长叹。问君西游何时还？畏途巉岩不可攀。但见悲鸟号古木，雄飞从雌绕林间。又闻子规啼夜月，愁空山。蜀道之难，难于上青天，使人听此凋朱颜。连峰去天不盈尺，枯松倒挂倚绝壁。飞湍瀑流争喧豗，砯崖转石万壑雷。其险也若此，嗟尔远道之人，胡为乎来哉。剑阁峥嵘而崔嵬，一夫当关，万夫莫开。所守或匪亲，化为狼与豺。朝避猛虎，夕避长蛇，磨牙吮血，杀人如麻。锦城虽云乐，不如早还家。蜀道之难，难于上青天，侧身西望长咨嗟。',0,1);
/*!40000 ALTER TABLE `CHNPassage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CHNPassageRecite`
--

DROP TABLE IF EXISTS `CHNPassageRecite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CHNPassageRecite` (
  `userId` int NOT NULL,
  `CHNPassageId` int NOT NULL,
  `error` int NOT NULL,
  `recite` text,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`userId`,`CHNPassageId`,`time`),
  KEY `CHNPassageId_idx` (`CHNPassageId`),
  CONSTRAINT `CHNPassageId` FOREIGN KEY (`CHNPassageId`) REFERENCES `CHNPassage` (`CHNPassageId`),
  CONSTRAINT `userId` FOREIGN KEY (`userId`) REFERENCES `User` (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CHNPassageRecite`
--

LOCK TABLES `CHNPassageRecite` WRITE;
/*!40000 ALTER TABLE `CHNPassageRecite` DISABLE KEYS */;
INSERT INTO `CHNPassageRecite` VALUES (1,1,4,'3,4','2022-02-27 01:52:23');
/*!40000 ALTER TABLE `CHNPassageRecite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CHNQuestion`
--

DROP TABLE IF EXISTS `CHNQuestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CHNQuestion` (
  `CHNQuestionId` int NOT NULL AUTO_INCREMENT,
  `question` varchar(200) NOT NULL,
  `answer` varchar(200) NOT NULL,
  `grade` int DEFAULT NULL,
  PRIMARY KEY (`CHNQuestionId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CHNQuestion`
--

LOCK TABLES `CHNQuestion` WRITE;
/*!40000 ALTER TABLE `CHNQuestion` DISABLE KEYS */;
INSERT INTO `CHNQuestion` VALUES (1,'请说出“铁骑突出刀枪鸣”的上一句','银瓶乍破水浆迸',11),(2,'请说出“轻舟已过万重山”的上一句','两岸猿声啼不住',6),(3,'请说出“铜雀春深锁二乔”的上一句','东风不与周郎便',9),(4,'请说出“秦时明月汉时关”的下一句','万里长征人未还',9);
/*!40000 ALTER TABLE `CHNQuestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CHNQuestionRecord`
--

DROP TABLE IF EXISTS `CHNQuestionRecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CHNQuestionRecord` (
  `userId` int NOT NULL,
  `CHNQuestionId` int NOT NULL,
  `time` datetime NOT NULL,
  `correct` int NOT NULL COMMENT '正确为1，错误为0',
  PRIMARY KEY (`userId`,`CHNQuestionId`,`time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CHNQuestionRecord`
--

LOCK TABLES `CHNQuestionRecord` WRITE;
/*!40000 ALTER TABLE `CHNQuestionRecord` DISABLE KEYS */;
INSERT INTO `CHNQuestionRecord` VALUES (1,1,'2021-06-02 20:46:11',1);
/*!40000 ALTER TABLE `CHNQuestionRecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Collection`
--

DROP TABLE IF EXISTS `Collection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Collection` (
  `collection` text,
  `userId` int NOT NULL,
  PRIMARY KEY (`userId`),
  CONSTRAINT `Collection_fk` FOREIGN KEY (`userId`) REFERENCES `User` (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Collection`
--

LOCK TABLES `Collection` WRITE;
/*!40000 ALTER TABLE `Collection` DISABLE KEYS */;
INSERT INTO `Collection` VALUES ('{\"18\": \"2022-02-26 19:02:45\"}',2),('{\"17\": \"2022-02-26 18:33:08\", \"9\": \"2022-02-27 10:17:54\"}',3),('{\"13\": \"2022-02-26 18:03:28\"}',5),('{\"8\": \"2022-02-26 10:28:59\"}',6);
/*!40000 ALTER TABLE `Collection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Game`
--

DROP TABLE IF EXISTS `Game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Game` (
  `gameId` int NOT NULL AUTO_INCREMENT,
  `game` text NOT NULL,
  PRIMARY KEY (`gameId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Game`
--

LOCK TABLES `Game` WRITE;
/*!40000 ALTER TABLE `Game` DISABLE KEYS */;
INSERT INTO `Game` VALUES (1,'{\"title\": \"三体·黑暗森林\", \"endings\": [1, 4, 6, 7, 8, 9], \"0\": {\"content\": \"三体世界危机降临，三体舰队将在四百年后到达地球，作为一名海军现役军官，你现在面临着抉择，是继续服役，或者参与支援未来计划、冬眠四百年加入未来太空军。你要如何选择呢，继续，或者冬眠？\", \"choices\": {\"继续\":1,\"冬眠\":2}}, \"1\": {\"content\": \"你度过了充实而有意义的一生，即使大低谷时期也没对你造成太严重的影响，三体世界与人类的未来与你无关。\"}, \"2\": {\"content\": \"你在四百年后醒来，短暂地适应了全新的人类社会，紧接着，你需要被编入新太空军编制中。你可以申请加入的战舰有：自然选择号，量子号，蓝色空间号，万有引力号。你的选择是？\", \"choices\": {\"自然选择\":3,\"量子\":4,\"蓝色空间\":5,\"万有引力\":6}}, \"3\": {\"content\": \"你的舰长是和你一同醒来的章北海，在太空军准备迎接水滴的到来时，他选择了逃亡。几艘战舰追捕你们而来，但随之你们收到消息，人类舰队被三体文明毁灭殆尽，你们是仅存的五艘战舰。但战舰上的资源显然不足以让你们存活到下一个宜居行星，你开始考虑要不要驾驶救生舱独自逃离去木星。你的选择是，逃走，或者留下？\", \"choices\":{\"逃走\":7,\"留下\":8}}, \"4\": {\"content\": \"你们战舰接受了一项光荣的任务，跟随丁仪博士前往迎接三体文明的信物。但形似水滴的信物不是圣母的眼泪，它毁灭了现存人类舰队。\"}, \"5\": {\"content\": \"你们舰队前去追击逃离的自然选择号，但随之你们收到消息，人类舰队被三体文明毁灭殆尽，你们是仅存的五艘战舰。但战舰上的资源显然不足以让你们存活到下一个宜居行星，你开始考虑要不要驾驶救生舱独自逃离去木星。你的选择是，逃走，或者留下？\", \"choices\":{\"逃走\":7,\"留下\":9}}, \"6\": {\"content\": \"你加入的是一艘搭载着引力波天线的战舰。在威慑纪元到来之后，你们出发前去追捕逃离的五艘战舰。最终，你们向宇宙广播了地球的坐标，这是太阳系的终结，也是你们新的文明的开始。\"}, \"7\": {\"content\": \"黑暗森林法则无处不在。救生舱上，你和一同逃离的伙伴之间开始了猜疑，最终同归于尽。\"}, \"8\": {\"content\": \"几艘战舰之间逐渐失去联络，你们都明白，想要活下去必须主动对其他战舰施加打击，集所有资源于自己。在人性的抉择之后，你们的舰长发动了攻击，但你们终究慢了一步。你的名字被刻在太阳系边界的巨大墓碑上。\"}, \"9\": {\"content\": \"几艘战舰之间逐渐失去联络，你们都明白，想要活下去必须主动对其他战舰施加打击，集所有资源于自己。其他战舰先发动了攻击，但你们在事先的准备下存活，并在反击之后成为最后的幸存者。这是人类最后薪火，你成为宇宙深处新人类文明的一员。\"}}'),(2,'{\"title\": \"游戏名\",\"endings\": [3, 4],\"0\": {\"content\": \"叙述0\", \"choices\": {\"选项A\": 1, \"选项B\": 2}},\"1\": {\"content\": \"叙述1\", \"choices\": {\"选项A\": 2, \"选项B\": 3}},\"2\": {\"content\": \"叙述2\", \"choices\": {\"选项A\": 3, \"选项B\": 4}},\"3\": {\"content\": \"结局3\"},\"4\": {\"content\": \"结局4\"}}');
/*!40000 ALTER TABLE `Game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `userId` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `vip` int NOT NULL DEFAULT '0',
  `gender` int DEFAULT '-1' COMMENT '0-男，1-女，-1为未填写。',
  `age` int DEFAULT NULL,
  `audioType` int DEFAULT '0',
  `speed` int DEFAULT '5',
  `password` varchar(50) NOT NULL,
  `motto` varchar(80) DEFAULT NULL,
  `registerDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`userId`),
  UNIQUE KEY `User_name_uindex` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'一只快活的野指针',3,1,18,1,3,'123',NULL,'2022-02-13 13:09:17'),(2,'张三',2,1,20,1,2,'123',NULL,'2022-02-13 13:09:17'),(3,'妖风振振',2,1,20,1,2,'123',NULL,'2022-02-13 13:09:17'),(4,'最后的软院人',2,1,20,1,2,'111',NULL,'2022-02-13 13:09:17'),(5,'sy小号',1,0,15,1,2,'222',NULL,'2022-02-13 13:09:17'),(6,'向天再借五百年',1,0,15,1,2,'333',NULL,'2022-02-13 13:09:17'),(7,'风之子',2,1,20,1,2,'123456',NULL,'2022-02-13 13:09:17'),(11,'王不留行',0,-1,NULL,0,5,'123456','冠军属于微草','2022-02-13 13:09:17'),(15,'柚子',0,-1,NULL,0,5,'123456','我好喜欢柚子','2022-02-13 13:09:17'),(16,'小爱',0,-1,NULL,0,5,'123456',NULL,'2022-02-13 13:09:17'),(17,'小艺',0,-1,NULL,0,5,'123456',NULL,'2022-02-13 13:09:17'),(19,'君莫笑',0,-1,NULL,0,5,'123',NULL,'2022-02-18 10:11:50'),(20,'lica',0,-1,NULL,0,5,'1234lica',NULL,'2022-02-18 12:17:45'),(21,'Lily',0,-1,NULL,0,5,'1234lily','yes ok','2022-02-18 12:19:19');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `newList`
--

DROP TABLE IF EXISTS `newList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `newList` (
  `userId` int NOT NULL,
  `list` text,
  PRIMARY KEY (`userId`),
  CONSTRAINT `newList_User_userId_fk` FOREIGN KEY (`userId`) REFERENCES `User` (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `newList`
--

LOCK TABLES `newList` WRITE;
/*!40000 ALTER TABLE `newList` DISABLE KEYS */;
INSERT INTO `newList` VALUES (2,'[{\"done\": 1, \"title\": \"\\u9759\\u591c\\u601d\"}, {\"done\": 0, \"title\": \"\\u51fa\\u5e08\\u8868\"}, {\"done\": 0, \"title\": \"\\u8700\\u9053\\u96be\"}]'),(3,'[{\"done\": 1, \"title\": \"\\u9759\\u591c\\u601d\"}, {\"done\": 0, \"title\": \"\\u51fa\\u5e08\\u8868\"}]');
/*!40000 ALTER TABLE `newList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviewList`
--

DROP TABLE IF EXISTS `reviewList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviewList` (
  `userId` int NOT NULL,
  `list` text,
  PRIMARY KEY (`userId`),
  CONSTRAINT `reviewList_User_userId_fk` FOREIGN KEY (`userId`) REFERENCES `User` (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviewList`
--

LOCK TABLES `reviewList` WRITE;
/*!40000 ALTER TABLE `reviewList` DISABLE KEYS */;
INSERT INTO `reviewList` VALUES (2,'[{\"done\": 0, \"title\": \"\\u79bb\\u9a9a\"}, {\"done\": 1, \"title\": \"\\u6843\\u82b1\\u6e90\\u8bb0\"}]'),(3,'[{\"done\": 0, \"title\": \"\\u79bb\\u9a9a\"}, {\"done\": 1, \"title\": \"\\u6843\\u82b1\\u6e90\\u8bb0\"}]');
/*!40000 ALTER TABLE `reviewList` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-27 11:05:29
