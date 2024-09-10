/*!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.6.18-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: shukdealsdb
-- ------------------------------------------------------
-- Server version	10.6.18-MariaDB-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account_activitylog`
--

DROP TABLE IF EXISTS `account_activitylog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_activitylog` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `type` varchar(10) NOT NULL,
  `created_date` date NOT NULL,
  `created_time` time(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_activitylog_user_id_e234bd33_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `account_activitylog_user_id_e234bd33_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=168 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_activitylog`
--

LOCK TABLES `account_activitylog` WRITE;
/*!40000 ALTER TABLE `account_activitylog` DISABLE KEYS */;
INSERT INTO `account_activitylog` VALUES (1,'login','2024-04-30','16:16:31.773536',10),(2,'login','2024-04-30','16:16:31.783286',10),(3,'login','2024-04-30','16:19:10.342060',10),(4,'login','2024-05-01','11:21:10.740361',11),(5,'logout','2024-05-01','12:22:30.247703',11),(6,'login','2024-05-01','14:29:11.534613',12),(7,'login','2024-05-01','14:29:11.640217',12),(8,'login','2024-05-08','08:26:15.820723',11),(9,'login','2024-05-08','14:27:56.528945',13),(10,'login','2024-05-09','15:12:49.690307',14),(11,'login','2024-05-12','15:05:16.598929',15),(12,'login','2024-05-12','15:05:16.870737',15),(13,'login','2024-05-12','17:54:48.466582',15),(14,'login','2024-05-12','17:54:49.027406',15),(15,'login','2024-05-15','03:55:43.271334',15),(16,'login','2024-05-15','10:08:37.980558',13),(17,'login','2024-05-16','18:00:26.167191',16),(18,'login','2024-05-17','07:38:50.605497',15),(19,'login','2024-05-17','07:39:25.117713',15),(20,'login','2024-05-19','12:20:13.627664',14),(21,'login','2024-05-20','12:39:52.020887',15),(22,'logout','2024-05-20','14:21:19.249893',15),(23,'login','2024-05-20','14:33:13.345505',11),(24,'login','2024-05-20','14:34:14.151507',11),(25,'logout','2024-05-20','14:45:32.335428',11),(26,'login','2024-05-20','14:45:43.002708',11),(27,'login','2024-05-20','14:49:45.653681',11),(28,'login','2024-05-21','08:29:22.557381',11),(29,'login','2024-05-21','08:29:58.129550',14),(30,'logout','2024-05-21','08:46:08.181544',11),(31,'login','2024-05-21','08:46:19.747892',15),(32,'login','2024-05-21','08:58:31.973733',15),(33,'login','2024-05-21','09:02:02.145804',15),(34,'login','2024-05-26','14:15:46.490961',15),(35,'login','2024-05-27','18:16:21.349296',14),(36,'login','2024-05-31','09:08:50.691321',15),(37,'logout','2024-05-31','09:14:58.418880',15),(38,'login','2024-05-31','09:15:05.638390',11),(39,'login','2024-05-31','09:28:39.344541',11),(40,'login','2024-05-31','09:40:48.367598',11),(41,'login','2024-05-31','09:45:17.542422',11),(42,'login','2024-05-31','09:45:42.519707',11),(43,'login','2024-06-05','10:03:16.675086',17),(44,'login','2024-06-05','10:03:16.910597',17),(45,'login','2024-06-05','10:04:13.742555',17),(46,'login','2024-06-05','10:04:34.500272',17),(47,'login','2024-06-05','10:06:42.804810',17),(48,'login','2024-06-05','10:16:17.489952',17),(49,'login','2024-06-05','10:17:54.034625',17),(50,'login','2024-06-06','06:20:43.116226',17),(51,'login','2024-06-06','06:20:53.921920',17),(52,'login','2024-06-10','15:50:44.264917',12),(53,'login','2024-06-10','15:50:44.413806',12),(54,'login','2024-06-10','15:53:39.425675',12),(55,'login','2024-06-10','15:53:39.592451',12),(56,'login','2024-06-17','14:21:56.753912',18),(57,'login','2024-06-26','14:50:42.839670',19),(58,'login','2024-06-26','14:51:30.137864',19),(59,'login','2024-06-26','14:53:08.864738',19),(60,'login','2024-06-27','09:35:43.537031',19),(61,'login','2024-06-27','09:35:46.136708',19),(62,'login','2024-06-27','09:38:13.328015',19),(63,'login','2024-07-01','06:54:09.652450',18),(64,'logout','2024-07-01','06:56:16.907493',18),(65,'login','2024-07-01','09:13:19.194034',11),(66,'logout','2024-07-01','09:14:06.004984',11),(67,'login','2024-07-05','14:20:27.435862',20),(68,'login','2024-07-05','14:21:26.749521',20),(69,'login','2024-07-17','04:52:32.848971',21),(70,'logout','2024-07-17','06:38:31.866744',21),(71,'login','2024-07-18','06:11:09.220040',21),(72,'login','2024-07-18','06:20:14.523986',21),(73,'logout','2024-07-18','09:13:52.573749',21),(74,'login','2024-07-18','11:18:35.209169',22),(75,'login','2024-07-19','04:21:23.146969',22),(76,'login','2024-07-22','03:58:33.112122',12),(77,'login','2024-07-22','03:58:33.116833',12),(78,'login','2024-07-22','03:58:55.044485',12),(79,'login','2024-07-22','03:58:55.045270',12),(80,'login','2024-07-22','04:09:57.783783',23),(81,'login','2024-07-22','04:09:57.796616',23),(82,'login','2024-07-22','04:13:11.527263',23),(83,'login','2024-07-22','11:58:25.149901',22),(84,'logout','2024-07-23','04:48:40.506021',22),(85,'login','2024-07-23','04:52:38.023800',21),(86,'logout','2024-07-23','09:13:13.804142',21),(87,'login','2024-07-23','09:56:37.171016',21),(88,'logout','2024-07-23','09:58:09.706250',21),(89,'login','2024-07-23','09:58:16.222297',22),(90,'login','2024-07-24','04:41:09.369905',22),(91,'login','2024-07-25','08:51:20.313820',24),(92,'login','2024-07-25','10:24:50.760937',24),(93,'login','2024-07-25','10:26:19.455987',24),(94,'logout','2024-07-26','04:34:55.174725',24),(95,'login','2024-07-31','17:05:13.199524',25),(96,'login','2024-08-03','06:29:02.080868',23),(97,'logout','2024-08-03','06:32:15.049803',23),(98,'login','2024-08-03','21:29:01.198098',25),(99,'login','2024-08-03','21:29:01.909155',25),(100,'login','2024-08-11','19:46:23.063546',19),(101,'login','2024-08-11','19:48:56.880264',19),(102,'login','2024-08-11','20:07:58.894044',26),(103,'login','2024-08-11','20:07:59.079347',26),(104,'login','2024-08-11','20:20:21.352923',28),(105,'login','2024-08-11','20:20:21.599987',28),(106,'login','2024-08-12','11:01:11.128952',21),(107,'logout','2024-08-12','11:31:10.642117',21),(108,'login','2024-08-12','15:40:47.435187',11),(109,'login','2024-08-12','15:40:53.306151',19),(110,'login','2024-08-12','15:41:23.325639',27),(111,'login','2024-08-12','15:41:51.223209',27),(112,'logout','2024-08-12','16:02:43.255876',19),(113,'login','2024-08-12','16:03:53.859117',19),(114,'logout','2024-08-12','16:06:39.094179',19),(115,'login','2024-08-12','16:07:19.851038',19),(116,'logout','2024-08-12','16:09:01.818193',19),(117,'login','2024-08-12','16:24:47.275314',19),(118,'logout','2024-08-12','18:05:32.332001',11),(119,'login','2024-08-13','06:25:12.257574',19),(120,'login','2024-08-13','09:00:04.415810',21),(121,'login','2024-08-13','09:10:21.475904',21),(122,'login','2024-08-13','09:12:38.495775',21),(123,'login','2024-08-13','11:29:26.738593',21),(124,'login','2024-08-14','05:28:42.308549',21),(125,'logout','2024-08-14','05:33:12.583169',21),(126,'login','2024-08-14','07:19:35.322446',21),(127,'logout','2024-08-14','07:21:27.440791',21),(128,'login','2024-08-14','08:45:33.532259',30),(129,'logout','2024-08-14','08:46:58.694083',30),(130,'login','2024-08-14','09:00:57.320282',32),(131,'login','2024-08-14','09:00:57.582662',32),(132,'login','2024-08-14','09:02:28.631795',30),(133,'login','2024-08-14','09:29:46.036778',30),(134,'login','2024-08-14','09:30:12.319512',30),(135,'logout','2024-08-14','09:30:31.758278',30),(136,'login','2024-08-14','09:40:04.624708',24),(137,'login','2024-08-14','09:41:06.345838',30),(138,'login','2024-08-14','09:45:04.762169',21),(139,'login','2024-08-14','09:45:05.031274',21),(140,'logout','2024-08-14','09:45:53.970367',30),(141,'login','2024-08-14','09:54:30.204413',35),(142,'login','2024-08-14','10:06:03.133687',35),(143,'login','2024-08-14','10:07:57.069944',35),(144,'logout','2024-08-14','10:09:05.212982',35),(145,'login','2024-08-14','10:09:09.188805',35),(146,'login','2024-08-14','10:11:55.934917',35),(147,'logout','2024-08-14','10:21:30.842963',35),(148,'login','2024-08-14','10:36:39.360447',36),(149,'login','2024-08-14','10:36:39.399347',36),(150,'login','2024-08-14','10:40:11.425138',36),(151,'login','2024-08-14','10:40:11.765836',36),(152,'login','2024-08-14','10:42:58.801602',36),(153,'login','2024-08-14','10:42:59.441907',36),(154,'login','2024-08-14','11:00:33.271990',36),(155,'login','2024-08-14','11:00:33.291438',36),(156,'login','2024-08-14','19:11:33.767979',25),(157,'login','2024-08-14','19:13:17.406204',19),(158,'login','2024-08-14','19:15:10.222449',19),(159,'login','2024-08-14','19:16:27.442576',19),(160,'login','2024-08-15','10:25:06.594229',11),(161,'login','2024-08-15','10:26:03.066894',11),(162,'logout','2024-08-15','19:09:35.571501',11),(163,'login','2024-08-20','02:26:08.383258',25),(164,'login','2024-08-21','07:59:22.738327',25),(165,'login','2024-08-21','09:38:35.038011',25),(166,'login','2024-08-22','18:46:20.910995',19),(167,'login','2024-08-22','18:46:31.292443',19);
/*!40000 ALTER TABLE `account_activitylog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_businesscategory`
--

DROP TABLE IF EXISTS `account_businesscategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_businesscategory` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `keyword` varchar(50) DEFAULT NULL,
  `parent_id` bigint(20) DEFAULT NULL,
  `display_type` varchar(20) NOT NULL,
  `name_es` varchar(50) DEFAULT NULL,
  `name_ar` varchar(50) DEFAULT NULL,
  `name_de` varchar(50) DEFAULT NULL,
  `name_fr` varchar(50) DEFAULT NULL,
  `name_he` varchar(50) DEFAULT NULL,
  `name_pt` varchar(50) DEFAULT NULL,
  `name_ru` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `account_businesscate_parent_id_3c66dc10_fk_account_b` (`parent_id`),
  CONSTRAINT `account_businesscate_parent_id_3c66dc10_fk_account_b` FOREIGN KEY (`parent_id`) REFERENCES `account_businesscategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=123 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_businesscategory`
--

LOCK TABLES `account_businesscategory` WRITE;
/*!40000 ALTER TABLE `account_businesscategory` DISABLE KEYS */;
INSERT INTO `account_businesscategory` VALUES (1,'Product','product',NULL,'dropdown','Producto','منتج','Produkt','produit','מוצר','produto','продукт'),(2,'Service','service',NULL,'dropdown','servicio','خدمة','Dienstleistung','service','שירות','serviço','услуга'),(3,'Restaurant','restaurant',NULL,'dropdown','restaurante','مطعم','Restaurant','restaurant','מסעדה','restaurante','ресторан'),(4,'Travel','travel',NULL,'dropdown','viajar','سفر','reisen','voyager','לטוס','viajar','путешествовать'),(5,'Real Estate','real_estate',NULL,'dropdown','bienes','العقارات','Immobilien','immobilier','נדל\"ן','imóveis','недвижимость'),(6,'Entertainment/Sports','entertainment_sport',NULL,'dropdown','Entretenimiento/Deportes','ترفيه/رياضة','Unterhaltung/Sport\n','Divertissement/Sports','בידור/ספורט','Entretenimento/Esportes','Развлечения/Спорт'),(10,'Rent','rent',5,'radio','alquiler','إيجار','Miete','loyer','שכירות','aluguel','аренда'),(11,'Vacation Rentals','vacation_rental',5,'radio','Alquileres de vacaciones','إيجارات العطلات','Ferienwohnungen','Locations de vacances','השכרת חופש','Aluguel de temporada','Аренда на каникулах'),(12,'Sale','sale',5,'radio','venta','بيع','Verkauf','vente','מכירה','venda','продажа'),(13,'Venue','venue',6,'radio','lugar','مكان','Veranstaltungsort','lieu','מקום','local','место'),(14,'Sports','sport',6,'radio','deportes','رياضة','Sport','sports','ספורט','esportes','спорт'),(15,'Movie Theaters','movie_theater',6,'radio','cines','دور السينما','Kinos','cinémas','בתי קולנוע','cinemas','кинотеатры'),(16,'Vehicles /Transportation',NULL,1,'dropdown','Vehículos/Transporte',' مركبات/نقل ','Fahrzeuge/Transport','Véhicules/Transport',' רכבים/תחבורה','Veículos/Transporte',' Транспорт/Транспортировка'),(17,'Roommate / Room Share',NULL,1,'dropdown','compañero de cuarto / compartición de habitación','زميل سكن / مشاركة غرفة ','Mitbewohner / Zimmer teilen','colocataire / colocation','חבר דירה / שיתוף חדר','colega de quarto / compartilhamento de quarto','сосед по комнате / совместное жилье'),(18,'Clothing',NULL,1,'dropdown','Ropa',' ملابس','Kleidung','Vêtements',' בגדים ','Roupas','Одежда'),(19,'Furniture',NULL,1,'dropdown','Muebles','أثاث','Möbel','Meubles','רהיטים','Móveis','Мебель'),(20,'Electronics',NULL,1,'dropdown','Electrónica','إلكترونيات','Elektronik','Électronique','אלקטרוניקה','Eletrônicos','Электроника'),(21,'Antiques & Collectibles',NULL,1,'dropdown','Antigüedades y Coleccionables','تحف وتحفيظات ','Antiquitäten und Sammlerstücke','Antiquités et Objets de Collection','יוקרתיים ואוספים ','Antiguidades e Colecionáveis','Антиквариат и Коллекционирование'),(22,'Appliances',NULL,1,'dropdown','Electrodomésticos','أجهزة كهربائية ','Haushaltsgeräte','Appareils électroménagers',' מכשירי חשמל','Eletrodomésticos','Бытовая техника'),(23,'Books, Films & Music',NULL,1,'dropdown','Libros, Películas y Música',' كتب، أفلام وموسيقى','Bücher, Filme und Musik','Livres, Films et Musique','ספרים, סרטים ומוזיקה','Livros, Filmes e Música','Книги, Фильмы и Музыка'),(24,'Tools',NULL,1,'dropdown','Herramientas',' أدوات','Werkzeuge','Outils','כלים','Ferramentas','Инструменты'),(25,'FREE',NULL,1,'dropdown','GRATIS','مجاناً','KOSTENLOS','GRATUIT','חינם','GRÁTIS','БЕСПЛАТНО'),(26,'Heath & Beauty',NULL,1,'dropdown','Salud y Belleza','الصحة والجمال ','Gesundheit und Schönheit','Santé et Beauté','בריאות ויופי ','Saúde e Beleza','Здоровье и Красота'),(27,'Jewellery & Watches',NULL,1,'dropdown','Joyas y Relojes','مجوهرات وساعات ','Schmuck und Uhren','Bijoux et Montres','תכשיטים ושעונים','Joias e Relógios','Ювелирные изделия и Часы'),(28,'Home Goods & Decor',NULL,1,'dropdown','Artículos para el hogar y Decoración','سلع منزلية وديكور ','Haushaltswaren und Dekor','Articles ménagers et Décoration',' מוצרי בית וקישוטים','Artigos para Casa e Decoração','Товары для дома и Декор'),(29,'Luggage & Bags',NULL,1,'dropdown','Equipaje y bolsos','أمتعة و حقائب','Gepäck und Taschen','Valises et sacs','מזוודות ותיקים','Bagagem e bolsas','Багаж и сумки'),(30,'Musical Instruments',NULL,1,'dropdown','Instrumentos musicales','الات موسيقية','Musikinstrumente','Instruments de musique','כלי נגינה','Instrumentos musicais','Музыкальные инструменты'),(31,'Patio & Garden',NULL,1,'dropdown','Patio y jardín','الفناء والحديقة','Terrasse & Garten','Patio et jardin','פטיו וגן','Pátio e jardim','Патио и сад'),(32,'Pets & Supplies',NULL,1,'dropdown','Mascotas y suministros','الحيوانات الأليفة والمستلزمات','Haustiere & Vorräte','Animaux et fournitures','חיות מחמד ואספקה','Animais de estimação e suprimentos','Домашние животные и расходные материалы'),(33,'Sporting Goods',NULL,1,'dropdown','Artículos deportivos','بضائع رياضيه','Sportwaren','Articles de sport','מוצרי ספורט','Artigos esportivos','Спортивные товары'),(34,'Toys & Games',NULL,1,'dropdown','Juguetes y Juegos','الألعاب والألعاب','Spielzeug & Spiele','Jouets et jeux','צעצועים ומשחקים','Brinquedos e jogos','Игрушки и игры'),(35,'Automotive',NULL,2,'dropdown','Automotor','السيارات','Automobil','Automobile','רכב','Automotivo','Автомобиль'),(36,'Beauty',NULL,2,'dropdown','Belleza','جمال','Schönheit','Beauté','יוֹפִי','Beleza','Красота'),(37,'Cell / Mobile',NULL,2,'dropdown','Celda / móvil','الخلية / الهاتف المحمول','Zelle / Mobile','Cellule / mobile','תא / נייד','Célula / celular','Ячейка / мобильный'),(38,'Computer',NULL,2,'dropdown','Computadora','حاسوب','Computer','Ordinateur','מַחשֵׁב','Computador','Компьютер'),(39,'Cycle',NULL,2,'dropdown','Ciclo','دورة','Zyklus','Faire du vélo','מחזור','Ciclo','Цикл'),(40,'Event Planing',NULL,2,'dropdown','Planificación de eventos','تخطيط الأحداث','Ereignisplanung','Planage de l\'événement','תכנון אירועים','Planejamento de eventos','Планирование событий'),(41,'Garden/ Landscaping',NULL,2,'dropdown','Jardín/ paisajismo','الحديقة/ المناظر الطبيعية','Garten/ Landschaftsbau','Jardin / aménagement paysager','גן/ גינון','Jardim/ paisagismo','Сад/ ландшафт'),(42,'Financial',NULL,2,'dropdown','Financiero','مالي','Finanziell','Financier','כַּספִּי','Financeiro','Финансовый'),(43,'Health / Wellness',NULL,2,'dropdown','Salud y bienestar','الصحة والعافية','Gesundheit','Santé','בריאות / בריאות','Saúde e bem estar','Здоровье / здоровье'),(44,'Household / Cleaning',NULL,2,'dropdown','Limpieza doméstica','التنظيف المنزلية','Haushaltsreinigung','Nettoyage ménager','משק בית / ניקוי','Doméstico / limpeza','Домохозяйство / уборка'),(45,'Labor / Moving l Hauling',NULL,2,'dropdown','Trabajo / mudanza l de transporte','العمل / الحركة','Arbeit / bewegt l Transport','Travail / déménagement en transport en l','עבודה / העברה L הובלה','Trabalho / Motivo para transportar','Труд / Перемещение L перевозки'),(46,'Legal',NULL,2,'dropdown','Legal','قانوني','Legal','Légal','משפטי','Jurídico','Юридический'),(47,'Lessons & Tutoring',NULL,2,'dropdown','Lecciones y tutoría','الدروس والدروس','Lektionen & Nachhilfe','Leçons et tutorat','שיעורים וחליפות','Lições e aulas','Уроки и репетиторство'),(48,'Pet',NULL,2,'dropdown','Mascota','حيوان أليف','Haustier','Animal de compagnie','חיית מחמד','Bicho de estimação','Домашний питомец'),(49,'Real Estate',NULL,2,'dropdown','Bienes raíces','العقارات','Immobilie','Immobilier','נדל\"ן','Imobiliária','Недвижимость'),(50,'Skilled Trade',NULL,2,'dropdown','Comercio especializado','التجارة الماهرة','Fachhandel','Métier qualifié','מסחר מיומן','Comércio qualificado','Квалифицированная торговля'),(51,'Travel/Vacation',NULL,2,'dropdown','Viajes/vacaciones','السفر/الإجازة','Reisen/Urlaub','Voyage / vacances','נסיעות/חופשה','Viagens/férias','Путешествие/Отпуск'),(52,'Entertaiment / Artists and Production',NULL,2,'dropdown','Entretaimente / artistas y producción','entertaiment / الفنانين والإنتاج','Entertaiment / Künstler und Produktion','Enterrent / artistes et production','Entertaiment / אמנים והפקה','ENTERTERAIMENT / ARTISTAS E PRODUÇÃO','Entertaiment / Artists и производство'),(53,'Fast Food',NULL,3,'dropdown','Comida rápida','الطعام السريع','Fastfood','Fast food','אוכל מהיר','Comida rápida','Быстрое питание'),(54,'Delivery Only',NULL,3,'dropdown','Solo entrega','التسليم فقط','Lieferverkehr frei','Livraison uniquement','משלוח בלבד','Apenas entrega','Только доставка'),(55,'Asian',NULL,3,'dropdown','asiático','آسيوي','asiatisch','asiatique','אסייתי','Asiático','Азиатский'),(56,'Italian',NULL,3,'dropdown','italiano','إيطالي','Italienisch','italien','אִיטַלְקִית','italiano','Итальянский'),(57,'Mexican',NULL,3,'dropdown','mexicano','مكسيكي','Mexikaner','mexicain','מֶקסִיקָני','mexicano','Мексиканец'),(58,'Indian',NULL,3,'dropdown','indio','هندي','indisch','Indien','הוֹדִי','indiano','Индийский'),(59,'Middle Eastern',NULL,3,'dropdown','Medio este','شرق اوسطي','Nahen Osten','Moyen-Orient','מזרח תיכוני','Oriente médio','Ближневосточный'),(60,'Deli',NULL,3,'dropdown','fiambres','أطعمة لذيذة','Delikatessen','épicerie fine','מעדניה','Delicatessen','гастроном'),(61,'Desserts',NULL,3,'dropdown','Postres','الحلويات','Nachspeisen','Desserts','קינוחים','Sobremesas','Десерты'),(62,'Kosher',NULL,3,'dropdown','Comestible según la ley judía','كوشير','Koscher','Kascher','כשר','Kosher','Кошер'),(63,'Burger',NULL,3,'dropdown','Hamburguesa','برغر','Burger','Burger','בורגר','Hambúrguer','Бургер'),(64,'Vegetarian / Vegan',NULL,3,'dropdown','Vegetariano / vegano','نباتي / نباتي','Vegetarier / vegan','Végétarien / végétalien','צמחוני / טבעוני','Vegetariano / vegano','Вегетарианский / веганский'),(65,'Kid Friendly',NULL,3,'dropdown','Amigable para niños','ودية للأطفال','Kinderfreundlich','Accueille les enfants','ידידותי לילדים','Amigável para crianças','Малыш'),(66,'Mediterranean',NULL,3,'dropdown','Mediterráneo','البحر المتوسط','Mittelmeer','méditerranéen','יָם תִיכוֹנִי','Mediterrâneo','Средиземноморье'),(67,'Family Style',NULL,3,'dropdown','Estilo familiar','نمط الأسرة','Familienstil','Style familial','סגנון משפחתי','Estilo familiar','Семейный стиль'),(68,'Fish / Seafood',NULL,3,'dropdown','Pescado / mariscos','الأسماك / المأكولات البحرية','Fisch / Meeresfrüchte','Poisson / fruits de mer','דגים / פירות ים','Peixe / frutos do mar','Рыба / морепродукты'),(69,'Steak house',NULL,3,'dropdown','Asador','بيت شرائح اللحم','Steak-House','Steak House','סטייקיה','Churrascaria','Стейк-хаус'),(70,'French',NULL,3,'dropdown','Francés','فرنسي','Französisch','Français','צָרְפָתִית','Francês','Французский'),(71,'Ethnic Cooking',NULL,3,'dropdown','Cocina étnica','الطبخ العرقي','Ethnische Küche','Cuisine ethnique','בישול אתני','Culinária étnica','Этническая кулинария'),(72,'Airline',NULL,4,'dropdown','Aerolínea','شركة طيران','Fluggesellschaft','Compagnie aérienne','חֶברַת תְעוּפָה','CIA aérea','Авиакомпания'),(73,'Hotel',NULL,4,'dropdown','Hotel','الفندق','Hotel','Hôtel','מלון','Hotel','Гостиница'),(74,'Bed & Breakfast',NULL,4,'dropdown','Cama y Desayuno','سرير و فطور','Bed & Breakfast','lit et petit-déjeuner','שינה וארוחת בוקר','Bed & Breakfast','Кровать и завтрак'),(75,'Motel',NULL,4,'dropdown','Motel','فندق صغير','Motel','Motel','מוֹטֶל','Motel','Мотель'),(76,'Hostel',NULL,4,'dropdown','Albergue','نزل','Herberge','Auberge','הוסטל','Hostel','Общежитие'),(77,'Camping',NULL,4,'dropdown','Cámping','تخييم','Camping','Camping','קֶמפִּינג','Acampamento','Кемпинг'),(78,'Car Rental',NULL,4,'dropdown','Alquiler de coches','تاجير سيارة','Autovermietung','Location de voiture','השכרת רכב','Aluguel de carros','Прокат автомобилей'),(79,'Park and Recreation',NULL,4,'dropdown','Parque y recreación','الحديقة والترفيه','Park und Erholung','Parc et loisirs','פארק ובילוי','Parque e recreação','Парк и отдых'),(80,'Amusement Park',NULL,4,'dropdown','Parque de atracciones','حديقة الملاهي','Freizeitpark','Parc d\'attractions','פארק השעשועים','Parque de diversões','Парк с аттракционами'),(81,'Shopping',NULL,4,'dropdown','Compras','التسوق','Einkaufen','Achats','קניות','Compras','Покупка'),(82,'Tours',NULL,4,'dropdown','Excursiones','جولات','Touren','Tournées','סיורים','Passeios','Туры'),(83,'Transportation Rentals',NULL,4,'dropdown','Alquiler de transporte','إيجارات النقل','Transportvermietungen','Location de transport','השכרת הובלה','Aluguel de transporte','Транспортная аренда'),(84,'Apartments / Housing',NULL,10,'dropdown','Apartamentos / vivienda','الشقق / السكن','Wohnungen / Wohnungen','Appartements / logements','דירות / דיור','Apartamentos / moradia','Квартиры / Жилье'),(85,'Sublet / Temporary',NULL,10,'dropdown','Subarriendo / temporal','Sublet / مؤقت','Untervermietung / vorübergehend','Sous-location / temporaire','תת -סובל / זמני','Subblina / temporária','Сублет / временный'),(86,'Office & Commercial',NULL,10,'dropdown','Oficina y comercial','المكتب والتجاري','Büro & kommerziell','Bureau et publicité','משרד ומסחר','Escritório e Comercial','Офис и коммерческий'),(87,'Apartments / Housing',NULL,12,'','Apartamentos / vivienda','الشقق / السكن','Wohnungen / Wohnungen','Appartements / logements','דירות / דיור','Apartamentos / moradia','Квартиры / Жилье'),(88,'Office & Commercial',NULL,12,'','Oficina y comercial','المكتب والتجاري','Büro & kommerziell','Bureau et publicité','משרד ומסחר','Escritório e Comercial','Офис и коммерческий'),(89,'Amusement Park',NULL,13,'dropdown','Parque de atracciones','حديقة الملاهي','Freizeitpark','Parc d\'attractions','פארק השעשועים','Parque de diversões','Парк с аттракционами'),(90,'Amusement Park',NULL,13,'dropdown','Parque de atracciones','حديقة الملاهي','Freizeitpark','Parc d\'attractions','פארק השעשועים','Parque de diversões','Парк с аттракционами'),(91,'Casinos',NULL,13,'dropdown','Casinos','الكازينوهات','Casinos','Casinos','בתי קזינו','Cassinos','Казино'),(92,'Concert Halls',NULL,13,'dropdown','Salas de conciertos','قاعات الحفلات الموسيقية','Konzerthallen','Salles de concert','אולמות קונצרטים','Salas de concertos','Концертные залы'),(93,'Live Music',NULL,13,'dropdown','Música en vivo','موسيقى مباشره','Live Musik','Musique live','מוסיקת חיה','Música ao vivo','Живая музыка'),(94,'Nightclubs/Bar',NULL,13,'dropdown','Clubes nocturnos/bar','النوادي الليلية/البار','Nachtclubs/Bar','Clubs de nuit / bar','מועדוני לילה/בר','Boates/bar','Ночные клубы/бар'),(95,'Theater',NULL,13,'dropdown','Teatro','مسرح','Theater','Théâtre','תיאטרון','Teatro','Театр'),(96,'Cultural Center',NULL,13,'dropdown','Centro Cultural','مركز ثقافي','Kulturzentrum','Centre culturel','מרכז תרבות','Centro Cultural','Культурный центр'),(97,'Community Center',NULL,13,'dropdown','Centro Comunitario','مركز اجتماعي','Gemeindezentrum','Centre communautaire','מרכז קהילתי','Centro Comunitário','Общественный центр'),(98,'Parks',NULL,13,'dropdown','Parque','الحدائق','Parks','Parcs','פארקים','Parques','Парки'),(99,'American Football',NULL,14,'dropdown','fútbol americano','كرة القدم الأمريكية','Amerikanischer Fußball','football américain','כדורגל אמריקאי','futebol americano','американский футбол'),(100,'Basketball',NULL,14,'dropdown','Baloncesto','كرة سلة','Basketball','Basket-ball','כדורסל','Basquetebol','Баскетбол'),(101,'Soccer',NULL,14,'dropdown','Fútbol','كرة القدم','Fußball','Football','כדורגל','Futebol','Футбольный'),(102,'Cricket',NULL,14,'dropdown','Grillo','كريكيت','Kricket','Criquet','קרִיקֶט','Grilo','Крикет'),(103,'Baseball',NULL,14,'dropdown','Béisbol','البيسبول','Baseball','Base-ball','בייסבול','Beisebol','Бейсбол'),(104,'Ice Hockey',NULL,14,'dropdown','Hockey sobre hielo','الهوكى الجليدى','Eishockey','Hockey sur glace','הוקי קרח','Hockey no gelo','Хоккей'),(105,'Tennis',NULL,14,'dropdown','Tenis','تنس','Tennis','Tennis','טֶנִיס','tênis','Большой теннис'),(106,'Motorsports',NULL,14,'dropdown','Portavoz','رياضة السيارات','Motorsport','Sport automobile','מוטורספורט','Motorsports','Автоспорта'),(107,'Marathons',NULL,14,'dropdown','Maratones','ماراثون','Marathons','Marathons','מרתונים','Maratonas','Марафоны'),(108,'Cycling',NULL,14,'dropdown','Ciclismo','ركوب الدراجات','Radfahren','Vélo','רכיבה על אופניים','Ciclismo','Езда на велосипеде'),(109,'Maccabiah',NULL,14,'dropdown','Maccabiah','مكابيا','MACCABIAH','Maccabia','מכביה','Maccabiah','Маккабия'),(110,'Olympics',NULL,14,'dropdown','Juegos Olímpicos','الألعاب الأولمبية','Olympia','Jeux olympiques','אולימפיאדה','Olimpíadas','Олимпийские игры'),(111,'Action',NULL,15,'dropdown','Acción','فعل','Aktion','Action','פעולה','Ação','Действие'),(112,'Horror',NULL,15,'dropdown','Horror','رعب','Grusel','Horreur','חֲרָדָה','Horror','Ужастик'),(113,'Drama',NULL,15,'dropdown','Drama','دراما','Theater','Drame','דְרָמָה','Drama','Драма'),(114,'Comedy',NULL,15,'dropdown','Comedia','كوميديا','Komödie','Comédie','קוֹמֶדִיָה','Comédia','Комедия'),(115,'Western',NULL,15,'dropdown','occidental','الغربي','Western','Occidental','מערבי','Ocidental','Западный'),(116,'Documentary',NULL,15,'dropdown','Documental','وثائقي','Dokumentarfilm','Documentaire','דוקומנטרי','Documentário','Документальный'),(117,'Romance',NULL,15,'dropdown','Romance','رومانسي','Romantik','Romance','רומנטיקה','Romance','Роман'),(118,'Thriller',NULL,15,'dropdown','Suspenso','إثارة','Thriller','Thriller','מוֹתְחָן','Filme de ação','Триллер'),(119,'SciFy',NULL,15,'dropdown','Chiflado','تفكيك','Surfen','Glissant','ציקי','Scify','Scify'),(120,'Kids',NULL,15,'dropdown','Niños','أطفال','Kinder','Enfants','ילדים','Crianças','Дети'),(121,'Independent',NULL,15,'dropdown','Independiente','مستقل','Unabhängig','Indépendant','עצמאי','Independente','Независимый'),(122,'Musical',NULL,15,'dropdown','Musical','موسيقي','Musical','Musical','מוּסִיקָלִי','Musical','Мюзикл');
/*!40000 ALTER TABLE `account_businesscategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_code`
--

DROP TABLE IF EXISTS `account_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_code` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `confirmation_code` varchar(6) NOT NULL,
  `usage` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_code_user_id_047b9897_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_code`
--

LOCK TABLES `account_code` WRITE;
/*!40000 ALTER TABLE `account_code` DISABLE KEYS */;
INSERT INTO `account_code` VALUES (1,'911138','Register','2024-04-05 10:38:23.429899',3),(2,'650738','Register','2024-04-06 05:43:15.497738',4),(9,'143789','Register','2024-04-26 12:33:51.047544',5),(10,'832829','Register','2024-04-26 12:36:45.007878',6),(11,'694964','Register','2024-04-29 10:43:52.694810',7),(12,'405588','Register','2024-04-29 11:54:53.827106',8),(13,'255227','Register','2024-04-29 11:55:45.656084',9),(41,'997666','Register','2024-08-14 09:32:24.919268',33);
/*!40000 ALTER TABLE `account_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_country`
--

DROP TABLE IF EXISTS `account_country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_country` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `numcode` smallint(6) NOT NULL,
  `nicename` varchar(80) NOT NULL,
  `iso` varchar(2) NOT NULL,
  `iso3` varchar(3) NOT NULL,
  `phonecode` smallint(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=240 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_country`
--

LOCK TABLES `account_country` WRITE;
/*!40000 ALTER TABLE `account_country` DISABLE KEYS */;
INSERT INTO `account_country` VALUES (1,'AFGHANISTAN',4,'Afghanistan','AF','AFG',93),(2,'ALBANIA',8,'Albania','AL','ALB',355),(3,'ALGERIA',12,'Algeria','DZ','DZA',213),(4,'AMERICAN SAMOA',16,'American Samoa','AS','ASM',1684),(5,'ANDORRA',20,'Andorra','AD','AND',376),(6,'ANGOLA',24,'Angola','AO','AGO',244),(7,'ANGUILLA',660,'Anguilla','AI','AIA',1264),(8,'ANTARCTICA',0,'Antarctica','AQ','',0),(9,'ANTIGUA AND BARBUDA',28,'Antigua and Barbuda','AG','ATG',1268),(10,'ARGENTINA',32,'Argentina','AR','ARG',54),(11,'ARMENIA',51,'Armenia','AM','ARM',374),(12,'ARUBA',533,'Aruba','AW','ABW',297),(13,'AUSTRALIA',36,'Australia','AU','AUS',61),(14,'AUSTRIA',40,'Austria','AT','AUT',43),(15,'AZERBAIJAN',31,'Azerbaijan','AZ','AZE',994),(16,'BAHAMAS',44,'Bahamas','BS','BHS',1242),(17,'BAHRAIN',48,'Bahrain','BH','BHR',973),(18,'BANGLADESH',50,'Bangladesh','BD','BGD',880),(19,'BARBADOS',52,'Barbados','BB','BRB',1246),(20,'BELARUS',112,'Belarus','BY','BLR',375),(21,'BELGIUM',56,'Belgium','BE','BEL',32),(22,'BELIZE',84,'Belize','BZ','BLZ',501),(23,'BENIN',204,'Benin','BJ','BEN',229),(24,'BERMUDA',60,'Bermuda','BM','BMU',1441),(25,'BHUTAN',64,'Bhutan','BT','BTN',975),(26,'BOLIVIA',68,'Bolivia','BO','BOL',591),(27,'BOSNIA AND HERZEGOVINA',70,'Bosnia and Herzegovina','BA','BIH',387),(28,'BOTSWANA',72,'Botswana','BW','BWA',267),(29,'BOUVET ISLAND',0,'Bouvet Island','BV','',0),(30,'BRAZIL',76,'Brazil','BR','BRA',55),(31,'BRITISH INDIAN OCEAN TERRITORY',0,'British Indian Ocean Territory','IO','',246),(32,'BRUNEI DARUSSALAM',96,'Brunei Darussalam','BN','BRN',673),(33,'BULGARIA',100,'Bulgaria','BG','BGR',359),(34,'BURKINA FASO',854,'Burkina Faso','BF','BFA',226),(35,'BURUNDI',108,'Burundi','BI','BDI',257),(36,'CAMBODIA',116,'Cambodia','KH','KHM',855),(37,'CAMEROON',120,'Cameroon','CM','CMR',237),(38,'CANADA',124,'Canada','CA','CAN',1),(39,'CAPE VERDE',132,'Cape Verde','CV','CPV',238),(40,'CAYMAN ISLANDS',136,'Cayman Islands','KY','CYM',1345),(41,'CENTRAL AFRICAN REPUBLIC',140,'Central African Republic','CF','CAF',236),(42,'CHAD',148,'Chad','TD','TCD',235),(43,'CHILE',152,'Chile','CL','CHL',56),(44,'CHINA',156,'China','CN','CHN',86),(45,'CHRISTMAS ISLAND',0,'Christmas Island','CX','',61),(46,'COCOS (KEELING) ISLANDS',0,'Cocos (Keeling) Islands','CC','',672),(47,'COLOMBIA',170,'Colombia','CO','COL',57),(48,'COMOROS',174,'Comoros','KM','COM',269),(49,'CONGO',178,'Congo','CG','COG',242),(50,'CONGO, THE DEMOCRATIC REPUBLIC OF THE',180,'Congo, the Democratic Republic of the','CD','COD',242),(51,'COOK ISLANDS',184,'Cook Islands','CK','COK',682),(52,'COSTA RICA',188,'Costa Rica','CR','CRI',506),(53,'COTE D\'IVOIRE',384,'Cote D\'Ivoire','CI','CIV',225),(54,'CROATIA',191,'Croatia','HR','HRV',385),(55,'CUBA',192,'Cuba','CU','CUB',53),(56,'CYPRUS',196,'Cyprus','CY','CYP',357),(57,'CZECH REPUBLIC',203,'Czech Republic','CZ','CZE',420),(58,'DENMARK',208,'Denmark','DK','DNK',45),(59,'DJIBOUTI',262,'Djibouti','DJ','DJI',253),(60,'DOMINICA',212,'Dominica','DM','DMA',1767),(61,'DOMINICAN REPUBLIC',214,'Dominican Republic','DO','DOM',1809),(62,'ECUADOR',218,'Ecuador','EC','ECU',593),(63,'EGYPT',818,'Egypt','EG','EGY',20),(64,'EL SALVADOR',222,'El Salvador','SV','SLV',503),(65,'EQUATORIAL GUINEA',226,'Equatorial Guinea','GQ','GNQ',240),(66,'ERITREA',232,'Eritrea','ER','ERI',291),(67,'ESTONIA',233,'Estonia','EE','EST',372),(68,'ETHIOPIA',231,'Ethiopia','ET','ETH',251),(69,'FALKLAND ISLANDS (MALVINAS)',238,'Falkland Islands (Malvinas)','FK','FLK',500),(70,'FAROE ISLANDS',234,'Faroe Islands','FO','FRO',298),(71,'FIJI',242,'Fiji','FJ','FJI',679),(72,'FINLAND',246,'Finland','FI','FIN',358),(73,'FRANCE',250,'France','FR','FRA',33),(74,'FRENCH GUIANA',254,'French Guiana','GF','GUF',594),(75,'FRENCH POLYNESIA',258,'French Polynesia','PF','PYF',689),(76,'FRENCH SOUTHERN TERRITORIES',0,'French Southern Territories','TF','',0),(77,'GABON',266,'Gabon','GA','GAB',241),(78,'GAMBIA',270,'Gambia','GM','GMB',220),(79,'GEORGIA',268,'Georgia','GE','GEO',995),(80,'GERMANY',276,'Germany','DE','DEU',49),(81,'GHANA',288,'Ghana','GH','GHA',233),(82,'GIBRALTAR',292,'Gibraltar','GI','GIB',350),(83,'GREECE',300,'Greece','GR','GRC',30),(84,'GREENLAND',304,'Greenland','GL','GRL',299),(85,'GRENADA',308,'Grenada','GD','GRD',1473),(86,'GUADELOUPE',312,'Guadeloupe','GP','GLP',590),(87,'GUAM',316,'Guam','GU','GUM',1671),(88,'GUATEMALA',320,'Guatemala','GT','GTM',502),(89,'GUINEA',324,'Guinea','GN','GIN',224),(90,'GUINEA-BISSAU',624,'Guinea-Bissau','GW','GNB',245),(91,'GUYANA',328,'Guyana','GY','GUY',592),(92,'HAITI',332,'Haiti','HT','HTI',509),(93,'HEARD ISLAND AND MCDONALD ISLANDS',0,'Heard Island and Mcdonald Islands','HM','',0),(94,'HOLY SEE (VATICAN CITY STATE)',336,'Holy See (Vatican City State)','VA','VAT',39),(95,'HONDURAS',340,'Honduras','HN','HND',504),(96,'HONG KONG',344,'Hong Kong','HK','HKG',852),(97,'HUNGARY',348,'Hungary','HU','HUN',36),(98,'ICELAND',352,'Iceland','IS','ISL',354),(99,'INDIA',356,'India','IN','IND',91),(100,'INDONESIA',360,'Indonesia','ID','IDN',62),(101,'IRAN, ISLAMIC REPUBLIC OF',364,'Iran, Islamic Republic of','IR','IRN',98),(102,'IRAQ',368,'Iraq','IQ','IRQ',964),(103,'IRELAND',372,'Ireland','IE','IRL',353),(104,'ISRAEL',376,'Israel','IL','ISR',972),(105,'ITALY',380,'Italy','IT','ITA',39),(106,'JAMAICA',388,'Jamaica','JM','JAM',1876),(107,'JAPAN',392,'Japan','JP','JPN',81),(108,'JORDAN',400,'Jordan','JO','JOR',962),(109,'KAZAKHSTAN',398,'Kazakhstan','KZ','KAZ',7),(110,'KENYA',404,'Kenya','KE','KEN',254),(111,'KIRIBATI',296,'Kiribati','KI','KIR',686),(112,'KOREA, DEMOCRATIC PEOPLE\'S REPUBLIC OF',408,'Korea, Democratic People\'s Republic of','KP','PRK',850),(113,'KOREA, REPUBLIC OF',410,'Korea, Republic of','KR','KOR',82),(114,'KUWAIT',414,'Kuwait','KW','KWT',965),(115,'KYRGYZSTAN',417,'Kyrgyzstan','KG','KGZ',996),(116,'LAO PEOPLE\'S DEMOCRATIC REPUBLIC',418,'Lao People\'s Democratic Republic','LA','LAO',856),(117,'LATVIA',428,'Latvia','LV','LVA',371),(118,'LEBANON',422,'Lebanon','LB','LBN',961),(119,'LESOTHO',426,'Lesotho','LS','LSO',266),(120,'LIBERIA',430,'Liberia','LR','LBR',231),(121,'LIBYAN ARAB JAMAHIRIYA',434,'Libyan Arab Jamahiriya','LY','LBY',218),(122,'LIECHTENSTEIN',438,'Liechtenstein','LI','LIE',423),(123,'LITHUANIA',440,'Lithuania','LT','LTU',370),(124,'LUXEMBOURG',442,'Luxembourg','LU','LUX',352),(125,'MACAO',446,'Macao','MO','MAC',853),(126,'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF',807,'Macedonia, the Former Yugoslav Republic of','MK','MKD',389),(127,'MADAGASCAR',450,'Madagascar','MG','MDG',261),(128,'MALAWI',454,'Malawi','MW','MWI',265),(129,'MALAYSIA',458,'Malaysia','MY','MYS',60),(130,'MALDIVES',462,'Maldives','MV','MDV',960),(131,'MALI',466,'Mali','ML','MLI',223),(132,'MALTA',470,'Malta','MT','MLT',356),(133,'MARSHALL ISLANDS',584,'Marshall Islands','MH','MHL',692),(134,'MARTINIQUE',474,'Martinique','MQ','MTQ',596),(135,'MAURITANIA',478,'Mauritania','MR','MRT',222),(136,'MAURITIUS',480,'Mauritius','MU','MUS',230),(137,'MAYOTTE',0,'Mayotte','YT','',269),(138,'MEXICO',484,'Mexico','MX','MEX',52),(139,'MICRONESIA, FEDERATED STATES OF',583,'Micronesia, Federated States of','FM','FSM',691),(140,'MOLDOVA, REPUBLIC OF',498,'Moldova, Republic of','MD','MDA',373),(141,'MONACO',492,'Monaco','MC','MCO',377),(142,'MONGOLIA',496,'Mongolia','MN','MNG',976),(143,'MONTSERRAT',500,'Montserrat','MS','MSR',1664),(144,'MOROCCO',504,'Morocco','MA','MAR',212),(145,'MOZAMBIQUE',508,'Mozambique','MZ','MOZ',258),(146,'MYANMAR',104,'Myanmar','MM','MMR',95),(147,'NAMIBIA',516,'Namibia','NA','NAM',264),(148,'NAURU',520,'Nauru','NR','NRU',674),(149,'NEPAL',524,'Nepal','NP','NPL',977),(150,'NETHERLANDS',528,'Netherlands','NL','NLD',31),(151,'NETHERLANDS ANTILLES',530,'Netherlands Antilles','AN','ANT',599),(152,'NEW CALEDONIA',540,'New Caledonia','NC','NCL',687),(153,'NEW ZEALAND',554,'New Zealand','NZ','NZL',64),(154,'NICARAGUA',558,'Nicaragua','NI','NIC',505),(155,'NIGER',562,'Niger','NE','NER',227),(156,'NIGERIA',566,'Nigeria','NG','NGA',234),(157,'NIUE',570,'Niue','NU','NIU',683),(158,'NORFOLK ISLAND',574,'Norfolk Island','NF','NFK',672),(159,'NORTHERN MARIANA ISLANDS',580,'Northern Mariana Islands','MP','MNP',1670),(160,'NORWAY',578,'Norway','NO','NOR',47),(161,'OMAN',512,'Oman','OM','OMN',968),(162,'PAKISTAN',586,'Pakistan','PK','PAK',92),(163,'PALAU',585,'Palau','PW','PLW',680),(164,'PALESTINIAN TERRITORY, OCCUPIED',0,'Palestinian Territory, Occupied','PS','',970),(165,'PANAMA',591,'Panama','PA','PAN',507),(166,'PAPUA NEW GUINEA',598,'Papua New Guinea','PG','PNG',675),(167,'PARAGUAY',600,'Paraguay','PY','PRY',595),(168,'PERU',604,'Peru','PE','PER',51),(169,'PHILIPPINES',608,'Philippines','PH','PHL',63),(170,'PITCAIRN',612,'Pitcairn','PN','PCN',0),(171,'POLAND',616,'Poland','PL','POL',48),(172,'PORTUGAL',620,'Portugal','PT','PRT',351),(173,'PUERTO RICO',630,'Puerto Rico','PR','PRI',1787),(174,'QATAR',634,'Qatar','QA','QAT',974),(175,'REUNION',638,'Reunion','RE','REU',262),(176,'ROMANIA',642,'Romania','RO','ROM',40),(177,'RUSSIAN FEDERATION',643,'Russian Federation','RU','RUS',70),(178,'RWANDA',646,'Rwanda','RW','RWA',250),(179,'SAINT HELENA',654,'Saint Helena','SH','SHN',290),(180,'SAINT KITTS AND NEVIS',659,'Saint Kitts and Nevis','KN','KNA',1869),(181,'SAINT LUCIA',662,'Saint Lucia','LC','LCA',1758),(182,'SAINT PIERRE AND MIQUELON',666,'Saint Pierre and Miquelon','PM','SPM',508),(183,'SAINT VINCENT AND THE GRENADINES',670,'Saint Vincent and the Grenadines','VC','VCT',1784),(184,'SAMOA',882,'Samoa','WS','WSM',684),(185,'SAN MARINO',674,'San Marino','SM','SMR',378),(186,'SAO TOME AND PRINCIPE',678,'Sao Tome and Principe','ST','STP',239),(187,'SAUDI ARABIA',682,'Saudi Arabia','SA','SAU',966),(188,'SENEGAL',686,'Senegal','SN','SEN',221),(189,'SERBIA AND MONTENEGRO',0,'Serbia and Montenegro','CS','',381),(190,'SEYCHELLES',690,'Seychelles','SC','SYC',248),(191,'SIERRA LEONE',694,'Sierra Leone','SL','SLE',232),(192,'SINGAPORE',702,'Singapore','SG','SGP',65),(193,'SLOVAKIA',703,'Slovakia','SK','SVK',421),(194,'SLOVENIA',705,'Slovenia','SI','SVN',386),(195,'SOLOMON ISLANDS',90,'Solomon Islands','SB','SLB',677),(196,'SOMALIA',706,'Somalia','SO','SOM',252),(197,'SOUTH AFRICA',710,'South Africa','ZA','ZAF',27),(198,'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS',0,'South Georgia and the South Sandwich Islands','GS','',0),(199,'SPAIN',724,'Spain','ES','ESP',34),(200,'SRI LANKA',144,'Sri Lanka','LK','LKA',94),(201,'SUDAN',736,'Sudan','SD','SDN',249),(202,'SURINAME',740,'Suriname','SR','SUR',597),(203,'SVALBARD AND JAN MAYEN',744,'Svalbard and Jan Mayen','SJ','SJM',47),(204,'SWAZILAND',748,'Swaziland','SZ','SWZ',268),(205,'SWEDEN',752,'Sweden','SE','SWE',46),(206,'SWITZERLAND',756,'Switzerland','CH','CHE',41),(207,'SYRIAN ARAB REPUBLIC',760,'Syrian Arab Republic','SY','SYR',963),(208,'TAIWAN, PROVINCE OF CHINA',158,'Taiwan, Province of China','TW','TWN',886),(209,'TAJIKISTAN',762,'Tajikistan','TJ','TJK',992),(210,'TANZANIA, UNITED REPUBLIC OF',834,'Tanzania, United Republic of','TZ','TZA',255),(211,'THAILAND',764,'Thailand','TH','THA',66),(212,'TIMOR-LESTE',0,'Timor-Leste','TL','',670),(213,'TOGO',768,'Togo','TG','TGO',228),(214,'TOKELAU',772,'Tokelau','TK','TKL',690),(215,'TONGA',776,'Tonga','TO','TON',676),(216,'TRINIDAD AND TOBAGO',780,'Trinidad and Tobago','TT','TTO',1868),(217,'TUNISIA',788,'Tunisia','TN','TUN',216),(218,'TURKEY',792,'Turkey','TR','TUR',90),(219,'TURKMENISTAN',795,'Turkmenistan','TM','TKM',7370),(220,'TURKS AND CAICOS ISLANDS',796,'Turks and Caicos Islands','TC','TCA',1649),(221,'TUVALU',798,'Tuvalu','TV','TUV',688),(222,'UGANDA',800,'Uganda','UG','UGA',256),(223,'UKRAINE',804,'Ukraine','UA','UKR',380),(224,'UNITED ARAB EMIRATES',784,'United Arab Emirates','AE','ARE',971),(225,'UNITED KINGDOM',826,'United Kingdom','GB','GBR',44),(226,'UNITED STATES',840,'United States','US','USA',1),(227,'UNITED STATES MINOR OUTLYING ISLANDS',0,'United States Minor Outlying Islands','UM','',1),(228,'URUGUAY',858,'Uruguay','UY','URY',598),(229,'UZBEKISTAN',860,'Uzbekistan','UZ','UZB',998),(230,'VANUATU',548,'Vanuatu','VU','VUT',678),(231,'VENEZUELA',862,'Venezuela','VE','VEN',58),(232,'VIET NAM',704,'Viet Nam','VN','VNM',84),(233,'VIRGIN ISLANDS, BRITISH',92,'Virgin Islands, British','VG','VGB',1284),(234,'VIRGIN ISLANDS, U.S.',850,'Virgin Islands, U.s.','VI','VIR',1340),(235,'WALLIS AND FUTUNA',876,'Wallis and Futuna','WF','WLF',681),(236,'WESTERN SAHARA',732,'Western Sahara','EH','ESH',212),(237,'YEMEN',887,'Yemen','YE','YEM',967),(238,'ZAMBIA',894,'Zambia','ZM','ZMB',260),(239,'ZIMBABWE',716,'Zimbabwe','ZW','ZWE',263);
/*!40000 ALTER TABLE `account_country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_currency`
--

DROP TABLE IF EXISTS `account_currency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_currency` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(24) NOT NULL,
  `iso_code` varchar(3) NOT NULL,
  `sign` varchar(2) DEFAULT NULL,
  `sign_svg` longtext DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_currency`
--

LOCK TABLES `account_currency` WRITE;
/*!40000 ALTER TABLE `account_currency` DISABLE KEYS */;
INSERT INTO `account_currency` VALUES (1,'Dollar','usd','$','/static/dist/img/usd.svg'),(2,'Euro','eur','€','/static/dist/img/eur.svg'),(3,'British Pound','gbp','£','/static/dist/img/gbp.svg'),(4,'Israeli Shekels','ils','₪','/static/dist/img/ils.svg'),(5,'Australian Dollar','aud','A$','/static/dist/img/aud.svg');
/*!40000 ALTER TABLE `account_currency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_currencyexchangerate`
--

DROP TABLE IF EXISTS `account_currencyexchangerate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_currencyexchangerate` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `rate_date` date NOT NULL,
  `exchange_rate` decimal(5,2) NOT NULL,
  `from_currency_id` bigint(20) NOT NULL,
  `to_currency_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_currencyexchange_from_currency_id_to_curr_f32c4c0d_uniq` (`from_currency_id`,`to_currency_id`,`rate_date`),
  KEY `account_currencyexchangerate_from_currency_id_e1e19e8e` (`from_currency_id`),
  KEY `account_currencyexchangerate_to_currency_id_89967a16` (`to_currency_id`),
  CONSTRAINT `account_currencyexch_from_currency_id_e1e19e8e_fk_account_c` FOREIGN KEY (`from_currency_id`) REFERENCES `account_currency` (`id`),
  CONSTRAINT `account_currencyexch_to_currency_id_89967a16_fk_account_c` FOREIGN KEY (`to_currency_id`) REFERENCES `account_currency` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_currencyexchangerate`
--

LOCK TABLES `account_currencyexchangerate` WRITE;
/*!40000 ALTER TABLE `account_currencyexchangerate` DISABLE KEYS */;
INSERT INTO `account_currencyexchangerate` VALUES (21,'2024-04-05',0.92,1,2),(22,'2024-04-05',0.79,1,3),(23,'2024-04-05',3.73,1,4),(24,'2024-04-05',1.52,1,5),(25,'2024-04-05',1.08,2,1),(26,'2024-04-05',0.86,2,3),(27,'2024-04-05',4.04,2,4),(28,'2024-04-05',1.65,2,5),(29,'2024-04-05',1.26,3,1),(30,'2024-04-05',1.17,3,2),(31,'2024-04-05',4.71,3,4),(32,'2024-04-05',1.92,3,5),(33,'2024-04-05',0.27,4,1),(34,'2024-04-05',0.25,4,2),(35,'2024-04-05',0.21,4,3),(36,'2024-04-05',0.41,4,5),(37,'2024-04-05',0.66,5,1),(38,'2024-04-05',0.61,5,2),(39,'2024-04-05',0.52,5,3),(40,'2024-04-05',2.46,5,4);
/*!40000 ALTER TABLE `account_currencyexchangerate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_deliverypartner`
--

DROP TABLE IF EXISTS `account_deliverypartner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_deliverypartner` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `image` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_deliverypartner`
--

LOCK TABLES `account_deliverypartner` WRITE;
/*!40000 ALTER TABLE `account_deliverypartner` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_deliverypartner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_familymember`
--

DROP TABLE IF EXISTS `account_familymember`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_familymember` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fullname` varchar(50) NOT NULL,
  `relation` varchar(10) NOT NULL,
  `image` varchar(256) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `email_add` varchar(220) NOT NULL,
  `phone_num` varchar(17) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_familymember_user_id_d441c6c3_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_familymember`
--

LOCK TABLES `account_familymember` WRITE;
/*!40000 ALTER TABLE `account_familymember` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_familymember` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_flagged`
--

DROP TABLE IF EXISTS `account_flagged`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_flagged` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `reason` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `flagged_by_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_flagged_flagged_by_id_9df2cd94_fk_account_myuser_id` (`flagged_by_id`),
  KEY `account_flagged_user_id_e31a303d_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `account_flagged_flagged_by_id_9df2cd94_fk_account_myuser_id` FOREIGN KEY (`flagged_by_id`) REFERENCES `account_myuser` (`id`),
  CONSTRAINT `account_flagged_user_id_e31a303d_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_flagged`
--

LOCK TABLES `account_flagged` WRITE;
/*!40000 ALTER TABLE `account_flagged` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_flagged` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_location`
--

DROP TABLE IF EXISTS `account_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_location` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `location` longtext DEFAULT NULL,
  `latitude` decimal(10,5) NOT NULL,
  `longitude` decimal(10,5) NOT NULL,
  `address` longtext NOT NULL,
  `city` varchar(30) NOT NULL,
  `state` varchar(30) NOT NULL,
  `country` varchar(20) NOT NULL,
  `zipcode` varchar(12) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `store_manager_email` varchar(256) DEFAULT NULL,
  `store_manager_phone` varchar(17) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_location`
--

LOCK TABLES `account_location` WRITE;
/*!40000 ALTER TABLE `account_location` DISABLE KEYS */;
INSERT INTO `account_location` VALUES (1,'5 Pienza, Irvine, CA 92606, USA',33.69708,-117.80250,'undefined','Irvine','California','United States','92606','2024-04-30 16:19:35.198025',NULL,NULL),(2,'Israel',31.04605,34.85161,'undefined','Ramat ha Sharon','Dan Region','Israel','4720924','2024-05-01 11:29:43.833364',NULL,NULL),(3,'Ramat Gan, Israel',32.06842,34.82478,'undefined','Ramat Gan','Tel Aviv District','Israel','336611','2024-05-09 15:17:35.930487',NULL,NULL),(4,'Ramat Hasharon, Israel',32.13779,34.84028,'68 Bialik St,','Ramat Hasharon','Tel Aviv District','Israel','4720519','2024-05-15 04:00:06.572444',NULL,NULL),(5,'Israel',31.04605,34.85161,'75 derech hashalom','tel aviv','israel','Israel','6794223','2024-05-16 18:03:05.961560',NULL,NULL),(6,'Ramat Hasharon, Israel',32.13779,34.84028,'undefined','Ramat Hasharon','Tel Aviv District','Israel','4720924','2024-06-17 14:23:52.653872',NULL,NULL),(7,'5H3H+QMJ, Kannimadam, Anjugramam, Levinjipuram, Tamil Nadu 627114, India',8.15446,77.57914,'Kannimadam','Anjugramam','Tamil Nadu','India','627114','2024-07-17 04:55:20.950336',NULL,NULL),(8,'5H3H+QMJ, Kannimadam, Anjugramam, Levinjipuram, Tamil Nadu 627114, India',8.15446,77.57914,'Kannimadam','Anjugramam','Tamil Nadu','India','627114','2024-07-18 12:01:25.423211',NULL,NULL),(9,'Chennai, Tamil Nadu, India',13.08430,80.27046,'7, Customs Colony, Thuraipakkam','Chennai','Tamil Nadu','India','600097','2024-07-22 04:14:58.071460',NULL,NULL),(10,'233 S Wacker Dr, Chicago, IL 60606, USA',41.87895,-87.63591,'South Wacke','Chicago','Illinois','United States','60606','2024-07-25 08:53:25.389367',NULL,NULL),(11,'Kanniyakumari, Tamil Nadu, India',8.08435,77.54950,'','Kanniyakumari','Tamil Nadu','India','629702','2024-08-13 09:12:37.777511',NULL,NULL),(12,'123 William St, New York, NY 10038, USA',40.70948,-74.00730,'','New York','New York','United States','10038','2024-08-14 05:03:23.051839',NULL,NULL),(13,'Kanniyakumari, Tamil Nadu, India',8.08435,77.54950,'4/162A32,Sothiri Nager,Parakkai,Nagercoil','Kanniyakumari','Tamil Nadu','India','629601','2024-08-14 08:46:29.354489',NULL,NULL),(14,'Kanniyakumari, Tamil Nadu, India',8.08435,77.54950,'4/162A32,Sothiri Nager,Parakkai,Nagercoil','Kanniyakumari','Tamil Nadu','India','629601','2024-08-14 09:55:27.494198',NULL,NULL);
/*!40000 ALTER TABLE `account_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_myuser`
--

DROP TABLE IF EXISTS `account_myuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_myuser` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(220) NOT NULL,
  `phone` varchar(17) DEFAULT NULL,
  `firstname` varchar(40) DEFAULT NULL,
  `lastname` varchar(40) DEFAULT NULL,
  `language` varchar(20) NOT NULL,
  `image` varchar(256) NOT NULL,
  `cover_pic` varchar(256) NOT NULL,
  `paid_account` tinyint(1) NOT NULL,
  `about` longtext DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `administrator_name` varchar(100) DEFAULT NULL,
  `business_contact` varchar(11) DEFAULT NULL,
  `business_email` varchar(220) DEFAULT NULL,
  `website_url` longtext DEFAULT NULL,
  `facebook_url` longtext DEFAULT NULL,
  `twitter_url` longtext DEFAULT NULL,
  `instagram_url` longtext DEFAULT NULL,
  `youtube_url` longtext DEFAULT NULL,
  `newsletter_subscribed` tinyint(1) NOT NULL,
  `is_verified` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_type` varchar(20) NOT NULL,
  `country_id` bigint(20) DEFAULT NULL,
  `ngo_id` bigint(20) DEFAULT NULL,
  `plan_id` bigint(20) DEFAULT NULL,
  `business_category_id` bigint(20) DEFAULT NULL,
  `currency_id` bigint(20) DEFAULT NULL,
  `stripe_customer_id` varchar(100) DEFAULT NULL,
  `extra_deal` tinyint(1) NOT NULL,
  `extra_location` int(11) NOT NULL,
  `extra_classified` tinyint(1) NOT NULL,
  `is_approved` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `parent_id` bigint(20) DEFAULT NULL,
  `relation` varchar(10) DEFAULT NULL,
  `is_phone_verified` tinyint(1) NOT NULL,
  `delete_reason` varchar(50) DEFAULT NULL,
  `user_type_category_id` bigint(20) DEFAULT NULL,
  `extra_weekly_deal` tinyint(1) NOT NULL,
  `service_provider_type` varchar(16) DEFAULT NULL,
  `reservation_walkin` varchar(16) DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  `plan_upgrade_date` date DEFAULT NULL,
  `is_store` tinyint(1) NOT NULL,
  `is_default_ngo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `account_myuser_country_id_165d0424_fk_account_country_id` (`country_id`),
  KEY `account_myuser_ngo_id_58f46b1f_fk_account_myuser_id` (`ngo_id`),
  KEY `account_myuser_plan_id_b8c4994b_fk_account_plan_id` (`plan_id`),
  KEY `account_myuser_business_category_id_6f3811ff_fk_account_b` (`business_category_id`),
  KEY `account_myuser_currency_id_992bd67e_fk_account_currency_id` (`currency_id`),
  KEY `account_myuser_parent_id_be86bd2c_fk_account_myuser_id` (`parent_id`),
  KEY `account_myuser_user_type_category_i_cb0f20fe_fk_account_u` (`user_type_category_id`),
  CONSTRAINT `account_myuser_business_category_id_6f3811ff_fk_account_b` FOREIGN KEY (`business_category_id`) REFERENCES `account_businesscategory` (`id`),
  CONSTRAINT `account_myuser_country_id_165d0424_fk_account_country_id` FOREIGN KEY (`country_id`) REFERENCES `account_country` (`id`),
  CONSTRAINT `account_myuser_currency_id_992bd67e_fk_account_currency_id` FOREIGN KEY (`currency_id`) REFERENCES `account_currency` (`id`),
  CONSTRAINT `account_myuser_ngo_id_58f46b1f_fk_account_myuser_id` FOREIGN KEY (`ngo_id`) REFERENCES `account_myuser` (`id`),
  CONSTRAINT `account_myuser_parent_id_be86bd2c_fk_account_myuser_id` FOREIGN KEY (`parent_id`) REFERENCES `account_myuser` (`id`),
  CONSTRAINT `account_myuser_plan_id_b8c4994b_fk_account_plan_id` FOREIGN KEY (`plan_id`) REFERENCES `account_plan` (`id`),
  CONSTRAINT `account_myuser_user_type_category_i_cb0f20fe_fk_account_u` FOREIGN KEY (`user_type_category_id`) REFERENCES `account_usertypecategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_myuser`
--

LOCK TABLES `account_myuser` WRITE;
/*!40000 ALTER TABLE `account_myuser` DISABLE KEYS */;
INSERT INTO `account_myuser` VALUES (2,'pbkdf2_sha256$390000$Huhl1ncJmnOFb2K5FvkicK$HTQHpu2WKqsncctH69Plp0zeL10aX6TZJSNY36GmUlg=','2024-08-28 17:31:53.498732',1,'info@jflixs.com',NULL,NULL,NULL,'en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,1,0,'2024-04-05 07:29:26.253155','2024-06-17 14:15:09.834717','',NULL,NULL,NULL,NULL,1,NULL,0,0,0,1,0,NULL,NULL,0,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(3,'pbkdf2_sha256$390000$7dNPlZwzcbCn5h7fWbLJZC$QEpqY2VYnQffZHYnK4skG7FmoSnRb9bigGhP4wBqwD4=',NULL,0,'ngo.sofrik1@mailinator.com','+919199944398',NULL,NULL,'en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,NULL,'Smile Foundation','Sofrik',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-04-05 10:38:23.161994','2024-08-14 10:38:56.396768','ngo',99,NULL,NULL,NULL,1,NULL,0,0,0,1,0,NULL,NULL,0,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(4,'pbkdf2_sha256$390000$VsVeYMu8pTLHhMWrxOrNcK$6WBP8uHXi3+WyjYKI0XpX8zDecnEztJ/YETozgeKnhQ=',NULL,0,'dd89c7d1-c805-499b-992f-fb7eb91ba2e7','1714495195','3b4302e5-0b07-4106-9f9d-cc03abef6000','718fb338-d104-4b56-a009-e416f9d5c544','en','','',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0,0,'2024-04-06 05:43:15.228711','2024-04-30 16:39:55.851647','member',NULL,3,NULL,NULL,NULL,NULL,0,0,0,1,1,NULL,NULL,0,'not_say',NULL,0,NULL,NULL,1,NULL,0,0),(5,'pbkdf2_sha256$390000$bvqZG2l83Y1Z7Y8e2rIjNf$QuJZ//uA67eCz6a5WrfkF8ObuZjwYBUk8Ky2tEY0td4=',NULL,0,'bf86b88f-cb77-4c33-8020-96556f7472b4','1714495140','7ce793f2-5585-4454-a276-9f0fa67a8f78','1db2b0c1-7adc-4e0d-918f-edeceda36594','en','','',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0,0,'2024-04-07 06:33:06.452164','2024-04-30 16:39:00.940649','business',NULL,3,NULL,NULL,NULL,NULL,0,0,0,0,1,NULL,NULL,0,'not_say',NULL,0,NULL,NULL,1,NULL,0,0),(6,'pbkdf2_sha256$390000$HeQVjYXxU3JMwuS63OjcZz$+RoJiGjS/OVLCL5UYl63AYXso/dviZ939s1jYAPjYII=',NULL,0,'5feff0e4-beb4-4d63-b525-0905b79fbc0a','1714495157','4cd62711-0468-47e7-9d84-ec602e504d87','746c9f53-8e0b-432a-972f-221b60aa37d2','es','','',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0,0,'2024-04-26 12:36:44.687262','2024-04-30 16:39:17.154117','business',NULL,3,NULL,NULL,NULL,NULL,0,0,0,0,1,NULL,NULL,0,'not_say',NULL,0,NULL,NULL,1,NULL,0,0),(7,'pbkdf2_sha256$390000$WxcxUZHqEHcyFcDck7q3b4$i9CmGvg7UcIiLdWu0uwPeCSysbMjE0jFwsOF/H9gHtI=',NULL,0,'04c55aef-f26f-4315-ab98-35c833b874a7','1714495176','24b432a4-5956-40e8-87b6-8f2f1042e842','3e9892ae-0ed6-4935-a3ac-38a086222136','he','','',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0,0,'2024-04-29 10:43:52.400173','2024-04-30 16:39:36.437877','business',NULL,3,NULL,NULL,NULL,NULL,0,0,0,0,1,NULL,NULL,0,'not_say',NULL,0,NULL,NULL,1,NULL,0,0),(8,'pbkdf2_sha256$390000$YrVTAJdMawvo84kjN5VyxO$9MPhbn23/NSJx7R/i+v/8tySQprL1yo48tOvwl/PJfA=',NULL,0,'20556529-4fec-40de-a0fc-5595b4b5f379','1714495167','7a12928b-2c8c-4651-965c-2419f7d411c0','a468e049-cfa2-4142-8a6e-29b1edc3169d','he','','',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0,0,'2024-04-29 11:54:53.422228','2024-04-30 16:39:27.274970','business',NULL,3,NULL,NULL,NULL,NULL,0,0,0,0,1,NULL,NULL,0,'not_say',NULL,0,NULL,NULL,1,NULL,0,0),(9,'pbkdf2_sha256$390000$4UaJtltvdqc3EdjwbZjrww$emAEqMtzC5vMrr+5bVGNBQ7sMBzQfITUQBorZFJmVgw=',NULL,0,'84e3335a-fabd-49c8-b944-20f9ffdc42c7','1714495184','a41afb05-3041-48b1-8519-264d60ad074f','e7e70ade-ec01-46e5-afad-e31732db2a1c','he','','',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0,0,'2024-04-29 11:55:45.380497','2024-04-30 16:39:44.275536','business',NULL,3,NULL,NULL,NULL,NULL,0,0,0,0,1,NULL,NULL,0,'not_say',NULL,0,NULL,NULL,1,NULL,0,0),(10,'pbkdf2_sha256$390000$eXSNUQqDi2UMl7WhlvFpbz$WTxW5UpRSHZcrA0ohaM2bCapUkDw0hp6mulCCe3vToc=','2024-04-30 16:19:10.318531',0,'59636b80-edef-4a1c-9a9b-bb76d464d522','1717581724','5cf0e988-2ca3-4fe3-9fe4-2902bb286262','ad8b2bb9-84b1-4905-af7e-510e40e3322c','en','','',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-04-30 16:14:10.737761','2024-06-05 10:02:04.045346','member',NULL,3,2,NULL,NULL,NULL,0,-1,0,1,1,NULL,NULL,1,'not_say',NULL,0,NULL,NULL,1,'2024-04-30',0,0),(11,'pbkdf2_sha256$390000$IpnHAOl0ftEVNOON9MCCeo$bG52DYjjLnNZlqXOfwk86x2bY1GEtkQuFyb4wgLGSOQ=','2024-08-15 19:09:35.567543',0,'meuhud@gmail.com','+19258903111','Robbie','Michaelson','en','profile_pics/11/IMG_2500.jpeg','profile_cover_pics/11/IMG_3361.jpeg',0,'Co-founder of Shukdeals.com. Working to make the world a better place by supporting Non-Profits via patronizing our participating businesses worldwide.',NULL,NULL,NULL,NULL,NULL,'','','','',0,1,0,0,'2024-05-01 11:14:23.637092','2024-08-15 19:09:35.567738','member',104,3,1,NULL,4,NULL,0,-1,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(12,'pbkdf2_sha256$390000$5xy3mZxbSIFxHnjYXVExWp$8fVUsEmWeJ9oaTlg1wD/x8jb/s7qvU35rv3tPBuxQxs=',NULL,0,'ceo@adonmed.com','+919789845776',NULL,NULL,'en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,NULL,'Healthcare Technology Solutions','Stalin Selvamoni',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-05-01 14:22:47.759732','2024-05-14 15:20:27.228259','business',99,3,NULL,NULL,1,'cus_Q1hY7Zpw11zewI',0,0,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(13,'pbkdf2_sha256$390000$YcNVfpniRoH63hbyi4pcq7$jaculL3cK5an9LIgbsOSL2nywBrZ8Ei879dkR7hhYU4=','2024-05-15 10:08:37.959935',0,'karingeva10@gmail.com','+972549955702','Karin','Geva','he','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-05-08 14:21:44.320363','2024-05-15 10:08:37.960192','member',104,3,1,NULL,4,NULL,0,0,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(14,'pbkdf2_sha256$390000$TG6fhICX0ttdXUasaIqhPr$zgvReBaZUpJ9bkzzSLA14m6uISb/786+uF+etkOiUug=','2024-05-27 18:16:21.333018',0,'uchartarifsky@gmail.com','+972529538655','Uri','Chartarifsky','en','profile_pics/14/1000002755.jpg','profile_cover_pics/14/1000003955.png',0,'I stand with Israel',NULL,NULL,NULL,NULL,NULL,'','','','',0,1,0,0,'2024-05-09 15:10:49.669041','2024-05-27 18:16:21.333283','member',104,3,1,NULL,1,NULL,0,-1,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(15,'pbkdf2_sha256$390000$XIxct6WowwFO19JEoIxb29$ok2Nn7OP19cCbUyuXnF+X2JT4xEBhfJA/xsKup66e/w=','2024-05-31 09:14:58.414777',0,'aliyahfilmproductionsinc@gmail.com','+9720543092961',NULL,NULL,'en','profile_pics/15/IMG_3915.jpeg','default_images/default_cover_pic.png',1,'Holding Company for various projects and entities; including Aliyah Film Productions, Inc and Shukdeals.com.','JFLIXS LLC','REM',NULL,NULL,'https://www.shukdeals.com','','','','',0,1,0,0,'2024-05-12 14:34:56.881242','2024-05-31 09:14:58.414997','business',226,3,4,2,1,'cus_Q5pcPUs41GKzjm',0,0,0,1,0,NULL,NULL,1,NULL,NULL,0,'company',NULL,1,'2024-05-12',0,0),(16,'pbkdf2_sha256$390000$uRyLnsBZAGTEI3q8eNs8ph$a/CAQiLeoXN7WSaOrugFqtsbtuNMzhKuWqxb6wwee2Q=','2024-05-16 18:00:26.145155',0,'jhyman1122@gmail.com','+972586616496','Jerry','Hyman','en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,'professional actor/translator',NULL,NULL,NULL,NULL,NULL,'','','','',0,1,0,0,'2024-05-16 14:09:25.314478','2024-05-16 18:03:05.964324','member',104,3,1,NULL,4,NULL,0,-1,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(17,'pbkdf2_sha256$390000$8dQQgWrYwk0pTyG05LdJ2v$S3Uy2T7Te8LRTzgE95oqdOQgYJy8QCgRdWAcaKOy5/0=','2024-06-06 06:20:43.097810',0,'rakesh5june1@mailinator.com','+919899944398','Rakesh','Kumar','en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-06-05 10:02:11.277085','2024-06-06 06:20:43.098081','member',99,3,1,NULL,2,'cus_QEkApgy6euKxuJ',0,0,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(18,'pbkdf2_sha256$390000$NVuhXNnzWQPVsreW4FLDTA$jN22QUu/Vw2rdm5XT0AZg5RKv0eWyHmBdMMn+beEhQY=','2024-07-01 06:56:16.901215',0,'lamborghini.robbie@gmail.com','+9720505530985','Robbie','Michaelson','en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,'better than most but still a work in progress',NULL,NULL,NULL,NULL,NULL,'','','','',0,1,0,0,'2024-06-17 14:19:44.742727','2024-07-01 06:56:16.901376','member',104,3,1,NULL,4,NULL,0,-1,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(19,'pbkdf2_sha256$390000$5i7eGUPEKSpCdV8lu69DKg$8ypM61CRwXg+RtcDu2EUuVgTFppOShtco1yjl7IdpiI=','2024-08-22 18:46:20.894743',0,'slenins@gmail.com','+919884653800','Lenin','S','en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-06-26 14:49:45.537408','2024-08-22 18:46:20.894996','member',226,3,1,NULL,1,'cus_QMgZzymNsDwq4B',0,0,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(20,'pbkdf2_sha256$390000$PnWiQfvDu5gUXRHr39k2FB$XWi4GQZ4mt+UKDkUMTEalahbn7zwpyoLUau/+pEjIeI=','2024-07-05 14:20:27.419677',0,'htobochnik@gmail.com','+9720587908939','Howard','Tobochnik','en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-07-05 14:19:50.882929','2024-07-05 14:20:27.419914','member',104,3,1,NULL,1,NULL,0,0,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(21,'pbkdf2_sha256$390000$nyVE3G6uIq6YvLdnbEcjua$qDClIFLDgBzQL3Xj6oe/7NaJ1ahw58krXFw1HRwTbfo=','2024-08-14 09:45:05.015346',0,'admininfo@v2wss.com','+918248183180','Admin','V2W','en','profile_pics/21/profile_pic.jpeg','profile_cover_pics/21/default_cover_pic.png',0,'Worker at v2w.',NULL,NULL,NULL,NULL,NULL,'','','','',0,1,0,0,'2024-07-17 04:49:47.787493','2024-08-14 09:45:26.644695','member',226,30,1,NULL,1,NULL,0,-1,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(22,'pbkdf2_sha256$390000$Pzpq4qdGmInxOjrydILN5J$PbYClbPnRS2zbMu5iJcqyqlZVRRLWRdOM2KqJL9QERI=','2024-07-23 09:58:16.208848',0,'prabhu.s@v2wss.com','+919750335074',NULL,NULL,'en','profile_pics/22/eagle_logo.jpg','profile_cover_pics/22/eg_cover.jpg',0,'Village to World','V2WSS','Administrator',NULL,NULL,'https://example.com','','','','',0,1,0,0,'2024-07-18 11:06:14.332296','2024-08-14 10:39:02.871101','ngo',226,NULL,NULL,NULL,1,NULL,0,-1,0,1,0,NULL,NULL,1,NULL,4,0,NULL,NULL,1,NULL,0,0),(23,'pbkdf2_sha256$390000$wL438nLgqehTI9IYCJyCkb$thbOhSvKQjzdO0K7k2vysLYuppTXYjpZ4i5RuYzt+MM=','2024-08-03 06:32:15.042769',0,'selvamoni@gmail.com','+919940435834','Stalin','Selvamoni','en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',1,'I am an Entrepreneur in Medical Technology Solutions',NULL,NULL,NULL,NULL,NULL,'','','','',0,1,0,0,'2024-07-22 04:04:41.044472','2024-08-03 06:32:15.043012','member',99,3,2,NULL,1,'cus_QWG5NmOOPOZKlE',0,-1,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,'2024-07-22',0,0),(24,'pbkdf2_sha256$390000$o5TD2qlIbg4qM8e77t5XG1$sgXyi35r5UeOJDacpNe1W+FKCdg0OfuKhBrm3zEjXu8=','2024-08-14 09:40:04.609126',0,'arunasalam.g@v2wss.com','+916382056187','Arun','G','en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,'Devops Engg.',NULL,NULL,NULL,NULL,NULL,'','','','',0,1,0,0,'2024-07-25 08:47:50.107817','2024-08-14 09:40:04.609386','member',99,22,1,NULL,1,'cus_QXTouDDX8QkLxK',0,-1,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(25,'pbkdf2_sha256$390000$bZZGzxWAv5SCQNbOKaf7s4$H1w4nLm+ep5ejVBephM7w05yUOp1SWc6M/dGqyS/BUE=','2024-08-21 09:38:35.019988',0,'sammatrix2020@gmail.com','+15488835166','Sam','Hussain','en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-07-31 17:03:33.867649','2024-08-21 09:38:35.020354','member',99,3,1,NULL,1,NULL,0,0,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(26,'pbkdf2_sha256$390000$Y6naybMEdIs9qYfkReI0VQ$R9vhT94BJUrbeavBvddUfjfQ1WUfKKSFT6yaQeGwThw=',NULL,0,'40612cec-7f1b-4ea5-b3ec-3ea1dc760aad','1723406965','b3847c8d-424e-4d7d-b097-9f46367a2960','75c97fed-8f67-48ef-b471-2252982cccea','en','','',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-08-11 20:05:38.936547','2024-08-11 20:09:25.768653','member',NULL,3,NULL,NULL,NULL,NULL,0,0,0,1,1,NULL,NULL,1,'expectation_not_meet',NULL,0,NULL,NULL,1,NULL,0,0),(27,'pbkdf2_sha256$390000$uAdGwVUdVDU8aqo7yHjCGJ$dDp10Cj6F2dZxa3ZonGuVmjNo+4a42MuYN9JUYj/ehk=','2024-08-12 15:41:23.310210',0,'adonmedtech@gmail.com','+919344227374',NULL,NULL,'en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,NULL,'Adon Med','Lenin',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-08-11 20:11:03.282966','2024-08-12 15:41:23.310470','ngo',99,NULL,NULL,NULL,1,NULL,0,0,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(28,'pbkdf2_sha256$390000$nHHTgAp85mx59wlzzJEPvZ$NPD5IaQHMAGaNCG/qiAQzHcYkQLmBoZG/p6c2B1c88U=',NULL,0,'lselvamony@gmail.com','+918056910202',NULL,NULL,'en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,NULL,'Lenin S','Lenin S',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-08-11 20:18:38.884162','2024-08-11 20:20:22.213361','business',99,27,NULL,NULL,1,'cus_Qe0GKiKNP3tiyp',0,0,0,0,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(29,'pbkdf2_sha256$390000$lvghI0h6Kl4jkEPvHeYklr$Bie+xDDFgS61QMS4jWI+jsntVrtDI0eBIl4CiLIlP54=',NULL,0,'sreengl@gmail.com','+14048836159',NULL,NULL,'en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,NULL,'The Test NGO','Sree',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-08-13 07:25:30.283941','2024-08-13 10:37:00.348807','ngo',226,NULL,NULL,NULL,1,NULL,0,0,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(30,'pbkdf2_sha256$390000$e5BAJmlRVhNWB3UYOClI2L$qo/+d8/PCWqIcNW4fas7mh24tUR646mRnNHMlZL0gHc=','2024-08-14 09:45:53.965905',0,'karan.k@v2wss.com','+919789330586',NULL,NULL,'en','profile_pics/30/86e764c3-df2b-4129-8150-6e14812bc6ac.png','default_images/default_cover_pic.png',0,'Village to world','V2Wsoftwaresolutions','Karan',NULL,NULL,'null','','','','',0,1,0,0,'2024-08-14 08:42:14.226868','2024-08-14 10:39:02.874312','ngo',99,NULL,NULL,NULL,1,NULL,0,-1,0,1,0,NULL,NULL,1,NULL,9,0,NULL,NULL,1,NULL,0,1),(31,'pbkdf2_sha256$390000$l7cuEBxS8Hm6ZdpDH6VP1A$CKtuKF1qNjdlyy1/sWHTWCtGTQbcyixA6ochpGVpAac=',NULL,0,'f0139bfd-cfe8-4c02-8a05-622efeb35ddd','1723625960','314be646-63ea-45ca-beea-01b37f6e938e','8584e1e8-5b7a-4245-8e1b-553330fc80c9','en','','',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-08-14 08:51:34.905363','2024-08-14 08:59:20.183038','business',NULL,30,NULL,NULL,NULL,NULL,0,0,0,1,1,NULL,NULL,1,'expectation_not_meet',NULL,0,NULL,NULL,1,NULL,0,0),(32,'pbkdf2_sha256$390000$8uhp9wWRKsBe8pHx6EzNOU$80WqenBMxBtEcb7KYgaNqO2PptRfuqRVVmHtrdEQFIs=',NULL,0,'81646f15-1874-45ff-b5d4-c6deb739c7dd','1723628807','1cc8d3af-81c4-4cb1-8180-0cc0c9276df1','4b79577a-6633-4683-b588-32d203365c47','en','','',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-08-14 08:59:44.439183','2024-08-14 09:46:47.214149','business',NULL,30,NULL,NULL,NULL,NULL,0,0,0,0,1,NULL,NULL,1,'handling_issue',NULL,0,NULL,NULL,1,NULL,0,0),(33,'pbkdf2_sha256$390000$zni4yIHGey1xHApHL3fdnm$p+yyEzcJpk3DhscfazWEnTDZjqsB+fn2y+agt30b+x4=',NULL,0,'karan.k@v2wss.co','+919789330587','kottar','k','en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0,0,'2024-08-14 09:32:24.651570','2024-08-14 09:32:24.917386','member',99,30,NULL,NULL,1,NULL,0,0,0,1,0,NULL,NULL,0,NULL,NULL,0,NULL,NULL,1,NULL,0,0),(34,'pbkdf2_sha256$390000$5COkTqivvryAKOvlGzf375$OfYq/ocrHJNP1+0AlKvhIwGP/3NmIhI+jAb/MUFZXgI=',NULL,0,'b2661922-74e1-44d3-a52e-fb91b251f75c','1723629088','208d0846-2f6e-426c-8eef-08a166bc3fd3','1f90dd09-574a-4119-9dec-45cf59f16aeb','en','','',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-08-14 09:49:21.360637','2024-08-14 09:51:28.402180','member',NULL,29,NULL,NULL,NULL,NULL,0,0,0,1,1,NULL,NULL,1,'choices_issue',NULL,0,NULL,NULL,1,NULL,0,0),(35,'pbkdf2_sha256$390000$YqdJxKmFKYunO8pgaRug7y$PyVl72A5rUpvkjdwRGUQpc9xV1UPICi19LBhR0W3UFQ=','2024-08-14 10:21:30.836683',0,'072590e7-f02c-47fc-a7cc-55014697b103','1723630884','686d9ffb-b95d-4498-818f-720b18cdf5da','b5c33349-2619-42c3-98d4-ebba5fb10e10','en','','',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-08-14 09:52:47.517764','2024-08-14 10:21:30.837076','member',NULL,22,1,NULL,NULL,NULL,0,-1,0,1,1,NULL,NULL,1,'expensive',NULL,0,NULL,NULL,1,NULL,0,0),(36,'pbkdf2_sha256$390000$BMGXXjxByDvS4F8Annp9MH$qu0f2l+jZxsFLK/vQZQ8KjP6WMArPs7hXjJSA6XYrn8=',NULL,0,'thangabalan.i@v2wss.com','+919080988352',NULL,NULL,'en','default_images/default_profile_pic.jpeg','default_images/default_cover_pic.png',0,NULL,'V2WSS','Prabu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,0,0,'2024-08-14 10:27:00.443719','2024-08-14 10:41:46.342012','business',99,30,NULL,NULL,1,'cus_QeyW3bm4jnnbP9',0,0,0,1,0,NULL,NULL,1,NULL,NULL,0,NULL,NULL,1,NULL,0,0);
/*!40000 ALTER TABLE `account_myuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_myuser_delivery_partner`
--

DROP TABLE IF EXISTS `account_myuser_delivery_partner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_myuser_delivery_partner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` bigint(20) NOT NULL,
  `deliverypartner_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_myuser_delivery__myuser_id_deliverypartne_cdc2cf8c_uniq` (`myuser_id`,`deliverypartner_id`),
  KEY `account_myuser_deliv_deliverypartner_id_fd622e66_fk_account_d` (`deliverypartner_id`),
  CONSTRAINT `account_myuser_deliv_deliverypartner_id_fd622e66_fk_account_d` FOREIGN KEY (`deliverypartner_id`) REFERENCES `account_deliverypartner` (`id`),
  CONSTRAINT `account_myuser_deliv_myuser_id_3177f355_fk_account_m` FOREIGN KEY (`myuser_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_myuser_delivery_partner`
--

LOCK TABLES `account_myuser_delivery_partner` WRITE;
/*!40000 ALTER TABLE `account_myuser_delivery_partner` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_myuser_delivery_partner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_myuser_favourite_classified`
--

DROP TABLE IF EXISTS `account_myuser_favourite_classified`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_myuser_favourite_classified` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` bigint(20) NOT NULL,
  `classified_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_myuser_favourite_myuser_id_classified_id_f96c64b5_uniq` (`myuser_id`,`classified_id`),
  KEY `account_myuser_favou_classified_id_438a264d_fk_classifie` (`classified_id`),
  CONSTRAINT `account_myuser_favou_classified_id_438a264d_fk_classifie` FOREIGN KEY (`classified_id`) REFERENCES `classifieds_classified` (`id`),
  CONSTRAINT `account_myuser_favou_myuser_id_7b3a7dad_fk_account_m` FOREIGN KEY (`myuser_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_myuser_favourite_classified`
--

LOCK TABLES `account_myuser_favourite_classified` WRITE;
/*!40000 ALTER TABLE `account_myuser_favourite_classified` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_myuser_favourite_classified` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_myuser_favourite_deal`
--

DROP TABLE IF EXISTS `account_myuser_favourite_deal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_myuser_favourite_deal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` bigint(20) NOT NULL,
  `deal_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_myuser_favourite_deal_myuser_id_deal_id_f18e1927_uniq` (`myuser_id`,`deal_id`),
  KEY `account_myuser_favourite_deal_deal_id_bde74f4d_fk_deals_deal_id` (`deal_id`),
  CONSTRAINT `account_myuser_favou_myuser_id_a2a80043_fk_account_m` FOREIGN KEY (`myuser_id`) REFERENCES `account_myuser` (`id`),
  CONSTRAINT `account_myuser_favourite_deal_deal_id_bde74f4d_fk_deals_deal_id` FOREIGN KEY (`deal_id`) REFERENCES `deals_deal` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_myuser_favourite_deal`
--

LOCK TABLES `account_myuser_favourite_deal` WRITE;
/*!40000 ALTER TABLE `account_myuser_favourite_deal` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_myuser_favourite_deal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_myuser_favourite_job`
--

DROP TABLE IF EXISTS `account_myuser_favourite_job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_myuser_favourite_job` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` bigint(20) NOT NULL,
  `job_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_myuser_favourite_job_myuser_id_job_id_f2e4d75f_uniq` (`myuser_id`,`job_id`),
  KEY `account_myuser_favourite_job_job_id_dab6e67c_fk_jobs_job_id` (`job_id`),
  CONSTRAINT `account_myuser_favou_myuser_id_46ca267e_fk_account_m` FOREIGN KEY (`myuser_id`) REFERENCES `account_myuser` (`id`),
  CONSTRAINT `account_myuser_favourite_job_job_id_dab6e67c_fk_jobs_job_id` FOREIGN KEY (`job_id`) REFERENCES `jobs_job` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_myuser_favourite_job`
--

LOCK TABLES `account_myuser_favourite_job` WRITE;
/*!40000 ALTER TABLE `account_myuser_favourite_job` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_myuser_favourite_job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_myuser_favourite_ngo_video`
--

DROP TABLE IF EXISTS `account_myuser_favourite_ngo_video`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_myuser_favourite_ngo_video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` bigint(20) NOT NULL,
  `ngovideo_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_myuser_favourite_myuser_id_ngovideo_id_2a4077b3_uniq` (`myuser_id`,`ngovideo_id`),
  KEY `account_myuser_favou_ngovideo_id_a0328eb4_fk_account_n` (`ngovideo_id`),
  CONSTRAINT `account_myuser_favou_myuser_id_8f63c24b_fk_account_m` FOREIGN KEY (`myuser_id`) REFERENCES `account_myuser` (`id`),
  CONSTRAINT `account_myuser_favou_ngovideo_id_a0328eb4_fk_account_n` FOREIGN KEY (`ngovideo_id`) REFERENCES `account_ngovideo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_myuser_favourite_ngo_video`
--

LOCK TABLES `account_myuser_favourite_ngo_video` WRITE;
/*!40000 ALTER TABLE `account_myuser_favourite_ngo_video` DISABLE KEYS */;
INSERT INTO `account_myuser_favourite_ngo_video` VALUES (1,21,1);
/*!40000 ALTER TABLE `account_myuser_favourite_ngo_video` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_myuser_favourite_user`
--

DROP TABLE IF EXISTS `account_myuser_favourite_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_myuser_favourite_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_myuser_id` bigint(20) NOT NULL,
  `to_myuser_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_myuser_favourite_from_myuser_id_to_myuser_52ca7062_uniq` (`from_myuser_id`,`to_myuser_id`),
  KEY `account_myuser_favou_to_myuser_id_6353d957_fk_account_m` (`to_myuser_id`),
  CONSTRAINT `account_myuser_favou_from_myuser_id_7c5f0649_fk_account_m` FOREIGN KEY (`from_myuser_id`) REFERENCES `account_myuser` (`id`),
  CONSTRAINT `account_myuser_favou_to_myuser_id_6353d957_fk_account_m` FOREIGN KEY (`to_myuser_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_myuser_favourite_user`
--

LOCK TABLES `account_myuser_favourite_user` WRITE;
/*!40000 ALTER TABLE `account_myuser_favourite_user` DISABLE KEYS */;
INSERT INTO `account_myuser_favourite_user` VALUES (1,21,22);
/*!40000 ALTER TABLE `account_myuser_favourite_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_myuser_groups`
--

DROP TABLE IF EXISTS `account_myuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_myuser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_myuser_groups_myuser_id_group_id_7d7152e7_uniq` (`myuser_id`,`group_id`),
  KEY `account_myuser_groups_group_id_44b24908_fk_auth_group_id` (`group_id`),
  CONSTRAINT `account_myuser_groups_group_id_44b24908_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `account_myuser_groups_myuser_id_5adbe57d_fk_account_myuser_id` FOREIGN KEY (`myuser_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_myuser_groups`
--

LOCK TABLES `account_myuser_groups` WRITE;
/*!40000 ALTER TABLE `account_myuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_myuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_myuser_user_permissions`
--

DROP TABLE IF EXISTS `account_myuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_myuser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_myuser_user_perm_myuser_id_permission_id_36f9bf13_uniq` (`myuser_id`,`permission_id`),
  KEY `account_myuser_user__permission_id_17807c80_fk_auth_perm` (`permission_id`),
  CONSTRAINT `account_myuser_user__myuser_id_cdc8ab14_fk_account_m` FOREIGN KEY (`myuser_id`) REFERENCES `account_myuser` (`id`),
  CONSTRAINT `account_myuser_user__permission_id_17807c80_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_myuser_user_permissions`
--

LOCK TABLES `account_myuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `account_myuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_myuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_ngopayout`
--

DROP TABLE IF EXISTS `account_ngopayout`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_ngopayout` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `amount` double NOT NULL,
  `payout` tinyint(1) NOT NULL,
  `payout_date` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `ngo_id` bigint(20) DEFAULT NULL,
  `paid_by_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `payment_detail_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `account_ngopayout_ngo_id_7ac40c12_fk_account_myuser_id` (`ngo_id`),
  KEY `account_ngopayout_paid_by_id_1f2d8b82_fk_account_myuser_id` (`paid_by_id`),
  KEY `account_ngopayout_user_id_994b63df_fk_account_myuser_id` (`user_id`),
  KEY `account_ngopayout_payment_detail_id_a64d9a39_fk_account_p` (`payment_detail_id`),
  CONSTRAINT `account_ngopayout_ngo_id_7ac40c12_fk_account_myuser_id` FOREIGN KEY (`ngo_id`) REFERENCES `account_myuser` (`id`),
  CONSTRAINT `account_ngopayout_paid_by_id_1f2d8b82_fk_account_myuser_id` FOREIGN KEY (`paid_by_id`) REFERENCES `account_myuser` (`id`),
  CONSTRAINT `account_ngopayout_payment_detail_id_a64d9a39_fk_account_p` FOREIGN KEY (`payment_detail_id`) REFERENCES `account_paymentdetail` (`id`),
  CONSTRAINT `account_ngopayout_user_id_994b63df_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_ngopayout`
--

LOCK TABLES `account_ngopayout` WRITE;
/*!40000 ALTER TABLE `account_ngopayout` DISABLE KEYS */;
INSERT INTO `account_ngopayout` VALUES (1,0.99,0,NULL,'2024-04-30 16:18:48.352470',3,NULL,10,1),(2,9.9,0,NULL,'2024-05-12 17:58:31.740891',3,NULL,15,4),(3,1,0,NULL,'2024-07-22 04:12:58.707895',3,NULL,23,18);
/*!40000 ALTER TABLE `account_ngopayout` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_ngoreferaltoken`
--

DROP TABLE IF EXISTS `account_ngoreferaltoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_ngoreferaltoken` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `referal_token` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_ngoreferaltoken_user_id_92ae76c5_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_ngoreferaltoken`
--

LOCK TABLES `account_ngoreferaltoken` WRITE;
/*!40000 ALTER TABLE `account_ngoreferaltoken` DISABLE KEYS */;
INSERT INTO `account_ngoreferaltoken` VALUES (1,'de56d8bb-db26-4fe6-b9ea-880c9db2fef9','2024-04-05 10:38:23.427004',3),(2,'5964665a-2abf-4fdd-b2f2-df4e02f9bb7a','2024-07-18 11:06:14.753318',22),(3,'0a3ba158-4fa1-4459-9eb7-474e6a01225f','2024-08-11 20:11:03.565500',27),(4,'83d21ee7-f2e9-47e8-b416-bf88819b0f56','2024-08-13 07:25:30.553305',29),(5,'de4e2222-5dfb-4ace-b65d-8bfef122753b','2024-08-14 08:42:14.523702',30);
/*!40000 ALTER TABLE `account_ngoreferaltoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_ngovideo`
--

DROP TABLE IF EXISTS `account_ngovideo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_ngovideo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `link` varchar(200) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_ngovideo_user_id_3bf698b6_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `account_ngovideo_user_id_3bf698b6_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_ngovideo`
--

LOCK TABLES `account_ngovideo` WRITE;
/*!40000 ALTER TABLE `account_ngovideo` DISABLE KEYS */;
INSERT INTO `account_ngovideo` VALUES (1,'Discover the impact of AI on the scientific operations of NASA\'s Mars Rover','https://youtu.be/VMAXwYd21ME?si=yyLrKraUp3AfCzyl','2024-07-18 12:05:39.132123','2024-07-18 12:05:39.132159',22),(2,'Discover the impact of AI on the scientific operations of NASA\'s Mars Rover','https://youtu.be/VMAXwYd21ME?si=yyLrKraUp3AfCzyl','2024-07-18 12:05:39.425022','2024-07-18 12:05:39.425059',22),(3,'Stegosaurus Fossil up for auction in New York','https://youtu.be/RWZo0LkG_zA?si=sq4Gq8AT9qNcbJ9R','2024-07-18 12:09:41.935143','2024-07-18 12:09:41.935182',22);
/*!40000 ALTER TABLE `account_ngovideo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_onelineuser`
--

DROP TABLE IF EXISTS `account_onelineuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_onelineuser` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_onelineuser_user_id_c10daa62_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `account_onelineuser_user_id_c10daa62_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_onelineuser`
--

LOCK TABLES `account_onelineuser` WRITE;
/*!40000 ALTER TABLE `account_onelineuser` DISABLE KEYS */;
INSERT INTO `account_onelineuser` VALUES (1,'2024-04-30 16:19:10.322738',10),(4,'2024-05-08 14:27:56.496170',13),(5,'2024-05-09 15:12:49.676081',14),(7,'2024-05-15 10:08:37.963573',13),(8,'2024-05-16 18:00:26.149007',16),(10,'2024-05-19 12:20:13.609500',14),(15,'2024-05-21 08:29:58.115257',14),(18,'2024-05-27 18:16:21.335866',14),(23,'2024-06-05 10:04:13.725541',17),(24,'2024-06-05 10:16:17.474206',17),(25,'2024-06-06 06:20:43.100643',17),(32,'2024-07-05 14:20:27.422988',20),(40,'2024-07-23 09:58:16.212908',22),(42,'2024-07-31 17:05:13.179703',25),(44,'2024-08-03 21:29:01.176281',25),(45,'2024-08-03 21:29:01.895564',25),(50,'2024-08-12 15:41:23.313311',27),(53,'2024-08-12 16:24:47.255313',19),(54,'2024-08-13 06:25:12.243235',19),(60,'2024-08-14 09:40:04.611967',24),(62,'2024-08-14 09:45:04.747373',21),(63,'2024-08-14 09:45:05.018344',21),(66,'2024-08-14 19:11:33.751636',25),(67,'2024-08-14 19:13:17.388257',19),(68,'2024-08-14 19:15:10.208727',19),(69,'2024-08-14 19:16:27.427286',19),(72,'2024-08-20 02:26:08.366118',25),(73,'2024-08-21 07:59:22.723913',25),(74,'2024-08-21 09:38:35.023836',25),(75,'2024-08-22 18:46:20.897670',19);
/*!40000 ALTER TABLE `account_onelineuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_paymentdetail`
--

DROP TABLE IF EXISTS `account_paymentdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_paymentdetail` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `item_type` varchar(20) NOT NULL,
  `locations_to_activate` int(11) NOT NULL,
  `amount` double NOT NULL,
  `currency` varchar(10) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `description` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `plan_to_activate_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `main_amount_in_usd` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_paymentdetai_plan_to_activate_id_9e3874ef_fk_account_p` (`plan_to_activate_id`),
  KEY `account_paymentdetail_user_id_25b0477d_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `account_paymentdetai_plan_to_activate_id_9e3874ef_fk_account_p` FOREIGN KEY (`plan_to_activate_id`) REFERENCES `account_plan` (`id`),
  CONSTRAINT `account_paymentdetail_user_id_25b0477d_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_paymentdetail`
--

LOCK TABLES `account_paymentdetail` WRITE;
/*!40000 ALTER TABLE `account_paymentdetail` DISABLE KEYS */;
INSERT INTO `account_paymentdetail` VALUES (1,'plan',0,6.71,'ils','complete',NULL,'2024-04-30 16:16:30.240580',2,10,1.8),(2,'plan',0,18,'usd','pending',NULL,'2024-05-01 14:29:10.697030',4,12,18),(3,'plan',0,18,'usd','pending',NULL,'2024-05-12 15:05:15.307495',4,15,18),(4,'plan',0,18,'usd','complete',NULL,'2024-05-12 17:54:47.558223',4,15,18),(5,'classified',0,14.17,'ils','pending',NULL,'2024-05-20 14:45:10.268416',NULL,11,1.8),(6,'classified',0,14.17,'ils','pending',NULL,'2024-05-20 14:55:18.321938',NULL,11,1.8),(7,'classified',0,14.17,'ils','pending',NULL,'2024-05-21 08:37:29.987366',NULL,11,1.8),(8,'weekly_deal',0,12,'usd','pending',NULL,'2024-05-21 09:08:47.345194',NULL,15,10),(9,'classified',0,7.46,'ils','pending',NULL,'2024-05-31 09:25:57.684715',NULL,11,0),(10,'classified',0,7.46,'ils','pending',NULL,'2024-05-31 09:42:51.868355',NULL,11,0),(11,'plan',0,1.66,'eur','pending',NULL,'2024-06-05 10:03:15.326101',2,17,1.8),(12,'classified',0,1.84,'eur','pending',NULL,'2024-06-05 10:06:26.103514',NULL,17,0),(13,'plan',0,18,'usd','cancelled',NULL,'2024-06-10 15:50:43.702496',4,12,18),(14,'plan',0,18,'usd','cancelled',NULL,'2024-06-10 15:53:39.217226',4,12,18),(15,'plan',0,18,'usd','pending',NULL,'2024-07-22 03:58:27.859305',4,12,18),(16,'plan',0,18,'usd','pending',NULL,'2024-07-22 03:58:28.455754',4,12,18),(17,'plan',0,18,'usd','pending',NULL,'2024-07-22 03:58:54.013006',4,12,18),(18,'plan',0,1.8,'usd','complete',NULL,'2024-07-22 04:09:57.736795',2,23,1.8),(19,'plan',0,1.8,'usd','pending',NULL,'2024-08-11 20:07:57.904300',2,26,1.8),(20,'plan',0,18,'usd','pending',NULL,'2024-08-11 20:20:20.945914',4,28,18),(21,'plan',0,18,'usd','pending',NULL,'2024-08-14 09:00:56.419571',4,32,18),(22,'plan',0,18,'usd','pending',NULL,'2024-08-14 10:36:35.972579',4,36,18),(23,'plan',0,18,'usd','pending',NULL,'2024-08-14 10:36:36.125211',4,36,18),(24,'plan',0,0.12,'usd','pending',NULL,'2024-08-14 10:42:58.125583',4,36,0.12);
/*!40000 ALTER TABLE `account_paymentdetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_plan`
--

DROP TABLE IF EXISTS `account_plan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_plan` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_type` varchar(20) NOT NULL,
  `name` varchar(10) NOT NULL,
  `amount` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_plan`
--

LOCK TABLES `account_plan` WRITE;
/*!40000 ALTER TABLE `account_plan` DISABLE KEYS */;
INSERT INTO `account_plan` VALUES (1,'member','Free',0),(2,'member','Hamsa',1.8),(3,'business','Delete',0),(4,'business','Hamsa',18),(5,'business','Corporate',100);
/*!40000 ALTER TABLE `account_plan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_planfeature`
--

DROP TABLE IF EXISTS `account_planfeature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_planfeature` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feature` varchar(100) NOT NULL,
  `plan_id` bigint(20) NOT NULL,
  `numbers_allowed` int(11) NOT NULL,
  `feature_type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_planfeature_plan_id_2e28af9e_fk_account_plan_id` (`plan_id`),
  CONSTRAINT `account_planfeature_plan_id_2e28af9e_fk_account_plan_id` FOREIGN KEY (`plan_id`) REFERENCES `account_plan` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_planfeature`
--

LOCK TABLES `account_planfeature` WRITE;
/*!40000 ALTER TABLE `account_planfeature` DISABLE KEYS */;
INSERT INTO `account_planfeature` VALUES (1,'Classifieds',1,0,'classified'),(4,'Classifieds',2,10000,'classified'),(7,'Listing',3,10000,'deal'),(10,'Listing',4,10000,'deal'),(13,'Location',4,1,'location'),(14,'Listing',5,10000,'deal'),(17,'Locations',5,10,'location'),(27,'Location',3,1,'location');
/*!40000 ALTER TABLE `account_planfeature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_productprice`
--

DROP TABLE IF EXISTS `account_productprice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_productprice` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) NOT NULL,
  `cost` double NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_productprice`
--

LOCK TABLES `account_productprice` WRITE;
/*!40000 ALTER TABLE `account_productprice` DISABLE KEYS */;
INSERT INTO `account_productprice` VALUES (1,'SINGLE_DEAL_COST',18,'2024-05-21 09:18:34.449376','2023-11-23 15:00:56.000000'),(2,'SINGLE_WEEKLY_DEAL_COST',18,'2024-05-21 09:16:47.261265','2023-11-23 16:15:51.000000'),(3,'FREE_BUSINESS_SINGLE_WEEKLY_DEAL_COST',18,'2024-08-14 10:42:17.974873','2023-11-23 16:17:08.000000'),(5,'FREE_MEMBER_SINGLE_CLASSIFIED_COST',0,'2024-06-06 17:36:29.607809','2023-11-23 16:23:00.000000'),(6,'SINGLE_LOCATION_COST',18,'2024-05-21 09:19:02.748973','2023-04-18 10:36:54.000000');
/*!40000 ALTER TABLE `account_productprice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_restaurantmenu`
--

DROP TABLE IF EXISTS `account_restaurantmenu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_restaurantmenu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `menu` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_restaurantmenu_user_id_c38d4d1a_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_restaurantmenu`
--

LOCK TABLES `account_restaurantmenu` WRITE;
/*!40000 ALTER TABLE `account_restaurantmenu` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_restaurantmenu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_revenue`
--

DROP TABLE IF EXISTS `account_revenue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_revenue` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `amount` double NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `payment_detail_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `account_revenue_payment_detail_id_a8477d9e_fk_account_p` (`payment_detail_id`),
  KEY `account_revenue_user_id_220429d7_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `account_revenue_payment_detail_id_a8477d9e_fk_account_p` FOREIGN KEY (`payment_detail_id`) REFERENCES `account_paymentdetail` (`id`),
  CONSTRAINT `account_revenue_user_id_220429d7_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_revenue`
--

LOCK TABLES `account_revenue` WRITE;
/*!40000 ALTER TABLE `account_revenue` DISABLE KEYS */;
INSERT INTO `account_revenue` VALUES (1,0.81,'2024-04-30 16:18:48.353763',1,10),(2,8.1,'2024-05-12 17:58:31.742706',4,15),(3,1,'2024-07-22 04:12:58.709657',18,23);
/*!40000 ALTER TABLE `account_revenue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_review`
--

DROP TABLE IF EXISTS `account_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_review` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `rating` double NOT NULL,
  `comment` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `reviewed_by_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_review_reviewed_by_id_1a8bb1a8_fk_account_myuser_id` (`reviewed_by_id`),
  KEY `account_review_user_id_7a6a51f1_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `account_review_reviewed_by_id_1a8bb1a8_fk_account_myuser_id` FOREIGN KEY (`reviewed_by_id`) REFERENCES `account_myuser` (`id`),
  CONSTRAINT `account_review_user_id_7a6a51f1_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_review`
--

LOCK TABLES `account_review` WRITE;
/*!40000 ALTER TABLE `account_review` DISABLE KEYS */;
INSERT INTO `account_review` VALUES (1,4,'NA','2024-04-30 16:36:50.768920',10,3),(2,5,'Beast place to learn and build your knowledge.','2024-07-23 04:59:55.720583',21,22);
/*!40000 ALTER TABLE `account_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_reviewflag`
--

DROP TABLE IF EXISTS `account_reviewflag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_reviewflag` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `reason` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `review_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_reviewflag_review_id_831a0b6e_fk_account_review_id` (`review_id`),
  KEY `account_reviewflag_user_id_34a39b2c_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `account_reviewflag_review_id_831a0b6e_fk_account_review_id` FOREIGN KEY (`review_id`) REFERENCES `account_review` (`id`),
  CONSTRAINT `account_reviewflag_user_id_34a39b2c_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_reviewflag`
--

LOCK TABLES `account_reviewflag` WRITE;
/*!40000 ALTER TABLE `account_reviewflag` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_reviewflag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_reviewmark`
--

DROP TABLE IF EXISTS `account_reviewmark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_reviewmark` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `mark_type` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `review_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_reviewmark_review_id_cfa508b9_fk_account_review_id` (`review_id`),
  KEY `account_reviewmark_user_id_148d775a_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `account_reviewmark_review_id_cfa508b9_fk_account_review_id` FOREIGN KEY (`review_id`) REFERENCES `account_review` (`id`),
  CONSTRAINT `account_reviewmark_user_id_148d775a_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_reviewmark`
--

LOCK TABLES `account_reviewmark` WRITE;
/*!40000 ALTER TABLE `account_reviewmark` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_reviewmark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_stripedetailnew`
--

DROP TABLE IF EXISTS `account_stripedetailnew`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_stripedetailnew` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `intent` varchar(200) NOT NULL,
  `payment_method` longtext DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `cancellation_reason` longtext DEFAULT NULL,
  `description` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `payment_detail_id` bigint(20) DEFAULT NULL,
  `amount` double NOT NULL,
  `currency` varchar(10) DEFAULT NULL,
  `card_mask` varchar(30) DEFAULT NULL,
  `expire_month` varchar(4) DEFAULT NULL,
  `expire_year` varchar(4) DEFAULT NULL,
  `event_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `account_stripedetailnew_user_id_4db09a81_fk_account_myuser_id` (`user_id`),
  KEY `account_stripedetail_payment_detail_id_5024c905_fk_account_p` (`payment_detail_id`),
  CONSTRAINT `account_stripedetail_payment_detail_id_5024c905_fk_account_p` FOREIGN KEY (`payment_detail_id`) REFERENCES `account_paymentdetail` (`id`),
  CONSTRAINT `account_stripedetailnew_user_id_4db09a81_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_stripedetailnew`
--

LOCK TABLES `account_stripedetailnew` WRITE;
/*!40000 ALTER TABLE `account_stripedetailnew` DISABLE KEYS */;
INSERT INTO `account_stripedetailnew` VALUES (1,'pi_3PBJM4GdqSWEbE4M0tmy8rtT','pi_3PBJM4GdqSWEbE4M0tmy8rtT','complete',NULL,'Customer:Rakesh, ID: 10','2024-04-30 16:16:32.644016',10,1,671,'ils',NULL,NULL,NULL,'payment_intent.succeeded'),(2,'pi_3PBe9kGdqSWEbE4M1fsu9Wh2',NULL,'pending',NULL,NULL,'2024-05-01 14:29:12.739299',12,2,0,NULL,NULL,NULL,NULL,NULL),(3,'pi_3PFdxiGdqSWEbE4M0tLsF7GD',NULL,'pending',NULL,NULL,'2024-05-12 15:05:18.216179',15,3,0,NULL,NULL,NULL,NULL,NULL),(4,'pi_3PFgblGdqSWEbE4M1BggUMrw','pi_3PFgblGdqSWEbE4M1BggUMrw','complete',NULL,'Customer:None, ID: 15','2024-05-12 17:54:49.761800',15,4,1800,'usd',NULL,NULL,NULL,'payment_intent.succeeded'),(5,'pi_3POGgbGdqSWEbE4M1u84m0Cw',NULL,'pending',NULL,NULL,'2024-06-05 10:03:17.770697',17,11,0,NULL,NULL,NULL,NULL,NULL),(6,'pi_3PQAUaGdqSWEbE4M0cAu5jeV','pi_3PQAUaGdqSWEbE4M0cAu5jeV','cancelled',NULL,'Customer:None, ID: 12','2024-06-10 15:50:45.107850',12,13,1800,'usd',NULL,NULL,NULL,'payment_intent.payment_failed'),(7,'pi_3PQAXQGdqSWEbE4M1qyO5AyC','pi_3PQAXQGdqSWEbE4M1qyO5AyC','cancelled',NULL,'Customer:None, ID: 12','2024-06-10 15:53:40.275136',12,14,1800,'usd',NULL,NULL,NULL,'payment_intent.payment_failed'),(8,'pi_3PfDOPGdqSWEbE4M114L96jA',NULL,'pending',NULL,NULL,'2024-07-22 03:58:33.896788',12,16,0,NULL,NULL,NULL,NULL,NULL),(9,'pi_3PfDOlGdqSWEbE4M00EtUcw9',NULL,'pending',NULL,NULL,'2024-07-22 03:58:55.493090',12,17,0,NULL,NULL,NULL,NULL,NULL),(10,'pi_3PfDZSGdqSWEbE4M03hFNu5A','pi_3PfDZSGdqSWEbE4M03hFNu5A','complete',NULL,'Customer:Stalin, ID: 23','2024-07-22 04:09:58.790110',23,18,180,'usd',NULL,NULL,NULL,'payment_intent.succeeded'),(11,'pi_3Pmi3XGdqSWEbE4M1O0GvxaB',NULL,'pending',NULL,NULL,'2024-08-11 20:08:00.144328',26,19,0,NULL,NULL,NULL,NULL,NULL),(12,'pi_3PmiFWGdqSWEbE4M14ON9VtF',NULL,'pending',NULL,NULL,'2024-08-11 20:20:22.905304',28,20,0,NULL,NULL,NULL,NULL,NULL),(13,'pi_3Pnd4gGdqSWEbE4M15YnSvkJ',NULL,'pending',NULL,NULL,'2024-08-14 09:00:58.609519',32,21,0,NULL,NULL,NULL,NULL,NULL),(14,'pi_3PneZJGdqSWEbE4M1bvKZFy7',NULL,'pending',NULL,NULL,'2024-08-14 10:36:41.449891',36,23,0,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `account_stripedetailnew` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_stripepaymentmethod`
--

DROP TABLE IF EXISTS `account_stripepaymentmethod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_stripepaymentmethod` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `payment_method` longtext DEFAULT NULL,
  `card_mask` varchar(30) DEFAULT NULL,
  `expire_month` varchar(4) DEFAULT NULL,
  `expire_year` varchar(4) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `is_default` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_stripepaymen_user_id_dee3ed16_fk_account_m` (`user_id`),
  CONSTRAINT `account_stripepaymen_user_id_dee3ed16_fk_account_m` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_stripepaymentmethod`
--

LOCK TABLES `account_stripepaymentmethod` WRITE;
/*!40000 ALTER TABLE `account_stripepaymentmethod` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_stripepaymentmethod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_temptoken`
--

DROP TABLE IF EXISTS `account_temptoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_temptoken` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_temptoken_user_id_3e8ae71f_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=123 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_temptoken`
--

LOCK TABLES `account_temptoken` WRITE;
/*!40000 ALTER TABLE `account_temptoken` DISABLE KEYS */;
INSERT INTO `account_temptoken` VALUES (3,'961a8369-184a-46d1-ba42-fdfd9b78435c','2024-04-30 16:14:53.169988',10),(9,'bb454982-c67e-4946-bbd4-69df57d9b12f','2024-05-01 11:20:14.259494',11),(28,'0d4c1a9a-abd9-44eb-901c-95a2b1261081','2024-05-08 14:23:01.444867',13),(32,'cdd6b463-996b-4e6c-b5a7-427bc32f5aa7','2024-05-09 15:12:35.486930',14),(37,'6c4a1368-2c0d-42e4-984c-8da5c2c30fd6','2024-05-12 17:54:42.638679',15),(43,'5e54d16f-c7d2-429b-a04e-ee32b9fb4b37','2024-05-16 18:00:11.976137',16),(47,'af37ea14-5813-448f-8eb2-741d652d4ff2','2024-06-05 10:03:10.307725',17),(51,'3d10528c-fbc7-4885-ae10-7498b73e9a1a','2024-06-17 14:15:09.833363',2),(54,'9a8aca01-3a47-4b03-b055-a9848690421d','2024-06-17 14:21:08.230191',18),(57,'b14a63a3-636c-438c-9f81-d653a7285c46','2024-06-26 14:50:29.623594',19),(60,'3e05fb9b-b7a8-453d-a391-8801bc868aad','2024-07-05 14:20:13.855350',20),(63,'ae30146b-35c7-4561-bfb3-a1a12a961355','2024-07-17 04:51:19.248124',21),(72,'3e4e2923-1300-4ffa-afe7-51cf978c3abb','2024-07-22 04:09:16.387961',23),(74,'715f5b2e-6b13-468f-80ca-52b6e8930b69','2024-07-23 09:58:16.221042',22),(78,'4036102f-bafa-4593-9b37-66a142d1977a','2024-07-25 08:50:50.460169',24),(82,'ef0afdfb-d728-4f08-9815-d84e7abde843','2024-07-31 17:04:38.754833',25),(83,'4e9261ae-6901-4c2b-b294-8bd7a1f96314','2024-08-03 06:32:27.941202',12),(86,'03b6dc31-9fe1-4cc0-af23-fc02ee90779e','2024-08-11 20:07:01.533572',26),(92,'325975a9-ddd3-44bf-b708-a84127f5d344','2024-08-11 20:19:08.239178',28),(93,'09f13465-19d6-49b8-bdfa-bc28d619341c','2024-08-12 15:41:23.324263',27),(96,'cbf6b7c3-2524-41c5-bb52-b7908fbdb41a','2024-08-13 07:26:58.847950',29),(105,'1efdffdf-78b1-4d94-9e86-7b9d72553a4d','2024-08-14 08:56:50.858818',31),(108,'b4978505-526d-44ff-b01e-13f8bb314bc5','2024-08-14 09:00:29.262917',32),(110,'12ef13ec-d7ac-457c-8860-d9517f2da89b','2024-08-14 09:41:06.344641',30),(113,'17589272-85c7-4b18-b42e-f4f98c7b101a','2024-08-14 09:50:41.730554',34),(117,'e33273e6-fefa-4304-af7c-cfb66db26d1b','2024-08-14 09:53:59.886652',35),(122,'2e43ac56-9281-4ad1-844c-dc82c0270894','2024-08-14 11:00:39.967699',36);
/*!40000 ALTER TABLE `account_temptoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_tranziladetail`
--

DROP TABLE IF EXISTS `account_tranziladetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_tranziladetail` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `processor_response_code` int(11) DEFAULT NULL,
  `transaction_id` int(11) DEFAULT NULL,
  `currency_code` varchar(2) DEFAULT NULL,
  `expiry_month` varchar(4) DEFAULT NULL,
  `expiry_year` varchar(4) DEFAULT NULL,
  `payment_plan` varchar(4) DEFAULT NULL,
  `credit_card_owner_id` varchar(100) DEFAULT NULL,
  `token` varchar(100) DEFAULT NULL,
  `card_last_four` varchar(4) DEFAULT NULL,
  `card_mask` varchar(30) DEFAULT NULL,
  `card_locality` varchar(20) DEFAULT NULL,
  `amount` double NOT NULL,
  `txn_type` varchar(10) DEFAULT NULL,
  `tranmode` varchar(10) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `payment_detail_id` bigint(20) DEFAULT NULL,
  `error_code` varchar(10) DEFAULT NULL,
  `error_info` longtext DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `account_tranziladeta_payment_detail_id_069c2782_fk_account_p` (`payment_detail_id`),
  KEY `account_tranziladetail_user_id_3b1b1b45_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `account_tranziladeta_payment_detail_id_069c2782_fk_account_p` FOREIGN KEY (`payment_detail_id`) REFERENCES `account_paymentdetail` (`id`),
  CONSTRAINT `account_tranziladetail_user_id_3b1b1b45_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_tranziladetail`
--

LOCK TABLES `account_tranziladetail` WRITE;
/*!40000 ALTER TABLE `account_tranziladetail` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_tranziladetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_tranzilatoken`
--

DROP TABLE IF EXISTS `account_tranzilatoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_tranzilatoken` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` varchar(100) NOT NULL,
  `expire_month` varchar(4) NOT NULL,
  `expire_year` varchar(4) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `card_mask` varchar(30) DEFAULT NULL,
  `is_default` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_tranzilatoken_user_id_bcb1d862` (`user_id`),
  CONSTRAINT `account_tranzilatoken_user_id_bcb1d862_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_tranzilatoken`
--

LOCK TABLES `account_tranzilatoken` WRITE;
/*!40000 ALTER TABLE `account_tranzilatoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_tranzilatoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_userlocation`
--

DROP TABLE IF EXISTS `account_userlocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_userlocation` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `is_primary` tinyint(1) NOT NULL,
  `location_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `account_userlocation_location_id_999ae1cb_fk_account_location_id` (`location_id`),
  KEY `account_userlocation_user_id_9d022ad6_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `account_userlocation_location_id_999ae1cb_fk_account_location_id` FOREIGN KEY (`location_id`) REFERENCES `account_location` (`id`),
  CONSTRAINT `account_userlocation_user_id_9d022ad6_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_userlocation`
--

LOCK TABLES `account_userlocation` WRITE;
/*!40000 ALTER TABLE `account_userlocation` DISABLE KEYS */;
INSERT INTO `account_userlocation` VALUES (1,1,1,10),(2,1,2,11),(3,1,3,14),(4,1,4,15),(5,1,5,16),(6,1,6,18),(7,1,7,21),(8,1,8,22),(9,1,9,23),(10,1,10,24),(11,1,13,30),(12,1,14,35);
/*!40000 ALTER TABLE `account_userlocation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_usertypecategory`
--

DROP TABLE IF EXISTS `account_usertypecategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_usertypecategory` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `user_type` varchar(20) NOT NULL,
  `name_ar` varchar(50) DEFAULT NULL,
  `name_de` varchar(50) DEFAULT NULL,
  `name_es` varchar(50) DEFAULT NULL,
  `name_fr` varchar(50) DEFAULT NULL,
  `name_he` varchar(50) DEFAULT NULL,
  `name_pt` varchar(50) DEFAULT NULL,
  `name_ru` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_usertypecategory`
--

LOCK TABLES `account_usertypecategory` WRITE;
/*!40000 ALTER TABLE `account_usertypecategory` DISABLE KEYS */;
INSERT INTO `account_usertypecategory` VALUES (1,'Museums /Cultural Centres','ngo','المتاحف /المراكز الثقافية','Museen /Kulturzentren','Museos /centros culturales','Musées / centres culturels','מוזיאונים /מרכזי תרבות','Museus /centros culturais','Музеи /культурные центры'),(2,'Environment / Climate','ngo','البيئة / المناخ','Umwelt / Klima','Medio ambiente / clima','Environnement / climat','סביבה / אקלים','Meio ambiente / clima','Окружающая среда / климат'),(3,'Health / Medical','ngo','الصحة / الطبي','Gesundheit / medizinisch','Salud y Medicina','Santé / médical','בריאות / רפואה','Saúde / médico','Здоровье / медицинское'),(4,'Education','ngo','تعليم','Ausbildung','Educación','Éducation','חינוך','Educação','Образование'),(5,'Disabilities','ngo','الإعاقات','Behinderungen','Discapacidad','Handicapées','מוגבלות','Deficiências','Инвалидность'),(6,'Religion Institutions','ngo','مؤسسات الدين','Religionsinstitutionen','Instituciones religiosas','Institutions de religion','מוסדות דת','Instituições religiosas','Религиозные учреждения'),(7,'Sports','ngo','رياضات','Sport','Deportes','Des sports','ספורט','Esportes','Виды спорта'),(8,'Woman','ngo','امرأة','Frau','Mujer','Femme','אִשָׁה','Mulher','Женщина'),(9,'Children','ngo','أطفال','Kinder','Niños','Enfants','יְלָדִים','Crianças','Дети'),(10,'Community Based','ngo','المجتمع على أساس','Gemeinschaftsbasiert','Basado en la comunidad','Basé sur la communauté','מבוסס על הקהילה','Baseada na comunidade','Сообщество'),(11,'Poverty / Hunger','ngo','الفقر / الجوع','Armut / Hunger','Pobreza / hambre','Pauvreté / faim','עוני / רעב','Pobreza / fome','Бедность / голод'),(12,'Animals','ngo','الحيوانات','Tiere','Animales','Animaux','בעלי חיים','Animais','Животные'),(13,'Innovation','ngo','ابتكار','Innovation','Innovación','Innovation','חדשנות','Inovação','Инновации'),(14,'Empowerment','ngo','التمكين','Ermächtigung','Empoderamiento','Autonomisation','העצמה','Fortalecimento','Расширение прав и возможностей'),(15,'City Wide Programs','ngo','برامج المدينة واسعة','Stadtweite Programme','Programas de la ciudad','Programmes à l\'échelle de la ville','תוכניות רחבות עירוניות','Programas da cidade','Городские программы'),(16,'Israeli Orgs','ngo','orgs الإسرائيلية','Israelische Orgs','Orgs israelíes','Orgs israéliens','אורגים ישראליים','Orgs israelenses','Израильские организации'),(17,'International Orgs','ngo','Orgs الدولية','Internationale Orgs','Orgs internacionales','Orgs internationaux','אורגים בינלאומיים','Orgs internacionais','Международные организации'),(18,'IDF','ngo','IDF','Idf','IDF','FDI','IDF','IDF','ИДФ'),(19,'Antisemitism','ngo','معاداة السامية','Antisemitismus','Antisemitismo','Antisémitisme','אנטישמיות','Anti -semitismo','Антисемитизм');
/*!40000 ALTER TABLE `account_usertypecategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_vendor`
--

DROP TABLE IF EXISTS `account_vendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_vendor` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `phone` varchar(17) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_vendor`
--

LOCK TABLES `account_vendor` WRITE;
/*!40000 ALTER TABLE `account_vendor` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_vendor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_vendorexpense`
--

DROP TABLE IF EXISTS `account_vendorexpense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_vendorexpense` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `invoice_number` varchar(100) NOT NULL,
  `file` varchar(100) NOT NULL,
  `vendor_id` bigint(20) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `amount` double NOT NULL,
  `date` date DEFAULT NULL,
  `remarks` longtext DEFAULT NULL,
  `paid` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_vendorexpense_vendor_id_89d01871_fk_account_vendor_id` (`vendor_id`),
  CONSTRAINT `account_vendorexpense_vendor_id_89d01871_fk_account_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `account_vendor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_vendorexpense`
--

LOCK TABLES `account_vendorexpense` WRITE;
/*!40000 ALTER TABLE `account_vendorexpense` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_vendorexpense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `article_news`
--

DROP TABLE IF EXISTS `article_news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article_news` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(256) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(100) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  `delete_requested` tinyint(1) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_popular` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `article_news_category_id_28e45dec_fk_account_businesscategory_id` (`category_id`),
  KEY `article_news_user_id_9f020dde_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `article_news_category_id_28e45dec_fk_account_businesscategory_id` FOREIGN KEY (`category_id`) REFERENCES `account_businesscategory` (`id`),
  CONSTRAINT `article_news_user_id_9f020dde_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article_news`
--

LOCK TABLES `article_news` WRITE;
/*!40000 ALTER TABLE `article_news` DISABLE KEYS */;
/*!40000 ALTER TABLE `article_news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=281 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add blacklisted token',6,'add_blacklistedtoken'),(22,'Can change blacklisted token',6,'change_blacklistedtoken'),(23,'Can delete blacklisted token',6,'delete_blacklistedtoken'),(24,'Can view blacklisted token',6,'view_blacklistedtoken'),(25,'Can add outstanding token',7,'add_outstandingtoken'),(26,'Can change outstanding token',7,'change_outstandingtoken'),(27,'Can delete outstanding token',7,'delete_outstandingtoken'),(28,'Can view outstanding token',7,'view_outstandingtoken'),(29,'Can add my user',8,'add_myuser'),(30,'Can change my user',8,'change_myuser'),(31,'Can delete my user',8,'delete_myuser'),(32,'Can view my user',8,'view_myuser'),(33,'Can add review',9,'add_review'),(34,'Can change review',9,'change_review'),(35,'Can delete review',9,'delete_review'),(36,'Can view review',9,'view_review'),(37,'Can add location',10,'add_location'),(38,'Can change location',10,'change_location'),(39,'Can delete location',10,'delete_location'),(40,'Can view location',10,'view_location'),(41,'Can add family member',11,'add_familymember'),(42,'Can change family member',11,'change_familymember'),(43,'Can delete family member',11,'delete_familymember'),(44,'Can view family member',11,'view_familymember'),(45,'Can add delivery partner',12,'add_deliverypartner'),(46,'Can change delivery partner',12,'change_deliverypartner'),(47,'Can delete delivery partner',12,'delete_deliverypartner'),(48,'Can view delivery partner',12,'view_deliverypartner'),(49,'Can add code',13,'add_code'),(50,'Can change code',13,'change_code'),(51,'Can delete code',13,'delete_code'),(52,'Can view code',13,'view_code'),(53,'Can add country',14,'add_country'),(54,'Can change country',14,'change_country'),(55,'Can delete country',14,'delete_country'),(56,'Can view country',14,'view_country'),(57,'Can add plan',15,'add_plan'),(58,'Can change plan',15,'change_plan'),(59,'Can delete plan',15,'delete_plan'),(60,'Can view plan',15,'view_plan'),(61,'Can add plan feature',16,'add_planfeature'),(62,'Can change plan feature',16,'change_planfeature'),(63,'Can delete plan feature',16,'delete_planfeature'),(64,'Can view plan feature',16,'view_planfeature'),(65,'Can add temp token',17,'add_temptoken'),(66,'Can change temp token',17,'change_temptoken'),(67,'Can delete temp token',17,'delete_temptoken'),(68,'Can view temp token',17,'view_temptoken'),(69,'Can add restaurant menu',18,'add_restaurantmenu'),(70,'Can change restaurant menu',18,'change_restaurantmenu'),(71,'Can delete restaurant menu',18,'delete_restaurantmenu'),(72,'Can view restaurant menu',18,'view_restaurantmenu'),(73,'Can add category',19,'add_businesscategory'),(74,'Can change category',19,'change_businesscategory'),(75,'Can delete category',19,'delete_businesscategory'),(76,'Can view category',19,'view_businesscategory'),(77,'Can add ngo video',20,'add_ngovideo'),(78,'Can change ngo video',20,'change_ngovideo'),(79,'Can delete ngo video',20,'delete_ngovideo'),(80,'Can view ngo video',20,'view_ngovideo'),(81,'Can add currency',21,'add_currency'),(82,'Can change currency',21,'change_currency'),(83,'Can delete currency',21,'delete_currency'),(84,'Can view currency',21,'view_currency'),(85,'Can add currency exchange rate',22,'add_currencyexchangerate'),(86,'Can change currency exchange rate',22,'change_currencyexchangerate'),(87,'Can delete currency exchange rate',22,'delete_currencyexchangerate'),(88,'Can view currency exchange rate',22,'view_currencyexchangerate'),(89,'Can add ngo referal token',23,'add_ngoreferaltoken'),(90,'Can change ngo referal token',23,'change_ngoreferaltoken'),(91,'Can delete ngo referal token',23,'delete_ngoreferaltoken'),(92,'Can view ngo referal token',23,'view_ngoreferaltoken'),(93,'Can add flagged',24,'add_flagged'),(94,'Can change flagged',24,'change_flagged'),(95,'Can delete flagged',24,'delete_flagged'),(96,'Can view flagged',24,'view_flagged'),(97,'Can add activity log',25,'add_activitylog'),(98,'Can change activity log',25,'change_activitylog'),(99,'Can delete activity log',25,'delete_activitylog'),(100,'Can view activity log',25,'view_activitylog'),(101,'Can add tranzila token',26,'add_tranzilatoken'),(102,'Can change tranzila token',26,'change_tranzilatoken'),(103,'Can delete tranzila token',26,'delete_tranzilatoken'),(104,'Can view tranzila token',26,'view_tranzilatoken'),(105,'Can add stripe detail new',27,'add_stripedetailnew'),(106,'Can change stripe detail new',27,'change_stripedetailnew'),(107,'Can delete stripe detail new',27,'delete_stripedetailnew'),(108,'Can view stripe detail new',27,'view_stripedetailnew'),(109,'Can add payment detail',28,'add_paymentdetail'),(110,'Can change payment detail',28,'change_paymentdetail'),(111,'Can delete payment detail',28,'delete_paymentdetail'),(112,'Can view payment detail',28,'view_paymentdetail'),(113,'Can add tranzila detail',29,'add_tranziladetail'),(114,'Can change tranzila detail',29,'change_tranziladetail'),(115,'Can delete tranzila detail',29,'delete_tranziladetail'),(116,'Can view tranzila detail',29,'view_tranziladetail'),(117,'Can add review mark',30,'add_reviewmark'),(118,'Can change review mark',30,'change_reviewmark'),(119,'Can delete review mark',30,'delete_reviewmark'),(120,'Can view review mark',30,'view_reviewmark'),(121,'Can add review flag',31,'add_reviewflag'),(122,'Can change review flag',31,'change_reviewflag'),(123,'Can delete review flag',31,'delete_reviewflag'),(124,'Can view review flag',31,'view_reviewflag'),(125,'Can add user_type_category',32,'add_usertypecategory'),(126,'Can change user_type_category',32,'change_usertypecategory'),(127,'Can delete user_type_category',32,'delete_usertypecategory'),(128,'Can view user_type_category',32,'view_usertypecategory'),(129,'Can add ngo payout',33,'add_ngopayout'),(130,'Can change ngo payout',33,'change_ngopayout'),(131,'Can delete ngo payout',33,'delete_ngopayout'),(132,'Can view ngo payout',33,'view_ngopayout'),(133,'Can add vendor',34,'add_vendor'),(134,'Can change vendor',34,'change_vendor'),(135,'Can delete vendor',34,'delete_vendor'),(136,'Can view vendor',34,'view_vendor'),(137,'Can add vendor expense',35,'add_vendorexpense'),(138,'Can change vendor expense',35,'change_vendorexpense'),(139,'Can delete vendor expense',35,'delete_vendorexpense'),(140,'Can view vendor expense',35,'view_vendorexpense'),(141,'Can add oneline user',36,'add_onelineuser'),(142,'Can change oneline user',36,'change_onelineuser'),(143,'Can delete oneline user',36,'delete_onelineuser'),(144,'Can view oneline user',36,'view_onelineuser'),(145,'Can add revenue',37,'add_revenue'),(146,'Can change revenue',37,'change_revenue'),(147,'Can delete revenue',37,'delete_revenue'),(148,'Can view revenue',37,'view_revenue'),(149,'Can add user location',38,'add_userlocation'),(150,'Can change user location',38,'change_userlocation'),(151,'Can delete user location',38,'delete_userlocation'),(152,'Can view user location',38,'view_userlocation'),(153,'Can add product price',39,'add_productprice'),(154,'Can change product price',39,'change_productprice'),(155,'Can delete product price',39,'delete_productprice'),(156,'Can view product price',39,'view_productprice'),(157,'Can add stripe payment method',40,'add_stripepaymentmethod'),(158,'Can change stripe payment method',40,'change_stripepaymentmethod'),(159,'Can delete stripe payment method',40,'delete_stripepaymentmethod'),(160,'Can view stripe payment method',40,'view_stripepaymentmethod'),(161,'Can add deal',41,'add_deal'),(162,'Can change deal',41,'change_deal'),(163,'Can delete deal',41,'delete_deal'),(164,'Can view deal',41,'view_deal'),(165,'Can add order',42,'add_order'),(166,'Can change order',42,'change_order'),(167,'Can delete order',42,'delete_order'),(168,'Can view order',42,'view_order'),(169,'Can add payment',43,'add_payment'),(170,'Can change payment',43,'change_payment'),(171,'Can delete payment',43,'delete_payment'),(172,'Can view payment',43,'view_payment'),(173,'Can add deal image',44,'add_dealimage'),(174,'Can change deal image',44,'change_dealimage'),(175,'Can delete deal image',44,'delete_dealimage'),(176,'Can view deal image',44,'view_dealimage'),(177,'Can add property details',45,'add_propertydetails'),(178,'Can change property details',45,'change_propertydetails'),(179,'Can delete property details',45,'delete_propertydetails'),(180,'Can view property details',45,'view_propertydetails'),(181,'Can add review',46,'add_review'),(182,'Can change review',46,'change_review'),(183,'Can delete review',46,'delete_review'),(184,'Can view review',46,'view_review'),(185,'Can add deal redeem',47,'add_dealredeem'),(186,'Can change deal redeem',47,'change_dealredeem'),(187,'Can delete deal redeem',47,'delete_dealredeem'),(188,'Can view deal redeem',47,'view_dealredeem'),(189,'Can add flagged',48,'add_flagged'),(190,'Can change flagged',48,'change_flagged'),(191,'Can delete flagged',48,'delete_flagged'),(192,'Can view flagged',48,'view_flagged'),(193,'Can add review mark',49,'add_reviewmark'),(194,'Can change review mark',49,'change_reviewmark'),(195,'Can delete review mark',49,'delete_reviewmark'),(196,'Can view review mark',49,'view_reviewmark'),(197,'Can add review flag',50,'add_reviewflag'),(198,'Can change review flag',50,'change_reviewflag'),(199,'Can delete review flag',50,'delete_reviewflag'),(200,'Can view review flag',50,'view_reviewflag'),(201,'Can add deal click',51,'add_dealclick'),(202,'Can change deal click',51,'change_dealclick'),(203,'Can delete deal click',51,'delete_dealclick'),(204,'Can view deal click',51,'view_dealclick'),(205,'Can add category',52,'add_category'),(206,'Can change category',52,'change_category'),(207,'Can delete category',52,'delete_category'),(208,'Can view category',52,'view_category'),(209,'Can add news',53,'add_news'),(210,'Can change news',53,'change_news'),(211,'Can delete news',53,'delete_news'),(212,'Can view news',53,'view_news'),(213,'Can add job',54,'add_job'),(214,'Can change job',54,'change_job'),(215,'Can delete job',54,'delete_job'),(216,'Can view job',54,'view_job'),(217,'Can add resume',55,'add_resume'),(218,'Can change resume',55,'change_resume'),(219,'Can delete resume',55,'delete_resume'),(220,'Can view resume',55,'view_resume'),(221,'Can add job click',56,'add_jobclick'),(222,'Can change job click',56,'change_jobclick'),(223,'Can delete job click',56,'delete_jobclick'),(224,'Can view job click',56,'view_jobclick'),(225,'Can add application',57,'add_application'),(226,'Can change application',57,'change_application'),(227,'Can delete application',57,'delete_application'),(228,'Can view application',57,'view_application'),(229,'Can add classified',58,'add_classified'),(230,'Can change classified',58,'change_classified'),(231,'Can delete classified',58,'delete_classified'),(232,'Can view classified',58,'view_classified'),(233,'Can add classified image',59,'add_classifiedimage'),(234,'Can change classified image',59,'change_classifiedimage'),(235,'Can delete classified image',59,'delete_classifiedimage'),(236,'Can view classified image',59,'view_classifiedimage'),(237,'Can add flagged',60,'add_flagged'),(238,'Can change flagged',60,'change_flagged'),(239,'Can delete flagged',60,'delete_flagged'),(240,'Can view flagged',60,'view_flagged'),(241,'Can add classified category',61,'add_classifiedcategory'),(242,'Can change classified category',61,'change_classifiedcategory'),(243,'Can delete classified category',61,'delete_classifiedcategory'),(244,'Can view classified category',61,'view_classifiedcategory'),(245,'Can add classified click',62,'add_classifiedclick'),(246,'Can change classified click',62,'change_classifiedclick'),(247,'Can delete classified click',62,'delete_classifiedclick'),(248,'Can view classified click',62,'view_classifiedclick'),(249,'Can add faq',63,'add_faq'),(250,'Can change faq',63,'change_faq'),(251,'Can delete faq',63,'delete_faq'),(252,'Can view faq',63,'view_faq'),(253,'Can add about',64,'add_about'),(254,'Can change about',64,'change_about'),(255,'Can delete about',64,'delete_about'),(256,'Can view about',64,'view_about'),(257,'Can add terms and condition',65,'add_termsandcondition'),(258,'Can change terms and condition',65,'change_termsandcondition'),(259,'Can delete terms and condition',65,'delete_termsandcondition'),(260,'Can view terms and condition',65,'view_termsandcondition'),(261,'Can add about journey',66,'add_aboutjourney'),(262,'Can change about journey',66,'change_aboutjourney'),(263,'Can delete about journey',66,'delete_aboutjourney'),(264,'Can view about journey',66,'view_aboutjourney'),(265,'Can add about team',67,'add_aboutteam'),(266,'Can change about team',67,'change_aboutteam'),(267,'Can delete about team',67,'delete_aboutteam'),(268,'Can view about team',67,'view_aboutteam'),(269,'Can add privacy policy',68,'add_privacypolicy'),(270,'Can change privacy policy',68,'change_privacypolicy'),(271,'Can delete privacy policy',68,'delete_privacypolicy'),(272,'Can view privacy policy',68,'view_privacypolicy'),(273,'Can add contact us',69,'add_contactus'),(274,'Can change contact us',69,'change_contactus'),(275,'Can delete contact us',69,'delete_contactus'),(276,'Can view contact us',69,'view_contactus'),(277,'Can add news',70,'add_news'),(278,'Can change news',70,'change_news'),(279,'Can delete news',70,'delete_news'),(280,'Can view news',70,'view_news');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blogs_category`
--

DROP TABLE IF EXISTS `blogs_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogs_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogs_category`
--

LOCK TABLES `blogs_category` WRITE;
/*!40000 ALTER TABLE `blogs_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `blogs_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blogs_news`
--

DROP TABLE IF EXISTS `blogs_news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogs_news` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `feature_picture` varchar(100) NOT NULL,
  `status` varchar(10) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blogs_news_user_id_0813a158_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `blogs_news_user_id_0813a158_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogs_news`
--

LOCK TABLES `blogs_news` WRITE;
/*!40000 ALTER TABLE `blogs_news` DISABLE KEYS */;
/*!40000 ALTER TABLE `blogs_news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classifieds_classified`
--

DROP TABLE IF EXISTS `classifieds_classified`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classifieds_classified` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `price` double NOT NULL,
  `contact_phone` varchar(17) DEFAULT NULL,
  `contact_email` varchar(254) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `location_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  `expiry_date` date NOT NULL,
  `price_type` varchar(20) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `pinned` tinyint(1) NOT NULL,
  `paid` tinyint(1) NOT NULL,
  `category_id` bigint(20) DEFAULT NULL,
  `product_condition` varchar(3) NOT NULL,
  `ngo_fee` double NOT NULL,
  `shuk_fee` double NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `classifieds_classifi_location_id_f80b6513_fk_account_l` (`location_id`),
  KEY `classifieds_classified_user_id_ee77f436_fk_account_myuser_id` (`user_id`),
  KEY `classifieds_classifi_category_id_f1a11403_fk_classifie` (`category_id`),
  CONSTRAINT `classifieds_classifi_category_id_f1a11403_fk_classifie` FOREIGN KEY (`category_id`) REFERENCES `classifieds_classifiedcategory` (`id`),
  CONSTRAINT `classifieds_classifi_location_id_f80b6513_fk_account_l` FOREIGN KEY (`location_id`) REFERENCES `account_location` (`id`),
  CONSTRAINT `classifieds_classified_user_id_ee77f436_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classifieds_classified`
--

LOCK TABLES `classifieds_classified` WRITE;
/*!40000 ALTER TABLE `classifieds_classified` DISABLE KEYS */;
INSERT INTO `classifieds_classified` VALUES (1,'Test Deal','Testing',12,'+918248183180','admininfo@v2wss.com','2024-08-13 09:12:37.779385','2024-08-13 09:12:37.780783',11,21,'2028-08-14','monthly',1,1,0,5,'new',0,0,0),(2,'DealOfMovies','MovieTicketBuZZ',8,'+918248183181','arunasalam.g@v2wss.com','2024-08-14 05:03:23.053824','2024-08-14 05:03:23.055169',12,21,'2024-08-16','monthly',1,1,0,8,'new',0,0,0);
/*!40000 ALTER TABLE `classifieds_classified` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classifieds_classifiedcategory`
--

DROP TABLE IF EXISTS `classifieds_classifiedcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classifieds_classifiedcategory` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `name_ar` varchar(50) DEFAULT NULL,
  `name_de` varchar(50) DEFAULT NULL,
  `name_es` varchar(50) DEFAULT NULL,
  `name_fr` varchar(50) DEFAULT NULL,
  `name_he` varchar(50) DEFAULT NULL,
  `name_pt` varchar(50) DEFAULT NULL,
  `name_ru` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classifieds_classifiedcategory`
--

LOCK TABLES `classifieds_classifiedcategory` WRITE;
/*!40000 ALTER TABLE `classifieds_classifiedcategory` DISABLE KEYS */;
INSERT INTO `classifieds_classifiedcategory` VALUES (1,'Vehicles /Transportation','المركبات /النقل','Fahrzeuge /Transport','Vehículos /transporte','Véhicules / transport','כלי רכב /הובלה','Veículos /transporte','Транспортные средства /транспорт'),(2,'Roommate / Room','المركبات /النقل','Mitbewohner / Zimmer','Compañero de cuarto / habitación','Colocataire / chambre','שותף לחדר / חדר','Companheiro de quarto / quarto','Сосед по комнате / комната'),(3,'Clothing','رفيق الغرفة / الغرفة','Kleidung','Ropa','Vêtements','הַלבָּשָׁה','Roupas','Одежда'),(4,'Furniture','ملابس','Möbel','Muebles','Meubles','רְהִיטִים','Mobília','Мебель'),(5,'Electronics','أثاث','Elektronik','Electrónica','Électronique','מכשירי חשמל','Eletrônicos','Электроника'),(6,'Antiques & Collectibles','الإلكترونيات','Antiquitäten & Sammlerstücke','Antigüedades y coleccionables','Antiquités et objets de collection','עתיקות ואספנות','Antiguidades e colecionáveis','Антиквариат и предметы коллекционирования'),(7,'Appliances','التحف والمقتنيات','Haushaltsgeräte','Accesorios','appareils électroménagers','מכשירים','Aparelhos','Техника'),(8,'Books, Films & Music','الأجهزة','Bücher, Filme und Musik','Libros, películas y música','Livres, films et musique','ספרים, סרטים ומוזיקה','Livros, filmes e música','Книги, фильмы и музыка'),(9,'Tools','الكتب والأفلام والموسيقى','Werkzeuge','Herramientas','Outils','כלים','Ferramentas','Инструменты'),(10,'FREE','أدوات','FREI','GRATIS','GRATUIT','חינם','LIVRE','БЕСПЛАТНО'),(11,'Heath & Beauty','حر','Heath & Beauty','Heath & Beauty','Heath et beauté','הית ויופי','Heath & Beauty','Хит и красота'),(12,'Jewellery & Watches','هيث والجمال','Schmuck & Uhren','Joyas y relojes','Bijoux et montres','תכשיטים ושעונים','Jóias e relógios','Ювелирные изделия и часы'),(13,'Home Goods & Decor','مجوهرات وساعات','Haushaltswaren und Dekoration','Artículos para el hogar y decoración','Goods à domicile et décoration','מוצרי בית ועיצוב','Artigos e decoração domésticos','Домашние товары и декор'),(14,'Luggage & Bags','السلع المنزلية والديكور','Gepäck und Taschen','Equipaje y bolsos','Valises et sacs','מזוודות ותיקים','Bagagem e bolsas','Багаж и сумки'),(15,'Musical Instruments','أمتعة و حقائب','Musikinstrumente','Instrumentos musicales','Instruments de musique','כלי נגינה','Instrumentos musicais','Музыкальные инструменты'),(16,'Patio & Garden','الات موسيقية','Terrasse & Garten','Patio y jardín','Patio et jardin','פטיו וגן','Pátio e jardim','Патио и сад'),(17,'Pets & Supplies','الفناء والحديقة','Haustiere & Vorräte','Mascotas y suministros','Animaux et fournitures','חיות מחמד ואספקה','Animais de estimação e suprimentos','Домашние животные и расходные материалы');
/*!40000 ALTER TABLE `classifieds_classifiedcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classifieds_classifiedclick`
--

DROP TABLE IF EXISTS `classifieds_classifiedclick`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classifieds_classifiedclick` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `classified_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `classifieds_classifi_user_id_a6b0a37b_fk_account_m` (`user_id`),
  KEY `classifieds_classifi_classified_id_1acc4116_fk_classifie` (`classified_id`),
  CONSTRAINT `classifieds_classifi_classified_id_1acc4116_fk_classifie` FOREIGN KEY (`classified_id`) REFERENCES `classifieds_classified` (`id`),
  CONSTRAINT `classifieds_classifi_user_id_a6b0a37b_fk_account_m` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classifieds_classifiedclick`
--

LOCK TABLES `classifieds_classifiedclick` WRITE;
/*!40000 ALTER TABLE `classifieds_classifiedclick` DISABLE KEYS */;
/*!40000 ALTER TABLE `classifieds_classifiedclick` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classifieds_classifiedimage`
--

DROP TABLE IF EXISTS `classifieds_classifiedimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classifieds_classifiedimage` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `classified_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `classifieds_classifi_classified_id_06587615_fk_classifie` (`classified_id`),
  CONSTRAINT `classifieds_classifi_classified_id_06587615_fk_classifie` FOREIGN KEY (`classified_id`) REFERENCES `classifieds_classified` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classifieds_classifiedimage`
--

LOCK TABLES `classifieds_classifiedimage` WRITE;
/*!40000 ALTER TABLE `classifieds_classifiedimage` DISABLE KEYS */;
INSERT INTO `classifieds_classifiedimage` VALUES (1,'classified_images/user_21/eagle_logo.jpg','2024-08-13 09:12:37.784110',1),(2,'classified_images/user_21/photo1.png','2024-08-14 05:03:23.060066',2);
/*!40000 ALTER TABLE `classifieds_classifiedimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classifieds_flagged`
--

DROP TABLE IF EXISTS `classifieds_flagged`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classifieds_flagged` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `reason` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `classified_id` bigint(20) NOT NULL,
  `flagged_by_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `classifieds_flagged_classified_id_3e2712bc_fk_classifie` (`classified_id`),
  KEY `classifieds_flagged_flagged_by_id_d026e075_fk_account_myuser_id` (`flagged_by_id`),
  CONSTRAINT `classifieds_flagged_classified_id_3e2712bc_fk_classifie` FOREIGN KEY (`classified_id`) REFERENCES `classifieds_classified` (`id`),
  CONSTRAINT `classifieds_flagged_flagged_by_id_d026e075_fk_account_myuser_id` FOREIGN KEY (`flagged_by_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classifieds_flagged`
--

LOCK TABLES `classifieds_flagged` WRITE;
/*!40000 ALTER TABLE `classifieds_flagged` DISABLE KEYS */;
/*!40000 ALTER TABLE `classifieds_flagged` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `content_about`
--

DROP TABLE IF EXISTS `content_about`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `content_about` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `heading` varchar(100) DEFAULT NULL,
  `sub_description` longtext DEFAULT NULL,
  `sub_heading` varchar(100) DEFAULT NULL,
  `team_description` longtext DEFAULT NULL,
  `team_heading` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content_about`
--

LOCK TABLES `content_about` WRITE;
/*!40000 ALTER TABLE `content_about` DISABLE KEYS */;
/*!40000 ALTER TABLE `content_about` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `content_aboutjourney`
--

DROP TABLE IF EXISTS `content_aboutjourney`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `content_aboutjourney` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `icon` varchar(256) NOT NULL,
  `counter` varchar(10) NOT NULL,
  `title` varchar(20) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content_aboutjourney`
--

LOCK TABLES `content_aboutjourney` WRITE;
/*!40000 ALTER TABLE `content_aboutjourney` DISABLE KEYS */;
/*!40000 ALTER TABLE `content_aboutjourney` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `content_aboutteam`
--

DROP TABLE IF EXISTS `content_aboutteam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `content_aboutteam` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(256) NOT NULL,
  `name` varchar(30) NOT NULL,
  `designation` varchar(30) NOT NULL,
  `facebook_link` varchar(200) NOT NULL,
  `twitter_link` varchar(200) NOT NULL,
  `instagram_link` varchar(200) NOT NULL,
  `linkedin_link` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content_aboutteam`
--

LOCK TABLES `content_aboutteam` WRITE;
/*!40000 ALTER TABLE `content_aboutteam` DISABLE KEYS */;
/*!40000 ALTER TABLE `content_aboutteam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `content_contactus`
--

DROP TABLE IF EXISTS `content_contactus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `content_contactus` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(17) NOT NULL,
  `message` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content_contactus`
--

LOCK TABLES `content_contactus` WRITE;
/*!40000 ALTER TABLE `content_contactus` DISABLE KEYS */;
/*!40000 ALTER TABLE `content_contactus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `content_faq`
--

DROP TABLE IF EXISTS `content_faq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `content_faq` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `question` varchar(300) NOT NULL,
  `answer` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content_faq`
--

LOCK TABLES `content_faq` WRITE;
/*!40000 ALTER TABLE `content_faq` DISABLE KEYS */;
INSERT INTO `content_faq` VALUES (1,'How do you open an account?','Under Login Tab press \"Sign Up & Support Tab\"','2024-05-14 16:46:35.030903'),(2,'What do you do if you enter the wrong email address?','Go to your profile, press edit, change email address, press save.','2024-05-14 16:49:15.078811'),(3,'How do you know that your account has been activated?','You will receive a verification code via the email address & phone number that you entered upon registering your account.','2024-05-14 16:52:02.833395'),(4,'How do you cancel / delete an Account?','Go to setting, press Account tab, press the Delete Account button.','2024-05-14 16:57:52.818405'),(5,'What is the difference between a Free Account User & a Hamsa Account?','Free Account Members qualify for lesser Coupon Savings; and are required to pay a $1.80 in order to place a Classified Ad;  Most importantly, Free Account Users are not able to help support our Non- Profit Organization partners.','2024-05-14 17:23:24.368767'),(6,'How can you pick which Non-Profit you would like to support?','When you register for a Free or a Hamsa Account you will see a tab on the right that\r\n Opens to a pulldown menu that will allow you to choose a Non-Profit to support.','2024-05-14 17:25:42.946125'),(7,'How can you see how much support a Non-Profit Organization has received?','By clicking on the name of any participating Non-Profit Organization listed on the\r\n “Shukdeals” platform, Users can view in real-time the financial support the particular\r\n  Non-Profit Organization has received.','2024-05-14 17:28:00.256942'),(8,'How can you add a family member to your account?','Sign onto your account; go to the “Profile Section” on the upper right hand side of your 	  	   	screen; click on the tab on the right hand side saying “Add Family Member”,,,','2024-05-14 17:29:12.980233'),(9,'How can you find a participating business in your area?','Choose location on top menu bar; enter Category Desired in search engine;','2024-05-14 17:30:35.546661'),(10,'How can you see the value of a coupon in your currency?','Click on the Currency Symbol on the Top Left hand side of the Menu Bar; change\r\n Currency of your choice; coupons will then appear in your chosen currency.','2024-05-14 17:32:04.658343'),(11,'How do you redeem a coupon online / in person?','From the 2nd from the top Menu Bar click on the Service / Topic you desire; Based on your location, the most popular coupons will appear; select from the menu bar to right of\r\nTHE SERVICE / TOPIC you have chosen: there are 3 drop-down menus plus a bar to enter the location you are interested in; you can reset these filters by clicking on the button to the right of the last filter; click on the coupon you desire to redeem; you will receive a confirmation email that your coupon has been redeemed.','2024-05-14 17:34:11.424971'),(12,'How can you change your method of payment?','Go into your profile; cancel credit or debit card listed; add replacement credit card or debit card.','2024-05-14 17:35:55.623514'),(13,'How can you change your personal / business information?','Sign in on the platform; go to the “Profile Section” on the upper right hand side of your \r\nscreen; click on “Profile” and then click the “Edit Profile” button on the left side of your screen;','2024-05-14 17:44:41.030054'),(14,'How do you know that your Hamsa Account support has been sent to an Non-Profit?','In your profile menu the Non-Profit will appear with their logo.','2024-05-14 17:50:02.765259'),(15,'How do you know that a Non-Profit Organizations has been verified as being legitimate?			legitimate?','All Non-Profit Organizations that appear on the “Shukdeals” platform have been thoroughly checked out and vetted prior to their being listed on the platform.','2024-05-14 18:20:44.598736'),(16,'How do you know that your personal information is protected on the shukdeals.com platform?','Shukdeals.com has incorporated the latest cyber-security safeguards and does not engage with and will not have an agreement with third parties to provide all Members and Users of our platform their personal information.','2024-05-14 18:29:54.197961'),(17,'How do you change the language on the platform?','Click on 2nd drop-down menu from the left on the home page.','2024-05-14 18:32:17.413672'),(18,'How do you create a classified ad?','Click on your Profile Tab opening drop-down menu; click on Classified Listing tab;\r\nClick on “Add Classifieds” tab; follow fields to complete a Classified Ad; click Preview tab and Save;','2024-05-14 18:34:00.331347'),(19,'How do you ask for help?','Click 1st tab at bottom left side of any page.','2024-05-14 18:34:50.101685'),(20,'How do you contact us?','Click 2nd tab at bottom left side of any page.','2024-05-14 18:35:34.839835'),(21,'How do you add favorites?','Click on the heart shaped symbol and then click the save button.','2024-05-14 18:38:58.308283'),(22,'How do you change your password?','Go to settings, press change password, enter old password first, then new password (twice), press submit.','2024-05-14 18:40:14.201693'),(23,'How to search for the price and condition of a classified ad?','Click on the ad, click on the the “filter tab” and then select from the drop down menu\r\nThe “price” or “condition” field.','2024-05-14 18:41:17.790707'),(24,'How to find a specific item under “classifieds”?','After opening the classifieds tab, click on the “categories” drop down menu \r\n                               \r\n		 Or, alternatively\r\n\r\nEnter a subject in the “subject bar” at the top of the Shukdeals Home Page & click on\r\nThe “search” button.','2024-05-14 18:43:25.297746');
/*!40000 ALTER TABLE `content_faq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `content_privacypolicy`
--

DROP TABLE IF EXISTS `content_privacypolicy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `content_privacypolicy` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content_privacypolicy`
--

LOCK TABLES `content_privacypolicy` WRITE;
/*!40000 ALTER TABLE `content_privacypolicy` DISABLE KEYS */;
INSERT INTO `content_privacypolicy` VALUES (1,'<p>Privacy Policy<br>1. Privacy Policy Acknowledgment<br>1. The use of the website __SHUKDEALS.COM_________ (hereinafter \"the Site\") by you (hereinafter \"the User(s)\"), through accessing the site and/or registering on the site and/or opening an account on the site, constitutes, each of them, agreement to the following privacy policy, determined by __JFLIXS LTD_________ Company (hereinafter \"the Company\"). If you do not agree to this Privacy Policy (hereinafter \"the Privacy Policy\"), you must refrain from using the site.<br>Anyone performing an action on the site hereby declares that they are aware of the site\'s privacy policy, accept it, and will not have any claim or demand against the Company, its representatives, and managers, or anyone on its behalf, except for claims related to the breach of the Company\'s obligations under this Privacy Policy.<br>The Company reserves the right to change the Privacy Policy from time to time, at its sole discretion. However, any change in the Privacy Policy will apply only to site usage made after the said change.<br>The Privacy Policy is formulated in the male gender for convenience only, but it is intended for both men and women.</p><p>2. General<br>2.1 The Company operates a website for the benefit of users that provides a platform through which users can, among other things, ___help financially support their chosen Non-Profit Organization, all in accordance with and subject to the terms of use [link] and the privacy policy mentioned above.<br>2.2 When using the website, information about the user is collected. Some of the information personally identifies the user, such as their name, address, phone number, date of birth, payment methods used by the user, and more. This is information that the user knowingly provides, including when registering on the site. Some of the information does not personally identify the user and is not stored together with the user\'s personal details (this includes statistical information accumulated, for example, the pages the user viewed, the internet protocol (IP) address from which they browsed, the services that interest the user, and information collected about the user during their use of the site).<br>2.3 The Company is not responsible for the use of information about the user received not directly from the user but from third parties, including commercial entities or websites, including those presented on the site and not under the Company\'s control. In any case of doubt, it is the user\'s responsibility to check the privacy policy and terms of use of that business, website, or commercial entity.</p><p><br>3. Registration on the Website<br>3.1 During the initial registration on the website, the user is required to enter their email address and choose a password or other means of identification, according to the company\'s request and its exclusive discretion. Later in the registration process, the user will be required to fill out a registration form, which includes, among other things, the following details: first name, last name, date of birth, phone number, address, email address, password selection, and also an identification number and payment details (if it is a paid subscription [link]).</p><p>4. Use of Information<br>4.1 The use of information obtained about the user due to their use of the site will be in accordance with this privacy policy or pursuant to any legal provisions, including, but not limited to, the following purposes: enabling the user\'s use of the site; improving and enriching the services and content offered on the site; modifying or canceling existing services and content; enabling the purchase of services; publishing information and content; customizing advertisements displayed during the user\'s site visit based on the user\'s areas of interest.<br>4.2 The company automatically records all information received from the user\'s browser on its servers, including the user\'s IP address and all pages the user visited during their browsing. By agreeing to the privacy policy, the user expresses their consent for such documentation by the company for the following purposes: contacting the user; enabling repeat use and repurchase on the site; preventing illegal or unauthorized use of the site; sending marketing or promotional material to the user (either by the company or on its behalf) via email unless the user explicitly states in writing to the company that they do not wish to receive such marketing or promotional material. If the user wishes to stop receiving such email messages, they must contact _SHUKDEALS.COM__ and request the removal of their details from the distribution list.</p><p>4.3 The company will not sell or transfer the user\'s personal information, as provided by the user, in whole or in part, to any third party except as stated below. Despite the above, the company reserves the right to disclose the user\'s personal information, in whole or in part, to any third parties, subject to the occurrence of one of the following conditions: the company has obtained the user\'s consent to disclose this information; disclosure of the information or part of it to certain entities is required for the provision of services. It should be emphasized that these entities will have limited rights to use this information for the purpose for which the company provides the information, including but not limited to providing any service, using tools such as a platform or specific software, etc.; when the delivery of information is required by law or if necessary within legal proceedings, including in cases where the company receives a court order instructing it to disclose the user\'s details to any third party; in the case of a legal dispute between the user and the company requiring the disclosure of the user\'s details; if the company finds that the user\'s actions violate the terms of use or are contrary to the law, including for the purpose of performing any type of legal remedy; in the event that the company transfers the site\'s activity in any form to another corporation or merges its activity with another corporation, provided that the other corporation agrees to comply with the privacy policy provisions.</p><p><br>5. Use of Cookies<br>5.1 The company may use \"cookies\" for the proper and ongoing operation of the website, including collecting statistical data about site usage and adapting it to the user\'s personal preferences and information security needs.<br>5.2 If you do not wish to receive \"cookies,\" you can block them by adjusting your browser settings. It should be noted that disabling or blocking the option to receive \"cookies\" may prevent you from using some of the functions and services on the site.</p><p>6. Data Security<br>6.1 The company secures the website and implements systems and protocols for data security. While the company\'s activities minimize the risks of unauthorized computer penetration, this does not guarantee absolute security and immunity to safeguard the information. Therefore, the company does not commit to absolute immunity against unauthorized access to the information stored on the site (provided that the company has taken reasonable measures to prevent them).<br>7. Right to Review Information<br>7.1 According to the Privacy Protection Law, 1981, every person is entitled to review information held about them in a database. A person who has reviewed their information and found it to be incorrect, incomplete, unclear, or outdated is entitled to apply to the database owner to correct or delete the information. In addition, if the information in the company\'s databases is used for personal contact with the user, the user is entitled, according to the Privacy Protection Law, 1981, to demand in writing that the information referring to them be deleted from the database.<br>8. Changes<br>8.1 The company reserves the right to update this privacy policy from time to time. In the case of significant changes to this privacy policy, the company will notify users through a prominent notice on the home page of the website or by sending a direct message to the user. Continued use of the service constitutes the user\'s agreement to this privacy policy and its updates.<br>&nbsp;</p><p>Last undated on: 17/05/24</p>','2024-05-17 11:02:47.881847');
/*!40000 ALTER TABLE `content_privacypolicy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `content_termsandcondition`
--

DROP TABLE IF EXISTS `content_termsandcondition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `content_termsandcondition` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content_termsandcondition`
--

LOCK TABLES `content_termsandcondition` WRITE;
/*!40000 ALTER TABLE `content_termsandcondition` DISABLE KEYS */;
INSERT INTO `content_termsandcondition` VALUES (1,'<h3>Terms of Use (Users)<br>General</h3><p>1.1. The company &nbsp; &nbsp; &nbsp; &nbsp; JFLIXS LTD_______ (hereinafter \"the Company\") operates the website ___SHUKDEALS.COM__________ serving as a platform for supporting&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; NON-PROFIT ORGANIZATIONS____, all in accordance with and subject to these Terms of Use and the Privacy Policy [link] (hereinafter \"the Site,\" \"the Platform\"). It is clarified that the Site does not manage, edit, or provide the events, travelers, services, and various products on the Platform (hereinafter \"the Products\"), and the Company is not involved, directly or indirectly, in their sale, production, or registration. The sole responsibility for them lies with the relevant suppliers (hereinafter \"the Suppliers”).</p><p>1.2. The provisions of this agreement shall apply to all logins and/or use of the site by users and may be amended from time to time at the exclusive discretion of the Company. Therefore, before performing any action on the site, the user is requested to carefully read the Terms of Use.</p><p>1.3. The site contains links to other websites, whether Israeli or foreign. The Company is not responsible for their content, the information published on them, or any other details associated with them, including any harm to the user\'s feelings. The presence of a link on the site is not a recommendation to visit it. Similarly, the Company shall not be liable for any direct or indirect, financial or other damage caused to the user as a result of relying on the information appearing on linked websites.</p><p>1.4. The Company reserves the right to change, delete, and/or add to these Terms of Use at any time without the obligation to provide advance notice and/or explanation. Any addition and/or modification made to these terms shall bind the user with continued use of the site. The user\'s use of the site after the changes indicates their agreement to these changes. In the event that the user does not agree to the changes and/or the Terms of Use, they must refrain from further use of the site.<br>1.5. The validity of these Terms of Use is cumulative and not alternative, and the Terms of Use shall be interpreted as complementary to each other and not limiting one another.<br>1.6. The use of the site constitutes confirmation that the user has read the provisions of the Terms of Use, agrees to the Terms of Use, and agrees to act in accordance with them and accept them in full without any limitation or reservation.<br>1.7. It is hereby clarified that the use of the masculine language in the Terms of Use is for convenience only and is not intended to harm and/or create any discrimination.</p><p>1.8. The user is permitted to use the site for personal and non-commercial purposes only. It is strictly prohibited to use the site for any purpose other than personal and non-commercial use.<br>1.9. Any use of the site is solely at the user\'s own risk. The user shall have no claim and/or demand against the Company regarding the site and/or its use, and/or the use by a third party, for any direct or indirect damage resulting from the use and/or reliance on the content of a third party and/or due to a violation of privacy and/or any other harm arising from such use.<br>1.10. Computer records processing the company\'s data regarding the actions performed through the site shall constitute conclusive evidence of the actions and the details of these actions.</p><p>2. Purchase and Payment<br>2.1. To purchase products from suppliers through the site, the user must select the supplier/product and fill in all the required details. A corresponding voucher will be sent to the email by the supplier, based on the address provided by the user. The suppliers will display their business on the \"Business Page\" on the site, along with a link to their website (hereinafter: \"Business Page\"). The Business Page is the sole responsibility of the suppliers, and the Company has no connection or responsibility for its content. The purchase of products from the businesses is subject to the purchase terms, terms of use, and privacy policy as presented on the suppliers\' site, and the Company recommends reading them thoroughly.<br>2.2. The user will be charged directly by the suppliers for the purchased products, and it is solely their responsibility. The Company assumes no responsibility towards the user or the suppliers, including regarding payment collection and management.</p><p>2.3. If the user chooses to use the site through a payment plan, the user will be charged monthly using the credit card payment method (hereinafter: \"Payment Method\") until a cancellation notice is provided as stated in section 2.1 below. It is clarified that the Company is not a party to the agreement between the user and the Payment Method.<br>2.4. In the case of a payment plan, during the transaction and as a condition for its completion, the user will be required to enter a delivery address, email, phone number, and payment details. To ensure a quick and smooth process, accurate information must be provided. Providing false information knowingly may result in criminal liability, and the Company will take legal action in such cases. (Add Company will delete User’s Account)</p><p>2.5. A validation of the payment details will be conducted during the transaction, and upon receiving transaction approval by the Payment Method, the user will receive a corresponding confirmation email (hereinafter: \"Confirmation\").<br>2.6. Conducting transactions through the site implies the user\'s consent to receive an electronic invoice for the transaction via email.</p><p>3. Cancellation Policy<br>3.1. For cancellation, the user must notify the Company, via email as specified in section 8.7 below, of their intention to cancel the subscription (and the monthly charge) up to _7__ days before the scheduled charge in the relevant month.<br>3.2. The Company shall not be liable to users or any third party for products that were not provided or events/travel that were canceled or changed, and the like. The Company is not interested in having suppliers who did not fulfill their commitments to users continue to be active on the site, so please inform us in such cases.</p><p>4. Limitation of Liability<br>4.1. The Company makes significant efforts to provide users with a quality and secure browsing experience on the site. However, the site is not immune to errors and/or issues.<br>4.2. The Company shall not be liable in any way, explicitly or implicitly, in connection with the site, and also in connection with its suitability for a specific purpose and/or user requirements. The user declares and undertakes hereby that they are solely and fully responsible for any use they make of the site, and that they are aware that the Company is not responsible, directly or indirectly, for any use they make of the site as mentioned.<br>4.3. The site, and all its services, are provided to the user \"As Is,\" without any representation or commitment, and any reliance by the user on the foregoing is at their sole discretion and responsibility. Also, please note that some of the content published on the site is intended for marketing and advertising purposes for the products, and it should not be considered as objective or comprehensive content for the purpose of evaluating the products.</p><p>4.4.1. In the use and/or inability to use the site, including any service on it, for any reason whatsoever.<br>4.4.2. Messages and/or files and/or content received by the user during or following the use of the site.<br>4.4.3. Any act and/or omission performed through the site.<br>4.4.4. Interruptions, unavailability, and malfunctions of the site, including any service on it, for any reason whatsoever, including those arising from disruptions or failures in the communication and internet network or the telephony network.<br>4.5. The Company is not responsible for any illegal activity that may be carried out by users on the site or any other entity on the Internet over which it has no control.<br>4.6. The Company is not responsible in any way for information that the user is exposed to and/or receives and/or sends through the site.<br>4.7. The Company is not responsible for any commitment and/or action that the user performs through the site.<br>4.8. The limitation of liability in this section does not derogate from any other limitation of liability specified in the terms of use.</p><p>5. Forbidden Uses<br>5.1. The user is not allowed to perform the following actions and/or acts while using the site:<br>5.1.1. Conduct commercial use on the site and/or through it.<br>5.1.2. Disturb or violate any rights of another user on the site and/or on the internet, including the right to privacy and/or collect personal information about users on the site, including by automated means.<br>5.1.3. Harm the dignity or privacy of another user and/or use the site to harm the good name of any person and/or publish defamation, fraud, incitement, slander, and/or any other information that is false, unreliable, or intended to cause harm intentionally.<br>5.1.4. Use wireless networks to harm any person and/or company in any way.<br>5.1.5. Failure to comply with these restrictions may lead to preventing the user\'s access to the site by the Company and may expose the user to civil and/or criminal liability under any law.</p><p>6. Entitlement to Use the Site<br>6.1. The right to use the site in accordance with the terms of use and the company\'s policy, and to enjoy its services, will be given to every user. It is clarified that the company has the authority at any time, and at its sole discretion, to prevent users\' access to the site if their behavior is not in compliance with the terms of use or if they engage in improper or unreasonable use of the site.<br>6.2. However, the company reserves the right to allow or prevent the user\'s access to the site at any time, at its sole discretion and for any reason. The company also reserves the exclusive right to change or cease the operation of the site, in whole or in part, at any time and without notice, without the user having any claim, right, or demand in this regard.</p><p>7. Information Security<br>7.1. The company employs reasonable measures and utilizes technological and organizational security means to secure the site against unintentional or intentional exploitation, loss, destruction, or unauthorized access. However, the company clarifies that in cases beyond its control or resulting from force majeure, it does not undertake that the site will operate smoothly without any disruption. Additionally, the company does not guarantee that the data sent and received through the site will be immune from unauthorized access or penetration to the site. The user is aware that the company is not responsible for any direct or indirect damage or loss of any kind resulting from such events, including privacy breaches.<br>7.2. It is emphasized that the user is responsible for taking all necessary measures to protect the hardware, software, and information on the device through which access to the site is made. During the use and connection to the site, the user relinquishes any claim against the company for any damage that may result from accessing the site.</p><p>&nbsp;</p><p>8. Intellectual Property<br>8.1. All intellectual property rights, including copyrights and trademarks, in the site and all its elements, including the platform, site name, information, auxiliary software used for site operation, trademarks, design, texts, images, editing, design, symbols, and any other visual, audible, or combined content displayed on the site (hereinafter referred to as the \"Content\"), are owned by the company or another third party that has granted the company the authorization to use them, whether specific copyright notices are included regarding certain information or not. It is strictly prohibited to use these elements, including copying, duplication, distribution, display, transfer to a third party, or any other use without the express written consent of the company, except for authorized use resulting from your private use of products purchased on the site in accordance with the terms of use.<br>8.2. Without derogating from the generality of the above, it is emphasized that the name \"ShukDeals\" and the trademarks on the site (whether registered or not) are the sole property of the company. Any use of them without the explicit written consent of the company is strictly prohibited.<br>8.3. You may not copy, duplicate, distribute, sell, market, modify the design or graphical interface, translate any information from the site, or any products sold on it without the explicit written permission of the company.<br>8.4. The provisions of this clause are not intended to derogate from any legal provisions, and in addition to them, all limitations and prohibitions established by law regarding intellectual property rights shall apply.</p><p>9. General<br>9.1. The user hereby undertakes to comply with all legal provisions, including laws and regulations that may apply to his use of the site, including these terms of use.<br>9.2. Israeli law and the exclusive jurisdiction of the competent court in Tel Aviv apply to these terms of use and any matter related to the use of the site. In case of a dispute, the exclusive jurisdiction will be in Tel Aviv.<br>9.3. The user also undertakes to indemnify the company and/or its representatives for any damage, loss, loss of profit, payment, or expense caused to them, directly or indirectly, including damage to reputation, economic and/or commercial damage, attorney fees, and legal expenses, arising directly or indirectly from the user\'s breach of these terms of use and/or any act or omission of the user for which the company and/or its representatives have no responsibility. This includes claims, demands, and lawsuits arising directly or indirectly from the user\'s improper or illegal use of the site, including the violation of these terms.<br>9.4. Reservation of rights - Even if we waive any of our rights under the terms of use on the site in a particular case, or grant you an extension to fulfill any of your obligations, we are not obligated to waive our rights again or give you an extension in other cases.<br>9.5. Nullification or determination in regard to one of the terms of use on the site or part thereof will apply only to that term or part, as applicable, and they do not, by themselves, constitute a failure to enforce the binding nature of the terms of use on the site.<br>9.6. Force Majeure - We will not be considered to have violated the terms of use on the site if we are delayed and/or prevented from fulfilling any of our obligations as a result of force majeure events and/or other circumstances beyond our control, whether expected or not, including due to an order and/or regulation and/or directive of a governmental authority, earthquake, storm, material and/or service shortage, public transport strikes and/or moving service strikes, fire, flood, explosion, accident, disease, epidemic, blockade, Sabbath, riots, public order disruption, war, military operation, terrorist action and/or enmity, and/or any action taken by the user and/or any third party, and you will have no right and/or claim in such a case.<br>9.7. Contact. For any matter, question, and/or request, please contact us by email at [specified email address].<br>&nbsp;</p><p>Updated on: 17/5/24</p><p>&nbsp;</p><h3><strong>Terms of Use (Business)</strong></h3><p>General<br>1.1. __JFLIXS LTD_________ Company (hereinafter \"the Company\") operates the Shukdeals.com_____________ website, serving as the platform for raising financial support for non-profits, all in accordance with and subject to these terms of use and the privacy policy [link] (hereinafter \"the Site,\" \"the Platform”). It is clarified that organizations and businesses are solely responsible for the products, services (hereinafter \"the Products\"), and the information they publish, and the Company is not involved, directly or indirectly, in their sale, production, or registration. The exclusive responsibility for them lies with the businesses only (hereinafter \"the Business,\" \"the Businesses\").<br>1.2. The provisions of this agreement apply to every login and/or use of the site by businesses and may change from time to time at the sole discretion of the Company. Therefore, before taking any action on the site, businesses are advised to carefully read these terms of use.<br>1.3. The site contains links to other websites, both Israeli and foreign. The Company assumes no responsibility for their content, the information published on them, or any other details related to them, including any harm to the user\'s feelings. Businesses are fully responsible for any linked content, and the presence of a link on the site is not a recommendation to visit it. The Company will not be liable for any direct or indirect damage, financial or otherwise, caused to any third party as a result of relying on the information on linked sites, and businesses will have full and exclusive responsibility for each such link.<br>1.4. The Company reserves the right to change, delete, and/or add to these terms of use at any time without prior notice or review. Any addition and/or change made to these terms will bind businesses with continued use of the site. The use of the site after the changes indicates agreement to these changes. If a business does not agree to the changes and/or the terms of use, they must refrain from continuing to use the site.<br>1.5. The validity of these terms of use is cumulative and not alternative, and these terms will be interpreted as coexisting rather than limiting each other.<br>1.6. The use of the site constitutes an acknowledgment that the business has read the provisions of these terms of use and agrees to them without any limitation or reservation, and also agrees to act according to them and accept them in full.<br>1.7. Any use of the site is at the sole responsibility of the business. The business will have no claim and/or demand against the Company regarding the site and/or its use and/or the use by a third party, for any direct or indirect damage arising from the use and/or reliance on the content of a third party and/or due to a violation of privacy and/or any other damage resulting from the use as mentioned.<br>1.8. The computer records of the data processing by the Company regarding the actions performed through the site will constitute conclusive evidence of the willingness of the actions and the details of the actions.</p><p>2. Purchase and Payment<br>2.1. The business undertakes to publish on the business page, as defined below, all the required information from the seller in a distance sale transaction, according to the Consumer Protection Law, and to provide clear and accurate details as required by law. Without detracting from the above, the business will include a full, accurate, and up-to-date description of the business and its objectives, a link to the website, and, as relevant, a full, accurate, and up-to-date description of the products, their prices, various purchase conditions (such as shipping fees), according to the fields designated for this purpose by the Company and as updated from time to time by the Company (hereinafter: \"the Business Page\"). It is clarified that the business page is the sole responsibility of the business, and the Company has no connection or responsibility for its content. The purchase of products from businesses is subject to the purchase terms, terms of use, and privacy policy as presented on the business\'s website.<br>2.2. In order to purchase products from a business through the website, the user must select the business/product and fill in all required details, and a suitable voucher will be sent to the email by the business according to the address provided by the user.<br>2.3. The user\'s payment for the purchased products will be made directly by the relevant business and is solely its responsibility. The Company will not bear any responsibility towards the user or the businesses, including regarding payment collection and management.<br>2.4. The business\'s charge for the monthly payment will be made monthly by credit card charge (hereinafter: \"Payment Method\") until a cancellation notice is given as stated in Section 2.1 below. It is clarified that the Company is not a party to the agreement between the business and the Payment Method.<br>2.5. During the transaction and as a condition for its completion, the business will be required to enter a delivery address, email, telephone number, and payment details. To ensure quick and trouble-free communication, it is important to provide accurate information. Providing false information knowingly may result in criminal prosecution, and the Company will act to enforce the law in such cases. (Add Company will delete User’s Account)<br>2.6. After the Company\'s approval as stated in Section 5, a check of the payment details will be performed, and upon receiving transaction approval by the Payment Method, a corresponding notification will be sent to the business\'s email (hereinafter: \"Confirmation\").<br>2.7. Making contact through the website constitutes consent to receive a tax invoice for the transaction by email.</p><p><br>3. Cancellation Policy<br>3.1. The subscription is for an indefinite period. To cancel the subscription, the business must notify the Company, by email as specified in Section 8.7 below, of its desire to cancel the subscription (and the monthly charge) up to ___ days before the charge date in the relevant month. &nbsp;(Deletion process)<br>3.2. Upon the termination of the subscription, the Company may remove all advertisements on behalf of the business. However, the Company may, at its sole discretion, choose to keep previous advertisements and/or publish that the business used to have an account on the site.<br>3.3. The business is aware that the Company may, at any time, prevent, remove, and/or delete any businesses and/or products at its sole discretion without prior notice.</p><p>4. Limitation of Liability<br>4.1. The Company makes significant efforts to provide businesses with a quality and secure user experience on the website. However, the website is not immune to errors and/or issues.<br>4.2. The Company shall not bear any explicit or implied responsibility in connection with the website, including its suitability for a specific purpose and/or the requirements of businesses. The businesses declare and undertake that they are solely and fully responsible for any use they make of the website, and they are aware that the Company is not responsible, directly or indirectly, for any use they make of the website as mentioned.<br>4.3. The website and all its services are provided to businesses \"As Is,\" without any representation or warranty, and any reliance by the businesses on the aforementioned is done at their sole discretion and responsibility.<br>4.4. The Company and/or its representatives shall not be liable for any direct or indirect damage or loss, including consequential, incidental, or punitive damages (including, without limitation, damages for loss of employment and businesses, loss of profits, work stoppages, loss and/or loss of business information, harm to reputation, and any other financial loss, expected or unexpected) arising from or related to the website or any use thereof, including but not limited to:<br>4.4.1. Use and/or inability to use the website, including any service therein, for any reason whatsoever;<br>4.4.2. Messages and/or files and/or content received by businesses during or following the use of the website;<br>4.4.3. Any action and/or omission performed through the website;</p><p>5. Prohibited Uses<br>5.1. The business is not allowed to perform the following actions and/or activities while using the website:<br>5.2. Disrupting or violating any rights of another business on the website and/or on the internet, including the right to privacy and/or collecting personal information about users on the site, including by automated means.<br>5.3. Harming the dignity or privacy of users on the site and/or using the site to harm the good name of any person or to publish slander, fraud, incitement, defamation, and/or any other information that is false, unreliable, or likely to cause intentional harm.<br>5.4. Using the wireless network to harm any person and/or company in any way.<br>5.5 Failure to comply with these limitations may lead to the prevention of the business\'s access to the site by the Company and may expose it to civil and/or criminal liability, according to any law.</p><p>5.6. Interruptions, availability, and functionality of the website, including any service therein, for any reason whatsoever, including those arising from disruptions or failures in the telecommunications and internet network or the telephone network.<br>5.7. The Company is not responsible for any illegal activity that may occur, to the extent that it occurs, by any of the businesses on the website and/or any other cause beyond its control on the internet network.<br>5.8. The Company is not responsible in any way for information to which the business is exposed and/or receives and/or sends through the website.<br>5.9. The Company is not responsible for any commitment and/or action performed by the business through the website.<br>5.10. The limitation of liability in this section shall not derogate from any other limitation of liability specified in the terms of use.</p><p>6. Rights to Use the Website<br>6.1. The rights to use the website in accordance with the terms of use and the company\'s policy, and to enjoy its services, will be granted to any business approved by the Company, at its sole discretion, without being obligated to explain this. It is clarified that the company has the authority at any time and at its sole discretion to prevent businesses\' access to the site if their behavior is deemed inappropriate or if they engage in unreasonable use of the site, including non-compliance with the terms of use.<br>6.2. However, the company may allow or prohibit the business\'s access to the site at any time, at its sole discretion and for any reason. The company reserves the exclusive right to change or terminate the operation of the site, in whole or in part, at any time without notice, and without the business having any claim, right, or demand in this regard.</p><p>7. Information Security<br>7.1. The company employs reasonable measures and utilizes technological and organizational security measures to secure the website against accidental or intentional exploitation, loss, destruction, or unauthorized access. However, the company clarifies that in cases beyond its control or resulting from force majeure, it does not undertake that the website will operate smoothly without any disruption, and/or that the data sent and received through the website will be completely immune from unauthorized access and/or penetration. It is known to the business that the company is not liable for any damage and/or loss, direct or indirect, of any kind, caused as a result, including due to a breach of privacy.<br>7.2. It is emphasized that the business is responsible for taking all measures to protect the hardware, software, and information on the device through which access to the website is made during the use and connection to the site. The business acknowledges that the mere use of the site releases the company from liability for any damage that may be caused to the business as a result of connecting to the site.</p><p>8. Intellectual Property<br>8.1. All intellectual property rights, including copyright and trademarks, in the website and all its elements, including the platform, site name, information, supporting software for site operation, trademarks, design, text, images, editorial content, layout, symbols, signs, and any other visual, audio, or combined content as presented on the site (hereinafter: \"Content\"), are owned by the company or a third party that granted the company the right to use them, whether or not specific copyright notices are associated with the information. It is prohibited to use these elements, including copying, duplicating, distributing, displaying, transferring to third parties, and/or any other use without the express written consent of the company.<br>8.2. Notwithstanding the generality of the above, it is emphasized that the name \"ShukDeals\" and the trademarks on the site (whether registered or not) are the exclusive property of the company. Any use of them without the company\'s written consent is prohibited.<br>8.3. It is prohibited to copy, duplicate, distribute, sell, market, modify the design or graphic interface, and translate any information from the site without the explicit written permission of the company.<br>8.4. The business declares and undertakes that in the publication of information on its business page, it will not infringe the rights of any third party, including copyright, trademarks, or other intellectual property rights. The business is solely responsible for any publication, activity, text, information, graphics, images, audio, video, links, or any other information it displays on its business page on the site. The business will be solely responsible for any damage resulting from the violation of copyrights, trademarks, or other intellectual property rights and will immediately compensate the company for any claim or lawsuit filed against it in this matter.<br>8.5. The business acknowledges that all content on the site belongs to the company, except for content uploaded by the business itself. By uploading content to its business page on the site, the business grants the company a license to use the content (including logos and trademarks) for full and commercial use at its sole discretion, including creating derivative works and/or editing and/or adapting the content to the site and/or the platform.<br>8.6. The business undertakes not to publish unauthorized content, with an emphasis on content whose publication constitutes a violation of consumer protection law, privacy law, defamation law, and copyright law.<br>8.7. The business undertakes to provide proper and lawful service to consumers. Failure to provide proper service adversely affects the site and the company\'s reputation. Similarly, advertisements on the site that do not comply with the law cause reputational damage to the site and the company.<br>8.8. The business undertakes to indemnify and compensate the company, the site, and/or anyone acting on their behalf for any damage caused to the site and/or the company due to the business\'s actions or omissions that constitute a violation of the law or a violation of the terms of this agreement. \"Damage\" includes, but is not limited to, expenses, loss of profits, damage to reputation, lawyer\'s fees, legal expenses, fines, and the like.<br>8.9. The provisions of this section shall not derogate from any provisions of the law, and in addition to them, all limitations and prohibitions set forth in the law regarding intellectual property rights shall apply.</p><p>9. General<br>9.1. The business hereby undertakes to comply with all legal provisions, including laws and regulations that may apply to its use of the site, including these terms of use. Without derogating from the generality of the above, the business declares that it is familiar with the Consumer Protection Law and its regulations, and it commits to act in accordance with them, including any matters related to consumer rights for \"distance selling.\" The business shall be solely responsible for any damage resulting from its violation of the Consumer Protection Law, and it shall indemnify the company for any complaint, demand, or lawsuit filed against it and/or the site regarding this matter.<br>9.2. Israeli law and the exclusive jurisdiction of the Israeli courts shall apply to these terms of use and any matter related to the use of the site. In case of a dispute, the jurisdiction shall be exclusively in Tel Aviv.<br>9.3. Additionally, the business undertakes to indemnify the company and/or anyone acting on its behalf for any damage, loss, loss of profit, payment, or expense caused to them, directly or indirectly, including economic and/or commercial damage, lawyer\'s fees, legal expenses, fines, and the like, resulting from the business\'s violation of the terms of use and/or any act or omission of the business and/or any obligation for which the company and/or anyone acting on its behalf is not liable according to these terms of use.<br>9.4. Reservation of Rights - Even if we waive any of our rights under the terms of use on the site in a particular case or give you an extension to fulfill any of your obligations, we are not obligated to waive our rights again or give you an extension in other cases.<br>9.5. Cancellation or determination of the nullity of a term in the terms of use on the site or part thereof shall apply only to that term or that part, as applicable, and shall not affect their validity as a whole or undermine their binding effect.<br>9.6. Force Majeure - We will not be considered to have violated the terms of use on the site or be delayed and/or prevented from performing any of our obligations as a result of force majeure events and/or other circumstances beyond our control, whether foreseeable or not, including and without derogating from the generality of the above, due to an order and/or regulation and/or instruction of a governmental authority, earthquake, storm, shortage of materials and/or public services and/or transportation services, fire, flood, explosion, accident, disease, epidemic, strike, sabotage, blockade, riot, violation of public order, war, military operation, terrorist activity, and/or enmity, and/or any act performed by the user and/or any third party, and we will not have any right and/or claim in such a case.<br>9.7. Contact Us - For any matter, question, and/or request, please contact us by email at ___________________.<br>Updated on: 17/5/24&nbsp;</p><p>&nbsp;</p><h3><strong>Terms &amp; Conditions - Non-Profit Organizations</strong><br>&nbsp;</h3><p>1 General<br>&nbsp;</p><p>1.1 The company ___________ (hereinafter \"the Company\") operates the website _____________, serving as a platform for ____________________, all in accordance with and subject to these terms of use and the privacy policy [link] (hereinafter \"the Website,\" \"the Platform\").<br>1.2 It is clarified that the platform serves organizations that are non-profit organizations (associations, public benefit companies, etc.) (hereinafter \"the Organization,\" \"the Organizations\"), which are solely responsible for the information they publish. The Company is not directly or indirectly involved in the information, videos, etc., published by the Organizations, and the exclusive responsibility for them lies with the Organizations alone.<br>1.3 The provisions of these terms and conditions shall apply to every login and/or use of the website by the Organizations and may change from time to time, at the sole discretion of the Company. Therefore, before taking any action on the site, the Organizations are required to read, thoroughly review, these terms of use.<br>1.4 The website contains links to other websites, both Israeli and foreign. The Company assumes no responsibility for their content, the information published on them, or any other details related to them, including any emotional distress the user may experience. The Organizations are fully responsible for any link mentioned, and the presence of the link on the site is not a recommendation to visit it. Additionally, the Company is not responsible for any direct or indirect damage, financial or otherwise, caused to third parties as a result of relying on the information on the linked sites, and the Organizations have full and exclusive responsibility for any link associated with them.<br>1.5 The Company reserves the right to change, delete, and/or add to these terms of use at any time without prior notice and/or retroactively. Any addition and/or change made to these terms will bind the Organizations with their continued use of the site. The use of the site after making these changes indicates the Organizations\' agreement to these changes. If an organization does not agree to the changes and/or terms of use, it must refrain from continuing to use the site.<br>1.6 The validity of these terms of use is cumulative and not alternative, and these terms will be interpreted as coexisting and not limiting each other.<br>1.7 The use of the site constitutes an acknowledgment that the Organization has read the terms of use and agrees to them without limitation or reservation.<br>1.8 All use of the site is solely the responsibility of the Organization. The Company will not have any claim and/or demand against the Organization regarding the site and/or its use, and/or the use by a third party, for any direct or indirect damage arising from the use and/or reliance on the content of a third party and/or due to a violation of privacy and/or other harm resulting from such use.<br>1.9 Computer records of the Company\'s data processing regarding the actions performed through the site will be conclusive evidence of the actions and the details of the actions.<br>ChatGPT<br>2. Entitlement to Use and Registration on the Website<br>2.1 The right to use the site in accordance with the terms of use and the company\'s policy, and to enjoy its services, will be granted to any organization approved by the company, at its sole discretion and without the need to justify this. It is emphasized that the company has the right at any time, at its sole discretion, to prevent organizations from accessing the site if their behavior is inconsistent and/or if they engage in improper or unreasonable use of the site, including non-compliance with the terms of use.<br>2.2 However, the company may allow or prohibit the organization\'s access to the site at any time, at its sole discretion, and for any reason. The company reserves the exclusive right to change or terminate the operation of the site, in whole or in part, at any time without notice and without any claim, right, and/or demand by the organization in this regard.<br>2.3 Once an organization is approved by the company, as mentioned in clause 2.1, the organization will receive a notification via email or text message to the mobile number provided during the registration request.<br>2.4 An organization that has been approved, as mentioned above, undertakes to publish on its organization page, as defined below, all information regarding the organization\'s activities and goals, including the corporate registration number, explanatory videos, a link to the organization\'s website, ______________________, and any other information required by the company (hereinafter \"the Organization Page\"). The organization is solely responsible for providing clear and accurate information and ensuring that the information is updated at all times. It is clarified that the organization page is the sole responsibility of the organization, and the company has no connection or responsibility for its content.<br>2.5 The organization will have the ability to check and receive daily updates regarding how many subscribers and businesses have registered to support them, as well as how much support has been garnered from those subscribers to the specific organization.<br>2.6 An organization that is approved and registered on the site will be entitled to receive 55% of the total revenue from subscribers to various support plans [link] received from users on the site who choose to support their specific organization. The organization\'s share of the aforementioned revenue will be transferred to the payment method provided by the company at the time of registration and against a tax invoice, as stated, until the 15th of the following month.<br>2.7 The organization is aware and commits to promoting its organization page on the site through telephone communication, email, events, or via the organization\'s social media accounts to expand exposure to various users and businesses.</p><p>II Cancellation Policy<br>&nbsp;</p><p>II - 1 The subscription is for an indefinite period. To cancel the subscription, the organization must inform the company, by email as specified in section 8.7 below, of its desire to terminate the subscription. The cancellation will take effect at the end of the month in which the notice is provided.<br>II - 2 Upon the termination of the subscription, the company is authorized to remove the organization page and all advertisements on behalf of the organization. However, the company may, at its sole discretion, choose to keep past advertisements and/or publish that the organization previously operated an account on the site.<br>II - 3 The organization is aware that the company reserves the right, at any time, to terminate the subscription with the organization, prevent, remove, and/or delete any organizations and/or advertisements for any reason at its sole discretion and without prior notice.<br>3 Limitation of Liability<br>3.1 The company makes significant efforts to provide organizations with a quality and secure user experience on the site. However, the site is not immune to glitches and/or issues.<br>3.2 The company will not be held liable, explicitly or implicitly, in connection with the site or its suitability for a specific purpose and/or the requirements of the organizations. The organizations declare and commit that they are solely and fully responsible for any use they make of the site, and they are aware that the company is not responsible, either directly or indirectly, for any use they make of the site.<br>3.3 The site and all its services are offered to organizations \"As Is,\" without any representation or commitment on the part of the company. Organizations\' reliance on the aforementioned is made at their discretion and sole responsibility.<br>3.4 The company and/or anyone on its behalf will not bear any liability for any damage and/or loss, direct or indirect, including consequential, incidental, or punitive damages. This includes, without limitation, compensation for job and business loss, loss of profits, work stoppages and disruptions, loss and/or loss of business information, damage to reputation, and any<br>&nbsp;</p><p>Prohibited Uses<br>The organization is not allowed to perform the following actions while using the site:</p><p>3.1 Disturb or violate any rights of another organization on the site and/or on the internet, including the right to privacy and/or collect personal information about users on the site, including by automated means.<br>3.2 Harm the dignity or privacy of users on the site and/or use the site to harm the good name of any person and/or publish libelous, defamatory, inciteful, or any other false information.<br>3.3 Engage in any action or omission through the site.<br>3.4 The limitation of liability in this section is not intended to derogate from any other limitation of liability specified in the terms of use.<br>Unauthorized Uses<br>The organization is not authorized to engage in the following activities:<br>3.5 Disrupt or interfere with the proper functioning and/or security of the site, including any services on it, for any reason whatsoever.<br>3.6 Messages and/or files and/or content received by organizations during or as a result of using the site.<br>3.7 Any act or omission carried out through the site.<br>3.8Interruptions, availability, and functionality of the site, including any services on it, for any reason whatsoever, including those arising from disruptions or failures in the communication and internet network or the telephony network.<br>&nbsp;</p><p>4.1.1 The company is not responsible in any way for any illegal activity that may be carried out, to the extent it occurs, by any of the organizations on the site and/or by any other entity on the internet over which it has no control.<br>4.1.2 The company is not responsible in any way for any information to which the organization is exposed and/or receives and/or sends through the site.<br>4.1.3 The company is not responsible for any commitment and/or action that the organization performs through the site.<br>4.1.4 Failure to comply with these restrictions may result in the company preventing the organization\'s access to the site and may expose it to civil and/or criminal liability under any law.<br>&nbsp;</p><p>5 Information Security<br>5.1 The company employs reasonable measures and utilizes technological and organizational security measures to secure the site against accidental or intentional exploitation, loss, destruction, or unauthorized access. However, the company clarifies that in some cases,<br>The organization is not responsible for any disturbances or unauthorized access to the site that may occur due to reasons beyond its control or force majeure. The organization acknowledges that the company is not liable for any direct or indirect damages, of any kind, caused as a result, including privacy infringements.</p><p>5.2 It is emphasized that the organization is responsible for taking all necessary measures to protect hardware, software, and information on the device through which access to the site is made. The organization, by using the site, absolves the company of any liability for damages that may result from the connection to the site.<br>&nbsp;</p><p>6 Intellectual Property:<br>6.1 All intellectual property rights, including copyrights and trademarks, on the site and all its elements, including the platform, site name, information, auxiliary programs used to operate the site, trademarks, design, texts, images, editing, design, symbols, and any other visual or audio content presented on the site (hereinafter referred to as \"Content\"), are owned by the company or another third party that has granted the company permission to use them. The use of these elements, including copying, duplication, distribution, display, transfer to a third party, or any other use, without the explicit written consent of the company, is prohibited.<br>6.2 The name \"ShukDeals\" and trademarks on the site are the sole property of the company. Any use of them without the written and prior consent of the company is prohibited.<br>6.3 The organization declares and undertakes that the publication of information on its organization\'s page will not infringe on the rights of third parties, including copyright, trademarks, or other intellectual property rights.<br>6.4 The organization is solely responsible for all content displayed on its organization page on the site. The organization will be solely responsible for any damage resulting from the violation of copyright, trademarks, trade secrets, or other intellectual property rights.<br>If they are not under its control and/or result from force majeure, the organization does not undertake that the website will operate smoothly without any disturbance, and/or that the data sent and received through the website will be completely immune from unauthorized access or penetration to the website. The organization is aware, and it is declared that the company will not be responsible for any direct or indirect damage or loss of any kind resulting from it, including due to a violation of privacy.<br>6.5 It is emphasized that the organization is responsible for taking all necessary measures to protect the hardware, software, and information on the device from which</p><p>access to the website is made during the use and connection to the site. The mere use of the organization\'s website releases the company from any responsibility for any damage that may be caused to the business as a result of connecting to the site.<br>Intellectual Property<br>6.6 All intellectual property rights, including copyright and trademarks, on the website and all its elements, including the platform, the site name, the information in it, auxiliary software used to operate the site, the trademark, design, text, images, editing, design, symbols, and any other visual or audio content or their combination as displayed on the site (hereinafter referred to as \"the Content\"), are owned by the company or another third party that has granted the company the right to use them, whether specific information is subject to copyright or not. It is prohibited to use any of these elements, including copying, duplicating, distributing, displaying, or transferring to a third party, or any other use without the company\'s explicit written consent.<br>Without detracting from the generality of the above, it is emphasized that the name \"ShukDeals\" and the trademarks on the site (whether registered or not) are solely owned by the company. No use should be made of them without the company\'s written and prior consent.<br>6.5 The organization declares and undertakes that the publication of information on its organization\'s page will not violate the rights of third parties, including copyrights, trademarks, or other intellectual property rights. The organization is solely responsible for any publication, activity, text, information, graphics, images, audio, video, links, or any other information it presents on its organization\'s page on the site. The organization will be solely responsible for any damage resulting from the violation of copyrights, trademarks, and other intellectual property rights.<br>Other Legal Provisions</p><p>6.6 The organization will compensate the company immediately for any claim or lawsuit filed against it regarding this matter. The organization acknowledges and undertakes that all contents on the site belong to the company, except for content uploaded by the organization itself. By uploading content to its organization\'s page on the site, the organization grants the company a license to use the content (including logos and trademarks) for full commercial use at its discretion, including for the creation of derivative works and/or editing and/or adapting the content to the site and/or platform.<br>6.7 The organization undertakes not to publish unauthorized content, with an emphasis on content whose publication constitutes a violation of consumer protection laws, privacy laws, defamation laws, and copyright laws. The organization commits to managing its activities properly and in accordance with the law. Similarly, publications through the website that do not comply with the law may cause reputational damage to the site, the company, and the organization commits to avoiding any such harm to the site and the company.<br>6.8 The organization undertakes to indemnify and compensate the company and the site and/or anyone acting on their behalf for any damage caused to the site and/or the company due to the behavior or omission of the organization or anyone acting on its behalf, constituting a violation of the law and/or a breach of the provisions of this agreement. \"Damage\" includes expenses, loss of profits, harm to reputation, slander on the site, attorney\'s fees, legal expenses, fines, and the like.<br>6.9 The provisions of this clause are not intended to derogate from the provisions of any law, and, in addition, all restrictions and prohibitions set forth in the law regarding intellectual property rights shall apply.<br>&nbsp;</p><p>7 General<br>&nbsp;</p><p>7.1 The organization hereby undertakes to comply with all legal provisions, including laws and/or regulations that may apply to its use of the site, including these terms of use. Israeli law and the exclusive jurisdiction of the Israeli courts shall apply to these</p><p>terms of use and any matter related to them and/or arising from them is vested in the competent court in Israel.<br>7.3 Additionally, the organization commits to indemnifying and compensating the company and/or anyone acting on their behalf for any damage, loss, loss of profit, payment, or expense caused to them, directly or indirectly, including economic and/or commercial damage, attorney\'s fees, and legal expenses due to any claim, demand, and/or lawsuit arising directly or indirectly from the breach of the terms of use and/or any act or omission for which the company and/or anyone acting on their behalf shall have no liability; or that is brought against them due to the use of the organization of the site and/or content contrary to these terms of use and/or any act or omission of the organization.<br>By a third party as a result of the organization\'s invalid and/or unlawful use of the website, including a violation of these terms.<br>7.4 Reservation of Rights - even if we waive any of our rights under the terms of use in a specific case, or give the organization an extension to fulfill any of its commitments, we are not obligated to waive our right again or grant the organization an extension in other cases.<br>7.5 The cancellation or determination regarding the invalidity of any provision of the terms of use on the site or part thereof shall apply only to that provision or part, as applicable, and shall not in themselves be deemed to undermine the binding force of the terms of use on the site.<br>7.6 Force Majeure - We will not be considered as having breached the terms of use on the site if we are delayed and/or prevented from fulfilling any of our commitments due to force majeure events and/or other circumstances beyond our control, whether foreseeable or not, including as a result of an order and/or regulation and/or instruction of a government authority, an earthquake, a storm, a shortage of materials and/or public services and/or transportation services, fire, flooding, explosion, outbreak, accident, disease, epidemic, strike, Sabbath observance, embargo, riot, public disorder, war, military operation, terrorist action and/or enmity, and/or any action taken by the user and/or any third party, and you shall have no right and/or claim in such a case.</p><p>7.7 Contact. For any matter, question, and/or request, please contact us by email at ___________________.<br>Updated on: 19/5/24</p>','2024-05-17 17:24:40.632539');
/*!40000 ALTER TABLE `content_termsandcondition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deals_deal`
--

DROP TABLE IF EXISTS `deals_deal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deals_deal` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `actual_price` double NOT NULL,
  `deal_type` varchar(20) NOT NULL,
  `club_member_discount_type` varchar(20) DEFAULT NULL,
  `club_member_discount_value` double DEFAULT NULL,
  `weekly` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `location_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  `expiry_date` date DEFAULT NULL,
  `club_member_code` varchar(20) DEFAULT NULL,
  `free_member_code` varchar(20) DEFAULT NULL,
  `free_member_discount_type` varchar(20) DEFAULT NULL,
  `free_member_discount_value` double DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `paid` tinyint(1) NOT NULL,
  `business_sub_category_id` bigint(20) DEFAULT NULL,
  `business_sub_sub_category_id` bigint(20) DEFAULT NULL,
  `number_of_travellers` int(11) NOT NULL,
  `property_class` varchar(100) DEFAULT NULL,
  `ngo_fee` double NOT NULL,
  `shuk_fee` double NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `online_supported` tinyint(1) NOT NULL,
  `redemption_link` longtext DEFAULT NULL,
  `all_stores` tinyint(1) NOT NULL,
  `parent_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `deals_deal_location_id_f07dff95_fk_account_location_id` (`location_id`),
  KEY `deals_deal_user_id_ee936300_fk_account_myuser_id` (`user_id`),
  KEY `deals_deal_business_sub_categor_4296b76a_fk_account_b` (`business_sub_category_id`),
  KEY `deals_deal_business_sub_sub_cat_082c02b8_fk_account_b` (`business_sub_sub_category_id`),
  KEY `deals_deal_parent_id_cdcdc473_fk_deals_deal_id` (`parent_id`),
  CONSTRAINT `deals_deal_business_sub_categor_4296b76a_fk_account_b` FOREIGN KEY (`business_sub_category_id`) REFERENCES `account_businesscategory` (`id`),
  CONSTRAINT `deals_deal_business_sub_sub_cat_082c02b8_fk_account_b` FOREIGN KEY (`business_sub_sub_category_id`) REFERENCES `account_businesscategory` (`id`),
  CONSTRAINT `deals_deal_location_id_f07dff95_fk_account_location_id` FOREIGN KEY (`location_id`) REFERENCES `account_location` (`id`),
  CONSTRAINT `deals_deal_parent_id_cdcdc473_fk_deals_deal_id` FOREIGN KEY (`parent_id`) REFERENCES `deals_deal` (`id`),
  CONSTRAINT `deals_deal_user_id_ee936300_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deals_deal`
--

LOCK TABLES `deals_deal` WRITE;
/*!40000 ALTER TABLE `deals_deal` DISABLE KEYS */;
INSERT INTO `deals_deal` VALUES (1,'Streaming Site for the Jewish People','Get hours of streaming content from the Jewish world plus daily live content out of Israel. This streaming site is to strengthen the connections between Israel and the Diaspora. Free for soldiers & veterans and a nominal charge for all other users.',9999,'online','percentage',10,0,'2024-05-21 08:58:31.632880','2024-05-21 08:58:31.637435',4,15,'2024-07-05','WB9XIT','7HUWKM','percentage',100,'payment_pending',1,0,52,NULL,0,NULL,0,0,0,1,'www.jflixs.com',0,NULL);
/*!40000 ALTER TABLE `deals_deal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deals_dealclick`
--

DROP TABLE IF EXISTS `deals_dealclick`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deals_dealclick` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `deal_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deals_dealclick_deal_id_93e3f49c_fk_deals_deal_id` (`deal_id`),
  KEY `deals_dealclick_user_id_235d8b8e_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `deals_dealclick_deal_id_93e3f49c_fk_deals_deal_id` FOREIGN KEY (`deal_id`) REFERENCES `deals_deal` (`id`),
  CONSTRAINT `deals_dealclick_user_id_235d8b8e_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deals_dealclick`
--

LOCK TABLES `deals_dealclick` WRITE;
/*!40000 ALTER TABLE `deals_dealclick` DISABLE KEYS */;
INSERT INTO `deals_dealclick` VALUES (1,'2024-05-21 08:58:49.789360',1,14),(2,'2024-05-31 10:16:20.490163',1,11);
/*!40000 ALTER TABLE `deals_dealclick` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deals_dealimage`
--

DROP TABLE IF EXISTS `deals_dealimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deals_dealimage` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `deal_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deals_dealimage_deal_id_c747ca1d_fk_deals_deal_id` (`deal_id`),
  CONSTRAINT `deals_dealimage_deal_id_c747ca1d_fk_deals_deal_id` FOREIGN KEY (`deal_id`) REFERENCES `deals_deal` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deals_dealimage`
--

LOCK TABLES `deals_dealimage` WRITE;
/*!40000 ALTER TABLE `deals_dealimage` DISABLE KEYS */;
INSERT INTO `deals_dealimage` VALUES (1,'deals_images/15/None/WhatsApp_Image_2022-03-14_at_10.05.09_AM.jpeg','2024-05-21 08:58:31.642231',1),(2,'deals_images/15/None/IMG_1521.jpeg','2024-05-21 08:58:31.644838',1);
/*!40000 ALTER TABLE `deals_dealimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deals_dealredeem`
--

DROP TABLE IF EXISTS `deals_dealredeem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deals_dealredeem` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `deal_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deals_dealredeem_deal_id_9da443ff_fk_deals_deal_id` (`deal_id`),
  KEY `deals_dealredeem_user_id_f2031d14_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `deals_dealredeem_deal_id_9da443ff_fk_deals_deal_id` FOREIGN KEY (`deal_id`) REFERENCES `deals_deal` (`id`),
  CONSTRAINT `deals_dealredeem_user_id_f2031d14_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deals_dealredeem`
--

LOCK TABLES `deals_dealredeem` WRITE;
/*!40000 ALTER TABLE `deals_dealredeem` DISABLE KEYS */;
INSERT INTO `deals_dealredeem` VALUES (1,'2024-05-21 08:59:04.321506',1,14),(2,'2024-05-31 10:16:26.371987',1,11);
/*!40000 ALTER TABLE `deals_dealredeem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deals_flagged`
--

DROP TABLE IF EXISTS `deals_flagged`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deals_flagged` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `reason` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `deal_id` bigint(20) NOT NULL,
  `flagged_by_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deals_flagged_deal_id_ed3604ea_fk_deals_deal_id` (`deal_id`),
  KEY `deals_flagged_flagged_by_id_468d49f7_fk_account_myuser_id` (`flagged_by_id`),
  CONSTRAINT `deals_flagged_deal_id_ed3604ea_fk_deals_deal_id` FOREIGN KEY (`deal_id`) REFERENCES `deals_deal` (`id`),
  CONSTRAINT `deals_flagged_flagged_by_id_468d49f7_fk_account_myuser_id` FOREIGN KEY (`flagged_by_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deals_flagged`
--

LOCK TABLES `deals_flagged` WRITE;
/*!40000 ALTER TABLE `deals_flagged` DISABLE KEYS */;
/*!40000 ALTER TABLE `deals_flagged` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deals_order`
--

DROP TABLE IF EXISTS `deals_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deals_order` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `deal_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deals_order_deal_id_a9a896d1_fk_deals_deal_id` (`deal_id`),
  CONSTRAINT `deals_order_deal_id_a9a896d1_fk_deals_deal_id` FOREIGN KEY (`deal_id`) REFERENCES `deals_deal` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deals_order`
--

LOCK TABLES `deals_order` WRITE;
/*!40000 ALTER TABLE `deals_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `deals_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deals_payment`
--

DROP TABLE IF EXISTS `deals_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deals_payment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `amount` double NOT NULL,
  `description` longtext NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `order_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deals_payment_order_id_5a3288aa_fk_deals_order_id` (`order_id`),
  CONSTRAINT `deals_payment_order_id_5a3288aa_fk_deals_order_id` FOREIGN KEY (`order_id`) REFERENCES `deals_order` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deals_payment`
--

LOCK TABLES `deals_payment` WRITE;
/*!40000 ALTER TABLE `deals_payment` DISABLE KEYS */;
/*!40000 ALTER TABLE `deals_payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deals_propertydetails`
--

DROP TABLE IF EXISTS `deals_propertydetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deals_propertydetails` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `property_type` varchar(24) NOT NULL,
  `offer_text` longtext DEFAULT NULL,
  `price` double NOT NULL,
  `phone` varchar(17) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `deal_id` bigint(20) NOT NULL,
  `price_type` varchar(24) DEFAULT NULL,
  `no_of_bathroom` int(11) DEFAULT NULL,
  `no_of_bedroom` int(11) DEFAULT NULL,
  `sq_feet` int(11) DEFAULT NULL,
  `rent_period` smallint(5) unsigned DEFAULT NULL CHECK (`rent_period` >= 0),
  PRIMARY KEY (`id`),
  UNIQUE KEY `deal_id` (`deal_id`),
  CONSTRAINT `deals_propertydetails_deal_id_f0651817_fk_deals_deal_id` FOREIGN KEY (`deal_id`) REFERENCES `deals_deal` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deals_propertydetails`
--

LOCK TABLES `deals_propertydetails` WRITE;
/*!40000 ALTER TABLE `deals_propertydetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `deals_propertydetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deals_review`
--

DROP TABLE IF EXISTS `deals_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deals_review` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `rating` double NOT NULL,
  `comment` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `deal_id` bigint(20) NOT NULL,
  `reviewed_by_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deals_review_deal_id_3db62b3f_fk_deals_deal_id` (`deal_id`),
  KEY `deals_review_reviewed_by_id_c15532a4_fk_account_myuser_id` (`reviewed_by_id`),
  CONSTRAINT `deals_review_deal_id_3db62b3f_fk_deals_deal_id` FOREIGN KEY (`deal_id`) REFERENCES `deals_deal` (`id`),
  CONSTRAINT `deals_review_reviewed_by_id_c15532a4_fk_account_myuser_id` FOREIGN KEY (`reviewed_by_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deals_review`
--

LOCK TABLES `deals_review` WRITE;
/*!40000 ALTER TABLE `deals_review` DISABLE KEYS */;
/*!40000 ALTER TABLE `deals_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deals_reviewflag`
--

DROP TABLE IF EXISTS `deals_reviewflag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deals_reviewflag` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `reason` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `review_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deals_reviewflag_review_id_a8577d5d_fk_deals_review_id` (`review_id`),
  KEY `deals_reviewflag_user_id_aacb6395_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `deals_reviewflag_review_id_a8577d5d_fk_deals_review_id` FOREIGN KEY (`review_id`) REFERENCES `deals_review` (`id`),
  CONSTRAINT `deals_reviewflag_user_id_aacb6395_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deals_reviewflag`
--

LOCK TABLES `deals_reviewflag` WRITE;
/*!40000 ALTER TABLE `deals_reviewflag` DISABLE KEYS */;
/*!40000 ALTER TABLE `deals_reviewflag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deals_reviewmark`
--

DROP TABLE IF EXISTS `deals_reviewmark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deals_reviewmark` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `mark_type` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `review_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deals_reviewmark_review_id_95ea9d4f_fk_deals_review_id` (`review_id`),
  KEY `deals_reviewmark_user_id_68249a70_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `deals_reviewmark_review_id_95ea9d4f_fk_deals_review_id` FOREIGN KEY (`review_id`) REFERENCES `deals_review` (`id`),
  CONSTRAINT `deals_reviewmark_user_id_68249a70_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deals_reviewmark`
--

LOCK TABLES `deals_reviewmark` WRITE;
/*!40000 ALTER TABLE `deals_reviewmark` DISABLE KEYS */;
/*!40000 ALTER TABLE `deals_reviewmark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (25,'account','activitylog'),(19,'account','businesscategory'),(13,'account','code'),(14,'account','country'),(21,'account','currency'),(22,'account','currencyexchangerate'),(12,'account','deliverypartner'),(11,'account','familymember'),(24,'account','flagged'),(10,'account','location'),(8,'account','myuser'),(33,'account','ngopayout'),(23,'account','ngoreferaltoken'),(20,'account','ngovideo'),(36,'account','onelineuser'),(28,'account','paymentdetail'),(15,'account','plan'),(16,'account','planfeature'),(39,'account','productprice'),(18,'account','restaurantmenu'),(37,'account','revenue'),(9,'account','review'),(31,'account','reviewflag'),(30,'account','reviewmark'),(27,'account','stripedetailnew'),(40,'account','stripepaymentmethod'),(17,'account','temptoken'),(29,'account','tranziladetail'),(26,'account','tranzilatoken'),(38,'account','userlocation'),(32,'account','usertypecategory'),(34,'account','vendor'),(35,'account','vendorexpense'),(1,'admin','logentry'),(70,'article','news'),(3,'auth','group'),(2,'auth','permission'),(52,'blogs','category'),(53,'blogs','news'),(58,'classifieds','classified'),(61,'classifieds','classifiedcategory'),(62,'classifieds','classifiedclick'),(59,'classifieds','classifiedimage'),(60,'classifieds','flagged'),(64,'content','about'),(66,'content','aboutjourney'),(67,'content','aboutteam'),(69,'content','contactus'),(63,'content','faq'),(68,'content','privacypolicy'),(65,'content','termsandcondition'),(4,'contenttypes','contenttype'),(41,'deals','deal'),(51,'deals','dealclick'),(44,'deals','dealimage'),(47,'deals','dealredeem'),(48,'deals','flagged'),(42,'deals','order'),(43,'deals','payment'),(45,'deals','propertydetails'),(46,'deals','review'),(50,'deals','reviewflag'),(49,'deals','reviewmark'),(57,'jobs','application'),(54,'jobs','job'),(56,'jobs','jobclick'),(55,'jobs','resume'),(5,'sessions','session'),(6,'token_blacklist','blacklistedtoken'),(7,'token_blacklist','outstandingtoken');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=325 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-04-05 06:38:56.484346'),(2,'contenttypes','0002_remove_content_type_name','2024-04-05 06:38:56.515631'),(3,'auth','0001_initial','2024-04-05 06:38:56.702657'),(4,'auth','0002_alter_permission_name_max_length','2024-04-05 06:38:56.721350'),(5,'auth','0003_alter_user_email_max_length','2024-04-05 06:38:56.726703'),(6,'auth','0004_alter_user_username_opts','2024-04-05 06:38:56.730846'),(7,'auth','0005_alter_user_last_login_null','2024-04-05 06:38:56.736573'),(8,'auth','0006_require_contenttypes_0002','2024-04-05 06:38:56.737901'),(9,'auth','0007_alter_validators_add_error_messages','2024-04-05 06:38:56.741995'),(10,'auth','0008_alter_user_username_max_length','2024-04-05 06:38:56.746058'),(11,'auth','0009_alter_user_last_name_max_length','2024-04-05 06:38:56.750093'),(12,'auth','0010_alter_group_name_max_length','2024-04-05 06:38:56.762193'),(13,'auth','0011_update_proxy_permissions','2024-04-05 06:38:56.766679'),(14,'auth','0012_alter_user_first_name_max_length','2024-04-05 06:38:56.770685'),(15,'account','0001_initial','2024-04-05 06:38:57.377738'),(16,'deals','0001_initial','2024-04-05 06:38:57.842048'),(17,'deals','0002_delete_category','2024-04-05 06:38:57.849149'),(18,'deals','0003_alter_deal_updated_at','2024-04-05 06:38:57.864011'),(19,'deals','0004_deal_expiry_date','2024-04-05 06:38:57.894521'),(20,'deals','0005_alter_deal_expiry_date','2024-04-05 06:38:57.907842'),(21,'deals','0006_rename_discount_type_deal_club_member_discount_type_and_more','2024-04-05 06:38:58.194857'),(22,'deals','0007_alter_deal_club_member_code_and_more','2024-04-05 06:38:58.231915'),(23,'deals','0008_alter_deal_expiry_date','2024-04-05 06:38:58.265892'),(24,'deals','0009_deal_status','2024-04-05 06:38:58.302262'),(25,'deals','0010_remove_deal_duration_alter_deal_club_member_code_and_more','2024-04-05 06:38:58.424450'),(26,'deals','0011_alter_deal_club_member_discount_type','2024-04-05 06:38:58.458539'),(27,'deals','0012_alter_deal_club_member_discount_type','2024-04-05 06:38:58.474073'),(28,'deals','0013_remove_propertydetails_address_and_more','2024-04-05 06:38:58.809078'),(29,'deals','0014_delete_propertydetails','2024-04-05 06:38:58.817317'),(30,'deals','0015_propertydetails','2024-04-05 06:38:58.858736'),(31,'deals','0016_alter_propertydetails_phone','2024-04-05 06:38:58.887963'),(32,'deals','0017_review','2024-04-05 06:38:59.007946'),(33,'deals','0018_alter_dealimage_deal','2024-04-05 06:38:59.022868'),(34,'deals','0019_deal_active','2024-04-05 06:38:59.056933'),(35,'deals','0020_dealredeem','2024-04-05 06:38:59.116155'),(36,'deals','0021_propertydetails_price_type','2024-04-05 06:38:59.206930'),(37,'deals','0022_alter_propertydetails_price_type','2024-04-05 06:38:59.233349'),(38,'deals','0023_alter_propertydetails_offer_text','2024-04-05 06:38:59.259811'),(39,'deals','0024_alter_propertydetails_email_and_more','2024-04-05 06:38:59.316432'),(40,'jobs','0001_initial','2024-04-05 06:38:59.624989'),(41,'jobs','0002_alter_job_status','2024-04-05 06:38:59.641084'),(42,'jobs','0003_alter_job_expiry_date','2024-04-05 06:38:59.656871'),(43,'jobs','0004_alter_job_status','2024-04-05 06:38:59.670617'),(44,'jobs','0005_application_email_application_firstname_and_more','2024-04-05 06:38:59.803440'),(45,'jobs','0006_alter_application_firstname','2024-04-05 06:38:59.819048'),(46,'jobs','0007_alter_application_email_alter_application_lastname_and_more','2024-04-05 06:38:59.862346'),(47,'jobs','0008_resume_reuse','2024-04-05 06:38:59.894186'),(48,'jobs','0009_alter_application_job','2024-04-05 06:39:00.001288'),(49,'jobs','0010_alter_jobclick_job','2024-04-05 06:39:00.018391'),(50,'jobs','0011_application_deleted','2024-04-05 06:39:00.144763'),(51,'jobs','0012_alter_job_job_type','2024-04-05 06:39:00.162036'),(52,'account','0002_remove_myuser_user_type','2024-04-05 06:39:00.188574'),(53,'account','0003_myuser_user_type','2024-04-05 06:39:00.224976'),(54,'account','0004_alter_myuser_favourite_and_more','2024-04-05 06:39:00.308585'),(55,'account','0005_alter_myuser_favourite_and_more','2024-04-05 06:39:00.473987'),(56,'account','0006_alter_myuser_user_type','2024-04-05 06:39:00.497471'),(57,'account','0007_alter_myuser_currency_alter_myuser_language','2024-04-05 06:39:00.610306'),(58,'account','0008_country','2024-04-05 06:39:00.619140'),(59,'account','0009_myuser_country','2024-04-05 06:39:00.660396'),(60,'account','0010_alter_myuser_language','2024-04-05 06:39:00.684166'),(61,'account','0011_plan_alter_myuser_currency_alter_myuser_language_and_more','2024-04-05 06:39:00.826164'),(62,'account','0012_myuser_ngo','2024-04-05 06:39:00.867394'),(63,'account','0013_planfeature_numbers_allowed','2024-04-05 06:39:00.888824'),(64,'account','0014_myuser_plan','2024-04-05 06:39:00.938093'),(65,'account','0015_temptoken','2024-04-05 06:39:00.984564'),(66,'account','0016_plan_donation_plan_platform','2024-04-05 06:39:01.129282'),(67,'account','0017_rename_platform_plan_shuk_tv','2024-04-05 06:39:01.148864'),(68,'account','0018_alter_location_zipcode','2024-04-05 06:39:01.202377'),(69,'account','0019_alter_location_zipcode','2024-04-05 06:39:01.336446'),(70,'account','0020_alter_location_city_alter_location_country_and_more','2024-04-05 06:39:01.491847'),(71,'account','0021_alter_location_city_alter_location_country_and_more','2024-04-05 06:39:01.545354'),(72,'account','0022_alter_location_address_alter_location_latitude_and_more','2024-04-05 06:39:01.726817'),(73,'account','0023_alter_location_latitude_alter_location_location_and_more','2024-04-05 06:39:01.777893'),(74,'account','0024_remove_myuser_menu_restaurantmenu','2024-04-05 06:39:01.868354'),(75,'account','0025_alter_myuser_business_category','2024-04-05 06:39:01.905210'),(76,'account','0026_remove_deliverypartner_user','2024-04-05 06:39:02.031719'),(77,'account','0027_myuser_delivery_partner','2024-04-05 06:39:02.231669'),(78,'account','0028_businesscategory','2024-04-05 06:39:02.270858'),(79,'account','0029_remove_myuser_business_category','2024-04-05 06:39:02.337750'),(80,'account','0030_myuser_business_category','2024-04-05 06:39:02.489626'),(81,'account','0031_alter_myuser_phone','2024-04-05 06:39:02.598927'),(82,'account','0032_alter_ngovideo_updated_at','2024-04-05 06:39:02.626394'),(83,'account','0033_alter_ngovideo_users_liked','2024-04-05 06:39:02.661040'),(84,'account','0034_alter_ngovideo_users_liked','2024-04-05 06:39:02.787780'),(85,'account','0035_delete_ngovideo','2024-04-05 06:39:02.801710'),(86,'account','0036_ngovideo','2024-04-05 06:39:02.995319'),(87,'account','0037_remove_businesscategory_image','2024-04-05 06:39:03.017192'),(88,'account','0038_businesscategory_keyword','2024-04-05 06:39:03.037769'),(89,'account','0039_alter_code_usage','2024-04-05 06:39:03.064307'),(90,'account','0040_currency','2024-04-05 06:39:03.073701'),(91,'account','0041_currencyexchangerate','2024-04-05 06:39:03.143784'),(92,'account','0042_alter_myuser_favourite','2024-04-05 06:39:03.171958'),(93,'account','0043_ngoreferaltoken','2024-04-05 06:39:03.218406'),(94,'classifieds','0001_initial','2024-04-05 06:39:03.419273'),(95,'classifieds','0002_alter_classified_contact_email','2024-04-05 06:39:03.465971'),(96,'classifieds','0003_alter_classified_contact_phone','2024-04-05 06:39:03.557106'),(97,'classifieds','0004_alter_classified_contact_phone','2024-04-05 06:39:03.594987'),(98,'classifieds','0005_classified_expiry_date','2024-04-05 06:39:03.645488'),(99,'classifieds','0006_alter_classified_expiry_date','2024-04-05 06:39:03.706618'),(100,'classifieds','0007_alter_classified_expiry_date','2024-04-05 06:39:03.756859'),(101,'classifieds','0008_rename_monthly_price_classified_price_and_more','2024-04-05 06:39:03.872018'),(102,'classifieds','0009_alter_classified_price_type','2024-04-05 06:39:03.898331'),(103,'classifieds','0010_classified_active','2024-04-05 06:39:03.945985'),(104,'classifieds','0011_alter_classifiedimage_classified','2024-04-05 06:39:03.990398'),(105,'account','0044_alter_myuser_plan','2024-04-05 06:39:04.027979'),(106,'account','0045_alter_review_rating','2024-04-05 06:39:04.296157'),(107,'account','0046_alter_review_reviewed_by','2024-04-05 06:39:04.335386'),(108,'account','0047_alter_location_latitude_alter_location_longitude','2024-04-05 06:39:04.400164'),(109,'account','0048_alter_location_location_alter_location_user','2024-04-05 06:39:04.483227'),(110,'account','0049_alter_location_latitude_alter_location_longitude','2024-04-05 06:39:04.656734'),(111,'account','0050_remove_businesscategory_parent','2024-04-05 06:39:04.727119'),(112,'account','0051_remove_myuser_favourite_myuser_favourite_user','2024-04-05 06:39:04.848576'),(113,'account','0052_myuser_favourite_deal','2024-04-05 06:39:04.935884'),(114,'account','0053_myuser_favourite_classified','2024-04-05 06:39:05.077691'),(115,'account','0054_myuser_favourite_ngo_videos','2024-04-05 06:39:05.164262'),(116,'account','0055_rename_favourite_ngo_videos_myuser_favourite_ngo_video','2024-04-05 06:39:05.200285'),(117,'account','0056_alter_myuser_image','2024-04-05 06:39:05.371145'),(118,'account','0057_alter_myuser_cover_pic','2024-04-05 06:39:05.501935'),(119,'account','0058_familymember_email_add_familymember_phone_num','2024-04-05 06:39:05.597625'),(120,'account','0059_alter_familymember_email_add_and_more','2024-04-05 06:39:05.737529'),(121,'account','0060_alter_familymember_image','2024-04-05 06:39:05.776836'),(122,'account','0061_myuser_pinned_classified','2024-04-05 06:39:05.869629'),(123,'account','0062_alter_myuser_currency','2024-04-05 06:39:05.900090'),(124,'account','0063_deliverypartner_image','2024-04-05 06:39:05.922786'),(125,'account','0064_alter_deliverypartner_image','2024-04-05 06:39:05.953547'),(126,'account','0065_alter_myuser_ngo','2024-04-05 06:39:05.979718'),(127,'account','0066_myuser_favourite_job','2024-04-05 06:39:06.069614'),(128,'account','0067_alter_currencyexchangerate_from_currency_and_more','2024-04-05 06:39:06.277080'),(129,'account','0068_remove_myuser_currency_and_more','2024-04-05 06:39:06.454821'),(130,'account','0069_myuser_currency','2024-04-05 06:39:06.527765'),(131,'account','0070_alter_myuser_currency','2024-04-05 06:39:06.605428'),(132,'account','0071_alter_myuser_currency','2024-04-05 06:39:06.690292'),(133,'account','0072_myuser_stripe_customer_id','2024-04-05 06:39:06.735795'),(134,'account','0073_remove_myuser_stripe_customer_id_stripedetail','2024-04-05 06:39:06.931767'),(135,'account','0074_myuser_stripe_customer_id_myuser_stripe_source_token_and_more','2024-04-05 06:39:07.202127'),(136,'account','0075_remove_myuser_stripe_source_token_stripedetail','2024-04-05 06:39:07.298003'),(137,'account','0076_alter_stripedetail_payment_method','2024-04-05 06:39:07.343288'),(138,'account','0077_stripedetail_amount_stripedetail_currency_and_more','2024-04-05 06:39:07.475139'),(139,'account','0078_stripedetail_cancellation_reason_and_more','2024-04-05 06:39:07.636218'),(140,'account','0079_alter_stripedetail_status','2024-04-05 06:39:07.658474'),(141,'account','0080_transaction','2024-04-05 06:39:07.737080'),(142,'account','0081_stripedetail_client_secret','2024-04-05 06:39:07.838348'),(143,'account','0082_remove_stripedetail_client_secret_and_more','2024-04-05 06:39:07.988376'),(144,'account','0083_alter_planfeature_feature_type','2024-04-05 06:39:08.008973'),(145,'account','0084_alter_planfeature_feature_type','2024-04-05 06:39:08.019194'),(146,'account','0085_myuser_extra_deal_alter_stripedetail_item_type','2024-04-05 06:39:08.087578'),(147,'account','0086_myuser_extra_location','2024-04-05 06:39:08.134722'),(148,'account','0087_stripedetail_locations_to_activate','2024-04-05 06:39:08.179849'),(149,'account','0088_myuser_extra_classified','2024-04-05 06:39:08.225911'),(150,'account','0089_alter_location_zipcode','2024-04-05 06:39:08.267446'),(151,'account','0090_alter_familymember_image','2024-04-05 06:39:08.399626'),(152,'account','0091_currency_sign','2024-04-05 06:39:08.420162'),(153,'account','0092_alter_currency_sign','2024-04-05 06:39:08.438416'),(154,'deals','0025_alter_deal_location','2024-04-05 06:39:08.466667'),(155,'deals','0026_alter_deal_active','2024-04-05 06:39:08.494451'),(156,'deals','0027_alter_deal_active','2024-04-05 06:39:08.521144'),(157,'deals','0028_alter_deal_active','2024-04-05 06:39:08.550189'),(158,'deals','0029_alter_deal_active','2024-04-05 06:39:08.578041'),(159,'deals','0030_remove_deal_active','2024-04-05 06:39:08.700591'),(160,'deals','0031_deal_active','2024-04-05 06:39:08.742125'),(161,'deals','0032_flagged','2024-04-05 06:39:08.811081'),(162,'deals','0033_reviewmark_reviewflag','2024-04-05 06:39:08.960266'),(163,'deals','0034_dealclick','2024-04-05 06:39:09.111487'),(164,'deals','0035_deal_paid','2024-04-05 06:39:09.158275'),(165,'account','0093_flagged','2024-04-05 06:39:09.233105'),(166,'account','0094_myuser_is_approved','2024-04-05 06:39:09.282668'),(167,'account','0095_alter_myuser_is_approved','2024-04-05 06:39:09.315671'),(168,'account','0096_remove_myuser_is_approved','2024-04-05 06:39:09.354188'),(169,'account','0097_myuser_is_approved','2024-04-05 06:39:09.403200'),(170,'account','0098_myuser_is_deleted_myuser_parent','2024-04-05 06:39:09.603821'),(171,'account','0099_myuser_relation_alter_familymember_relation','2024-04-05 06:39:09.671451'),(172,'account','0100_alter_familymember_relation_alter_myuser_relation','2024-04-05 06:39:09.728490'),(173,'account','0101_activitylog','2024-04-05 06:39:09.848609'),(174,'account','0102_rename_created_tile_activitylog_created_time','2024-04-05 06:39:09.886807'),(175,'account','0103_alter_familymember_relation_alter_myuser_relation','2024-04-05 06:39:09.943025'),(176,'account','0104_tranzilatoken','2024-04-05 06:39:09.999215'),(177,'account','0105_tranziladetail','2024-04-05 06:39:10.241810'),(178,'account','0106_rename_expiry_month_tranzilatoken_expire_month_and_more','2024-04-05 06:39:10.319791'),(179,'account','0107_remove_tranziladetail_amount_and_more','2024-04-05 06:39:10.914715'),(180,'account','0108_stripedetailnew_payment_detail_and_more','2024-04-05 06:39:11.020164'),(181,'account','0109_delete_tranziladetail','2024-04-05 06:39:11.026680'),(182,'account','0110_currency_sign_svg','2024-04-05 06:39:11.045593'),(183,'account','0111_tranziladetail','2024-04-05 06:39:11.104692'),(184,'account','0112_remove_myuser_pinned_classified','2024-04-05 06:39:11.253359'),(185,'account','0113_tranziladetail_error_code_tranziladetail_error_info','2024-04-05 06:39:11.295202'),(186,'account','0114_alter_tranziladetail_card_last_four_and_more','2024-04-05 06:39:11.691305'),(187,'account','0115_alter_tranziladetail_transaction_id','2024-04-05 06:39:11.719974'),(188,'account','0116_reviewmark','2024-04-05 06:39:11.797615'),(189,'account','0117_reviewflag','2024-04-05 06:39:11.873297'),(190,'account','0118_rename_comment_reviewflag_reason','2024-04-05 06:39:11.914989'),(191,'account','0119_myuser_is_phone_verified','2024-04-05 06:39:12.031889'),(192,'account','0120_alter_tranzilatoken_user','2024-04-05 06:39:12.127655'),(193,'account','0121_stripedetailnew_amount_stripedetailnew_currency','2024-04-05 06:39:12.292772'),(194,'account','0122_tranzilatoken_card_mask','2024-04-05 06:39:12.330639'),(195,'account','0123_myuser_delete_reason','2024-04-05 06:39:12.371607'),(196,'account','0124_businesssubcategory','2024-04-05 06:39:12.517275'),(197,'account','0125_usertypecategory','2024-04-05 06:39:12.527487'),(198,'account','0126_myuser_user_type_category','2024-04-05 06:39:12.596203'),(199,'account','0127_myuser_business_sub_category','2024-04-05 06:39:12.746912'),(200,'deals','0036_deal_business_sub_category','2024-04-05 06:39:12.806605'),(201,'deals','0037_remove_deal_business_sub_category','2024-04-05 06:39:12.875617'),(202,'account','0128_remove_myuser_business_sub_category','2024-04-05 06:39:12.918333'),(203,'account','0129_delete_businesssubcategory','2024-04-05 06:39:12.927763'),(204,'account','0130_businesscategory_parent','2024-04-05 06:39:12.979523'),(205,'account','0131_businesscategory_display_type','2024-04-05 06:39:13.010406'),(206,'account','0132_remove_transaction_stripe_remove_transaction_user_and_more','2024-04-05 06:39:13.237060'),(207,'account','0133_myuser_extra_weekly_deal','2024-04-05 06:39:13.360016'),(208,'account','0134_myuser_provider_type','2024-04-05 06:39:13.401910'),(209,'account','0135_rename_provider_type_myuser_service_provider_type','2024-04-05 06:39:13.447279'),(210,'account','0136_myuser_reservation_walkin','2024-04-05 06:39:13.487374'),(211,'account','0137_myuser_active','2024-04-05 06:39:13.537002'),(212,'account','0138_alter_paymentdetail_item_type','2024-04-05 06:39:13.569674'),(213,'account','0139_ngopayout','2024-04-05 06:39:13.666137'),(214,'account','0140_remove_ngopayout_main_amount_in_usd_and_more','2024-04-05 06:39:13.755028'),(215,'account','0141_alter_ngopayout_payout_date','2024-04-05 06:39:13.800243'),(216,'account','0142_ngopayout_payment_detail','2024-04-05 06:39:13.858459'),(217,'account','0143_vendor_vendorexpense','2024-04-05 06:39:13.895443'),(218,'account','0144_vendorexpense_created_at','2024-04-05 06:39:13.921068'),(219,'account','0145_rename_vendor_vendorexpense_vendor','2024-04-05 06:39:13.969145'),(220,'account','0146_alter_myuser_facebook_url_alter_myuser_instagram_url_and_more','2024-04-05 06:39:14.598945'),(221,'account','0147_alter_deliverypartner_image_alter_familymember_image_and_more','2024-04-05 06:39:14.843043'),(222,'account','0148_onelineuser','2024-04-05 06:39:14.898389'),(223,'account','0149_alter_onelineuser_user','2024-04-05 06:39:14.932602'),(224,'account','0150_remove_ngovideo_users_liked','2024-04-05 06:39:15.061671'),(225,'account','0151_vendorexpense_amount_vendorexpense_date_and_more','2024-04-05 06:39:15.104716'),(226,'account','0152_vendorexpense_paid','2024-04-05 06:39:15.127652'),(227,'account','0153_revenue','2024-04-05 06:39:15.204171'),(228,'account','0154_tranziladetail_status','2024-04-05 06:39:15.235735'),(229,'account','0155_tranziladetail_user','2024-04-05 06:39:15.288898'),(230,'account','0156_myuser_plan_upgrade_date','2024-04-05 06:39:15.403945'),(231,'account','0157_userlocation','2024-04-05 06:39:15.480725'),(232,'account','0158_remove_location_is_primary_remove_location_user','2024-04-05 06:39:15.590275'),(233,'account','0159_location_store_manager_email_and_more','2024-04-05 06:39:15.629719'),(234,'account','0160_alter_location_store_manager_email_and_more','2024-04-05 06:39:15.697652'),(235,'account','0161_alter_location_store_manager_email_and_more','2024-04-05 06:39:15.709033'),(236,'account','0162_alter_location_store_manager_email_and_more','2024-04-05 06:39:15.746851'),(237,'account','0163_myuser_is_store','2024-04-05 06:39:15.801414'),(238,'account','0164_remove_myuser_is_store','2024-04-05 06:39:15.845697'),(239,'account','0165_myuser_is_store','2024-04-05 06:39:15.899957'),(240,'account','0166_stripedetailnew_card_mask_and_more','2024-04-05 06:39:16.104174'),(241,'account','0167_alter_plan_amount_alter_plan_donation_and_more','2024-04-05 06:39:16.134004'),(242,'account','0168_remove_plan_donation_remove_plan_shuk_tv','2024-04-05 06:39:16.172471'),(243,'account','0169_productprice','2024-04-05 06:39:16.274793'),(244,'account','0170_myuser_is_default_ngo_alter_myuser_user_type_and_more','2024-04-05 06:39:16.431142'),(245,'account','0171_alter_paymentdetail_item_type_stripepaymentmethod','2024-04-05 06:39:16.518089'),(246,'account','0172_stripepaymentmethod_is_default_and_more','2024-04-05 06:39:16.614291'),(247,'account','0173_businesscategory_name_es','2024-04-05 06:39:16.632395'),(248,'account','0174_businesscategory_name_ar_businesscategory_name_de_and_more','2024-04-05 06:39:16.901185'),(249,'account','0175_usertypecategory_name_ar_usertypecategory_name_de_and_more','2024-04-05 06:39:17.028081'),(250,'account','0176_alter_myuser_delete_reason','2024-04-05 06:39:17.068487'),(251,'admin','0001_initial','2024-04-05 06:39:17.153707'),(252,'admin','0002_logentry_remove_auto_add','2024-04-05 06:39:17.187360'),(253,'admin','0003_logentry_add_action_flag_choices','2024-04-05 06:39:17.220308'),(254,'article','0001_initial','2024-04-05 06:39:17.303185'),(255,'article','0002_news_image','2024-04-05 06:39:17.346182'),(256,'article','0003_alter_news_image','2024-04-05 06:39:17.399196'),(257,'article','0004_delete_news','2024-04-05 06:39:17.408364'),(258,'article','0005_initial','2024-04-05 06:39:17.493350'),(259,'article','0006_news_status','2024-04-05 06:39:17.640639'),(260,'article','0007_alter_news_image','2024-04-05 06:39:17.693656'),(261,'article','0008_alter_news_image','2024-04-05 06:39:17.745733'),(262,'article','0009_news_delete_requested_news_deleted','2024-04-05 06:39:17.933049'),(263,'article','0010_alter_news_status','2024-04-05 06:39:17.980380'),(264,'article','0011_news_created_at','2024-04-05 06:39:18.036747'),(265,'article','0012_alter_news_created_at','2024-04-05 06:39:18.070419'),(266,'article','0013_news_is_popular','2024-04-05 06:39:18.121945'),(267,'blogs','0001_initial','2024-04-05 06:39:18.225543'),(268,'classifieds','0012_alter_classified_location','2024-04-05 06:39:18.264821'),(269,'classifieds','0013_flagged','2024-04-05 06:39:18.450667'),(270,'classifieds','0014_classified_pinned','2024-04-05 06:39:18.507623'),(271,'classifieds','0015_classified_paid','2024-04-05 06:39:18.566103'),(272,'classifieds','0016_classifiedcategory','2024-04-05 06:39:18.579641'),(273,'classifieds','0017_classified_category','2024-04-05 06:39:18.646012'),(274,'classifieds','0018_classified_product_condition','2024-04-05 06:39:18.700730'),(275,'classifieds','0019_classified_ngo_fee_classified_shuk_fee_and_more','2024-04-05 06:39:18.909059'),(276,'classifieds','0020_classified_is_deleted','2024-04-05 06:39:18.964163'),(277,'classifieds','0021_classifiedclick','2024-04-05 06:39:19.053658'),(278,'classifieds','0022_rename_deal_classifiedclick_classified','2024-04-05 06:39:19.338803'),(279,'classifieds','0023_classifiedcategory_name_ar_and_more','2024-04-05 06:39:19.438705'),(280,'content','0001_initial','2024-04-05 06:39:19.448890'),(281,'content','0002_about','2024-04-05 06:39:19.459223'),(282,'content','0003_termsandcondition','2024-04-05 06:39:19.469491'),(283,'content','0004_aboutjourney_aboutteam_about_heading_and_more','2024-04-05 06:39:19.682091'),(284,'content','0005_aboutjourney_about_aboutteam_about','2024-04-05 06:39:19.729598'),(285,'content','0006_remove_aboutjourney_about_remove_aboutteam_about','2024-04-05 06:39:19.796355'),(286,'content','0007_about_team_description_about_team_heading','2024-04-05 06:39:19.824112'),(287,'content','0008_privacypolicy','2024-04-05 06:39:19.835242'),(288,'content','0009_contactus','2024-04-05 06:39:19.848503'),(289,'content','0010_alter_aboutjourney_icon_alter_aboutteam_image','2024-04-05 06:39:19.878138'),(290,'content','0011_alter_privacypolicy_description','2024-04-05 06:39:19.882983'),(291,'content','0012_alter_privacypolicy_description','2024-04-05 06:39:19.902282'),(292,'content','0013_alter_privacypolicy_description','2024-04-05 06:39:19.909404'),(293,'content','0014_alter_termsandcondition_description','2024-04-05 06:39:19.927414'),(294,'deals','0038_deal_business_sub_category_and_more','2024-04-05 06:39:20.139624'),(295,'deals','0039_remove_propertydetails_rental_type_and_more','2024-04-05 06:39:20.185220'),(296,'deals','0040_propertydetails_no_of_bathroom_and_more','2024-04-05 06:39:20.265228'),(297,'deals','0041_alter_propertydetails_price','2024-04-05 06:39:20.282060'),(298,'deals','0042_deal_number_of_travellers_deal_property_class','2024-04-05 06:39:20.390589'),(299,'deals','0043_alter_deal_property_class','2024-04-05 06:39:20.431967'),(300,'deals','0044_propertydetails_rent_period','2024-04-05 06:39:20.459590'),(301,'deals','0045_deal_ngo_fee_deal_shuk_fee','2024-04-05 06:39:20.663126'),(302,'deals','0046_deal_is_deleted','2024-04-05 06:39:20.722122'),(303,'deals','0047_deal_online_supported','2024-04-05 06:39:20.780104'),(304,'deals','0048_deal_redemption_link','2024-04-05 06:39:20.829744'),(305,'deals','0049_deal_all_stores','2024-04-05 06:39:20.886321'),(306,'deals','0050_deal_parent','2024-04-05 06:39:20.955214'),(307,'jobs','0013_job_salary_type','2024-04-05 06:39:21.015935'),(308,'jobs','0014_job_payment_currency','2024-04-05 06:39:21.071740'),(309,'jobs','0015_rename_payment_currency_job_salary_currency','2024-04-05 06:39:21.123943'),(310,'sessions','0001_initial','2024-04-05 06:39:21.148972'),(311,'token_blacklist','0001_initial','2024-04-05 06:39:21.384072'),(312,'token_blacklist','0002_outstandingtoken_jti_hex','2024-04-05 06:39:21.433422'),(313,'token_blacklist','0003_auto_20171017_2007','2024-04-05 06:39:21.479947'),(314,'token_blacklist','0004_auto_20171017_2013','2024-04-05 06:39:21.551395'),(315,'token_blacklist','0005_remove_outstandingtoken_jti','2024-04-05 06:39:21.602937'),(316,'token_blacklist','0006_auto_20171017_2113','2024-04-05 06:39:21.650188'),(317,'token_blacklist','0007_auto_20171017_2214','2024-04-05 06:39:21.813394'),(318,'token_blacklist','0008_migrate_to_bigautofield','2024-04-05 06:39:22.108039'),(319,'token_blacklist','0010_fix_migrate_to_bigautofield','2024-04-05 06:39:22.158219'),(320,'token_blacklist','0011_linearizes_history','2024-04-05 06:39:22.160060'),(321,'token_blacklist','0012_alter_outstandingtoken_user','2024-04-05 06:39:22.203393'),(322,'account','0177_stripedetailnew_event_type','2024-04-30 15:38:42.899293'),(323,'content','0015_alter_about_description','2024-06-19 13:13:30.444171'),(324,'content','0016_alter_about_description','2024-06-19 13:13:30.452273');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('5542aep58638z3cmjsiyjr31rrzz2rhx','.eJxVjEEOwiAQAP_C2ZCFpQgevfsGsmUXWzUlKe3J-HdD0oNeZybzVon2bUp7kzXNrC7KqtMvGyk_ZemCH7Tcq8512dZ51D3Rh236Vlle16P9G0zUpr7NMRQJzoAZ5GxoALRoDQKagJHZej-QsCMr4DxCgYhoiweONAIG9fkCqys2Zw:1saTpY:z_X_wctgqGH1loCgtN6weX9SJga809jC_rqv8HTNbTY','2024-08-18 05:30:56.836120'),('67r5o7zhaubnh74brdwlevvc21o24mcu','.eJxVjEEOwiAQAP_C2ZCFpQgevfsGsmUXWzUlKe3J-HdD0oNeZybzVon2bUp7kzXNrC7KqtMvGyk_ZemCH7Tcq8512dZ51D3Rh236Vlle16P9G0zUpr7NMRQJzoAZ5GxoALRoDQKagJHZej-QsCMr4DxCgYhoiweONAIG9fkCqys2Zw:1sZClz:wsiOxI69t-UTM6KpTZ0l8_CcnEId9ElyMPZiute9L2c','2024-08-14 17:05:59.313928'),('76fhkbuxrs3pq8yg7vl49hbfcft4zszj','.eJxVjEEOwiAQAP_C2ZCFpQgevfsGsmUXWzUlKe3J-HdD0oNeZybzVon2bUp7kzXNrC7KqtMvGyk_ZemCH7Tcq8512dZ51D3Rh236Vlle16P9G0zUpr7NMRQJzoAZ5GxoALRoDQKagJHZej-QsCMr4DxCgYhoiweONAIG9fkCqys2Zw:1sA2BH:0zwBZ5YPQ1Tns3T3k0EUvfvezFHtNc9jsCoZm0gARhk','2024-06-06 06:44:03.151473'),('7khq9gscevb7ft4mqi5huftss2zs3ghf','.eJxVjEEOwiAQAP_C2ZCFpQgevfsGsmUXWzUlKe3J-HdD0oNeZybzVon2bUp7kzXNrC7KqtMvGyk_ZemCH7Tcq8512dZ51D3Rh236Vlle16P9G0zUpr7NMRQJzoAZ5GxoALRoDQKagJHZej-QsCMr4DxCgYhoiweONAIG9fkCqys2Zw:1sMTty:C4VvejEyaJ-BbmEEih2tnXb9AAfDIl6oFq6Cm4afDS4','2024-07-10 14:45:38.735435'),('9uqn9978ixbmzmieprtyj2dyfksho6ff','.eJxVjEEOwiAQAP_C2ZCFpQgevfsGsmUXWzUlKe3J-HdD0oNeZybzVon2bUp7kzXNrC7KqtMvGyk_ZemCH7Tcq8512dZ51D3Rh236Vlle16P9G0zUpr7NMRQJzoAZ5GxoALRoDQKagJHZej-QsCMr4DxCgYhoiweONAIG9fkCqys2Zw:1sjMWP:8WNPhoH74EaPBhR9efgEm9Fj-SrdR1Pi-_BNudtyVl0','2024-09-11 17:31:53.501261'),('arsrocxxh3xjl13grbo2a4s6i83im1dw','.eJxVjEEOwiAQAP_C2ZCFpQgevfsGsmUXWzUlKe3J-HdD0oNeZybzVon2bUp7kzXNrC7KqtMvGyk_ZemCH7Tcq8512dZ51D3Rh236Vlle16P9G0zUpr7NMRQJzoAZ5GxoALRoDQKagJHZej-QsCMr4DxCgYhoiweONAIG9fkCqys2Zw:1sGjjR:1ArEKJkpoDkoQ36aqGk9V889rxbe_WpCSyHPvylL5fE','2024-06-24 18:27:01.158548'),('gsya8vxn5qcjhpu6q86sjepbh77hgt7y','.eJxVjEEOwiAQAP_C2ZCFpQgevfsGsmUXWzUlKe3J-HdD0oNeZybzVon2bUp7kzXNrC7KqtMvGyk_ZemCH7Tcq8512dZ51D3Rh236Vlle16P9G0zUpr7NMRQJzoAZ5GxoALRoDQKagJHZej-QsCMr4DxCgYhoiweONAIG9fkCqys2Zw:1seJM8:jL8UmajZeEspQpfHIR2zfSmpJc71Ha-Sbj4Y34pS9-Q','2024-08-28 19:08:24.231606'),('hmfhrmes1gstfc8zflorlbem32wcidap','.eJxVjEEOwiAQAP_C2ZCFpQgevfsGsmUXWzUlKe3J-HdD0oNeZybzVon2bUp7kzXNrC7KqtMvGyk_ZemCH7Tcq8512dZ51D3Rh236Vlle16P9G0zUpr7NMRQJzoAZ5GxoALRoDQKagJHZej-QsCMr4DxCgYhoiweONAIG9fkCqys2Zw:1se6eQ:_kLrI7ai00EOw-YrrB003wKjeQadCAONKW1XRggTBxI','2024-08-28 05:34:26.311119'),('kbh2cp6z2i6i8ggkdmpn5i1es4xbpmmh','.eJxVjEEOwiAQAP_C2ZCFpQgevfsGsmUXWzUlKe3J-HdD0oNeZybzVon2bUp7kzXNrC7KqtMvGyk_ZemCH7Tcq8512dZ51D3Rh236Vlle16P9G0zUpr7NMRQJzoAZ5GxoALRoDQKagJHZej-QsCMr4DxCgYhoiweONAIG9fkCqys2Zw:1sTgo9:liOMxJAUuKmXs69qeiMvnK5uBKSPCisZfioufJF_yVc','2024-07-30 11:57:25.406307'),('onxo3u0blmkd7zj88fewcxaws0a4mep9','.eJxVjEEOwiAQAP_C2ZCFpQgevfsGsmUXWzUlKe3J-HdD0oNeZybzVon2bUp7kzXNrC7KqtMvGyk_ZemCH7Tcq8512dZ51D3Rh236Vlle16P9G0zUpr7NMRQJzoAZ5GxoALRoDQKagJHZej-QsCMr4DxCgYhoiweONAIG9fkCqys2Zw:1rse19:ard9b4j4MYmt8brYxR7FoRio4b2bJEZzlHlhvjY8B-8','2024-04-19 07:29:43.216887'),('p2eadz9k2vir7gdcadnlgxf0444t3cud','.eJxVjEEOwiAQAP_C2ZCFpQgevfsGsmUXWzUlKe3J-HdD0oNeZybzVon2bUp7kzXNrC7KqtMvGyk_ZemCH7Tcq8512dZ51D3Rh236Vlle16P9G0zUpr7NMRQJzoAZ5GxoALRoDQKagJHZej-QsCMr4DxCgYhoiweONAIG9fkCqys2Zw:1sgEcA:RnjLyz20Z08bIN-XBgGaQbAzrEHYLz2aae_aUIuioOQ','2024-09-03 02:28:54.351831'),('vsid5dt709bxd39frfg1m0isgsl3vpil','.eJxVjEEOwiAQAP_C2ZCFpQgevfsGsmUXWzUlKe3J-HdD0oNeZybzVon2bUp7kzXNrC7KqtMvGyk_ZemCH7Tcq8512dZ51D3Rh236Vlle16P9G0zUpr7NMRQJzoAZ5GxoALRoDQKagJHZej-QsCMr4DxCgYhoiweONAIG9fkCqys2Zw:1sgcWc:EYF4o8Q37Bo-XyoVt_VdAryxHtN5_CCkn9KR-bhzNZQ','2024-09-04 04:00:46.951543'),('xzd9bygccfrilhd2waxlmx34vfwtbqkx','.eJxVjEEOwiAQAP_C2ZCFpQgevfsGsmUXWzUlKe3J-HdD0oNeZybzVon2bUp7kzXNrC7KqtMvGyk_ZemCH7Tcq8512dZ51D3Rh236Vlle16P9G0zUpr7NMRQJzoAZ5GxoALRoDQKagJHZej-QsCMr4DxCgYhoiweONAIG9fkCqys2Zw:1sCzFf:i3m1ojBqwxifMs2aL3JCr-RH1DJmkzpOeLewDfh7yGw','2024-06-14 10:12:47.968898'),('zclkpdrvu929oe2fsi9lp0hkz700bhds','.eJxVjEEOwiAQAP_C2ZCFpQgevfsGsmUXWzUlKe3J-HdD0oNeZybzVon2bUp7kzXNrC7KqtMvGyk_ZemCH7Tcq8512dZ51D3Rh236Vlle16P9G0zUpr7NMRQJzoAZ5GxoALRoDQKagJHZej-QsCMr4DxCgYhoiweONAIG9fkCqys2Zw:1seA8m:R7bDoQv5vQQsdhCMZg3stT9VY7vRgpTOUHsSH8oUTps','2024-08-28 09:18:00.425411');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_application`
--

DROP TABLE IF EXISTS `jobs_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobs_application` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) DEFAULT NULL,
  `job_id` bigint(20) NOT NULL,
  `resume_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  `email` varchar(200) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `phone` varchar(17) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jobs_application_job_id_7bb7e966_fk_jobs_job_id` (`job_id`),
  KEY `jobs_application_resume_id_df76097a_fk_jobs_resume_id` (`resume_id`),
  KEY `jobs_application_user_id_59477d51_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `jobs_application_job_id_7bb7e966_fk_jobs_job_id` FOREIGN KEY (`job_id`) REFERENCES `jobs_job` (`id`),
  CONSTRAINT `jobs_application_resume_id_df76097a_fk_jobs_resume_id` FOREIGN KEY (`resume_id`) REFERENCES `jobs_resume` (`id`),
  CONSTRAINT `jobs_application_user_id_59477d51_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_application`
--

LOCK TABLES `jobs_application` WRITE;
/*!40000 ALTER TABLE `jobs_application` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobs_application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_job`
--

DROP TABLE IF EXISTS `jobs_job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobs_job` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `roles_and_responsibilities` longtext NOT NULL,
  `job_type` varchar(20) NOT NULL,
  `salary` int(11) NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `expiry_date` date DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  `salary_type` varchar(20) NOT NULL,
  `salary_currency` varchar(5) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jobs_job_user_id_093659ab_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `jobs_job_user_id_093659ab_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_job`
--

LOCK TABLES `jobs_job` WRITE;
/*!40000 ALTER TABLE `jobs_job` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobs_job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_jobclick`
--

DROP TABLE IF EXISTS `jobs_jobclick`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobs_jobclick` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) DEFAULT NULL,
  `job_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jobs_jobclick_job_id_ed6a0dd1_fk_jobs_job_id` (`job_id`),
  KEY `jobs_jobclick_user_id_b3ce1b83_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `jobs_jobclick_job_id_ed6a0dd1_fk_jobs_job_id` FOREIGN KEY (`job_id`) REFERENCES `jobs_job` (`id`),
  CONSTRAINT `jobs_jobclick_user_id_b3ce1b83_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_jobclick`
--

LOCK TABLES `jobs_jobclick` WRITE;
/*!40000 ALTER TABLE `jobs_jobclick` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobs_jobclick` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_resume`
--

DROP TABLE IF EXISTS `jobs_resume`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobs_resume` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `reuse` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jobs_resume_user_id_07ec7231_fk_account_myuser_id` (`user_id`),
  CONSTRAINT `jobs_resume_user_id_07ec7231_fk_account_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_resume`
--

LOCK TABLES `jobs_resume` WRITE;
/*!40000 ALTER TABLE `jobs_resume` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobs_resume` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_blacklist_blacklistedtoken`
--

DROP TABLE IF EXISTS `token_blacklist_blacklistedtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `token_blacklist_blacklistedtoken` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `blacklisted_at` datetime(6) NOT NULL,
  `token_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_id` (`token_id`),
  CONSTRAINT `token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk` FOREIGN KEY (`token_id`) REFERENCES `token_blacklist_outstandingtoken` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_blacklistedtoken`
--

LOCK TABLES `token_blacklist_blacklistedtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_blacklistedtoken` DISABLE KEYS */;
INSERT INTO `token_blacklist_blacklistedtoken` VALUES (1,'2024-05-01 12:22:30.242465',2),(2,'2024-05-20 14:21:19.242991',12),(3,'2024-05-20 14:45:32.328045',13),(4,'2024-05-21 08:46:08.176125',15),(5,'2024-05-31 09:14:58.413477',20),(6,'2024-07-01 06:56:16.900144',31),(7,'2024-07-01 09:14:05.996633',32),(8,'2024-07-17 06:38:31.861652',34),(9,'2024-07-18 09:13:52.566619',35),(10,'2024-07-23 04:48:40.498277',38),(11,'2024-07-23 09:13:13.799031',39),(12,'2024-07-23 09:58:09.696683',40),(13,'2024-07-26 04:34:55.168336',42),(14,'2024-08-03 06:32:15.041450',44),(15,'2024-08-12 11:31:10.634933',48),(16,'2024-08-12 16:02:43.250361',50),(17,'2024-08-12 16:06:39.089175',52),(18,'2024-08-12 16:09:01.809360',53),(19,'2024-08-12 18:05:32.326113',49),(20,'2024-08-14 05:33:12.576060',57),(21,'2024-08-14 07:21:27.435842',58),(22,'2024-08-14 08:46:58.688973',59),(23,'2024-08-14 09:30:31.752785',60),(24,'2024-08-14 09:45:53.964535',62),(25,'2024-08-14 10:09:05.208375',65),(26,'2024-08-14 10:21:30.834889',66),(27,'2024-08-15 19:09:35.566284',71);
/*!40000 ALTER TABLE `token_blacklist_blacklistedtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_blacklist_outstandingtoken`
--

DROP TABLE IF EXISTS `token_blacklist_outstandingtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `token_blacklist_outstandingtoken` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` longtext NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `expires_at` datetime(6) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `jti` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_uniq` (`jti`),
  KEY `token_blacklist_outs_user_id_83bc629a_fk_account_m` (`user_id`),
  CONSTRAINT `token_blacklist_outs_user_id_83bc629a_fk_account_m` FOREIGN KEY (`user_id`) REFERENCES `account_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_outstandingtoken`
--

LOCK TABLES `token_blacklist_outstandingtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_outstandingtoken` DISABLE KEYS */;
INSERT INTO `token_blacklist_outstandingtoken` VALUES (1,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzA4NTk1MCwiaWF0IjoxNzE0NDkzOTUwLCJqdGkiOiIwMGRjZjA3MTcwMmQ0OThiYTE4MjUwOTA0ODVhMTE0MyIsInVzZXJfaWQiOjEwfQ.6qGEiHRburTpYUAk-UI8-FTVwFGM3R0bt54K9qzbtoE','2024-04-30 16:19:10.324330','2024-05-30 16:19:10.000000',10,'00dcf071702d498ba1825090485a1143'),(2,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzE1NDQ3MCwiaWF0IjoxNzE0NTYyNDcwLCJqdGkiOiIzNzM2ODAzZTlmMDY0ZGE0YTdlMjA2Y2NiMTcyM2UwNSIsInVzZXJfaWQiOjExfQ.3PR8YMy-V9lkbl_V_-Hu1c_kwqzvBY3fLxdpalUgy0Y','2024-05-01 11:21:10.726506','2024-05-31 11:21:10.000000',11,'3736803e9f064da4a7e206ccb1723e05'),(3,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzc0ODc3NSwiaWF0IjoxNzE1MTU2Nzc1LCJqdGkiOiJiMTRhYWIyYmE3ZWY0YWMyOGM0YzdlMzdlMGRjZGVkNyIsInVzZXJfaWQiOjExfQ.RaiuANfeEH2tjK3yuBksYdd92SFjWcRO_Vf21w-goSA','2024-05-08 08:26:15.807086','2024-06-07 08:26:15.000000',11,'b14aab2ba7ef4ac28c4c7e37e0dcded7'),(4,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzc3MDQ3NiwiaWF0IjoxNzE1MTc4NDc2LCJqdGkiOiI3MWQ1MzFlMWFhMDU0YmRlYWZlYWNjOTMyNzk4YWNkMCIsInVzZXJfaWQiOjEzfQ.ucHkq2vaFKKjA_F0Al4u547O-X_HkoX7fdsxZvds4Ec','2024-05-08 14:27:56.497257','2024-06-07 14:27:56.000000',13,'71d531e1aa054bdeafeacc932798acd0'),(5,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzg1OTUzNiwiaWF0IjoxNzE1MjY3NTM2LCJqdGkiOiJhOGMwZDhiZjI0NDg0NzVhYWFhYWJhZGM5MmJmM2U0YSIsInVzZXJfaWQiOjE0fQ.PDQMQkNhlidWpaxNlpixD1OqwUsQAEV2bsV8P0HmTlU','2024-05-09 15:12:16.884083','2024-06-08 15:12:16.000000',14,'a8c0d8bf2448475aaaaabadc92bf3e4a'),(6,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzg1OTU2OSwiaWF0IjoxNzE1MjY3NTY5LCJqdGkiOiJlYTBmZGU2NWM1NDA0NmFlYmRlNWRhZjM2ZTU1M2FkNiIsInVzZXJfaWQiOjE0fQ.cl8RW_LoMEapXFah3-79A_K_WBvWyLXDVDAku55wd7Y','2024-05-09 15:12:49.677189','2024-06-08 15:12:49.000000',14,'ea0fde65c54046aebde5daf36e553ad6'),(7,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODMzNzM0MywiaWF0IjoxNzE1NzQ1MzQzLCJqdGkiOiJhM2QwMDMwZjIwZjU0NjAzOWNmNWE4ODFkOWI2OTAzNCIsInVzZXJfaWQiOjE1fQ.534cDQKZMOsM4iKkmRNiRrAwRmtV9ysDWiDJ3U-aBww','2024-05-15 03:55:43.258935','2024-06-14 03:55:43.000000',15,'a3d0030f20f546039cf5a881d9b69034'),(8,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODM1OTcxNywiaWF0IjoxNzE1NzY3NzE3LCJqdGkiOiJhZDEzNDhlNThhOTA0ZjllODNkZGY2ZTdlZDgwOGFlZiIsInVzZXJfaWQiOjEzfQ.0hnzO6chZ_xEd20mfIvj1PCK7Q8Z_EFKZXKP3pfsX_0','2024-05-15 10:08:37.964934','2024-06-14 10:08:37.000000',13,'ad1348e58a904f9e83ddf6e7ed808aef'),(9,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODQ3NDQyNiwiaWF0IjoxNzE1ODgyNDI2LCJqdGkiOiJlZGRlNDc0ZjYzMzA0NWFhYTE5ZjA0YTg5YTY5ODE5MyIsInVzZXJfaWQiOjE2fQ.EdWfjkBRJt6pH3sYW-QHoEoMAfwmDHqCN57kcvnauDc','2024-05-16 18:00:26.150230','2024-06-15 18:00:26.000000',16,'edde474f633045aaa19f04a89a698193'),(10,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODUyMzUzMCwiaWF0IjoxNzE1OTMxNTMwLCJqdGkiOiI4ZTdiNDM4OTdmNmU0NTRlODVjNmI4Y2Q0ZWRlNzA0NyIsInVzZXJfaWQiOjE1fQ.DKKRLMUmur2j6qkxpCH5Aj6MZQfdYyb8AGeWnB_GiYE','2024-05-17 07:38:50.592457','2024-06-16 07:38:50.000000',15,'8e7b43897f6e454e85c6b8cd4ede7047'),(11,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODcxMzIxMywiaWF0IjoxNzE2MTIxMjEzLCJqdGkiOiIyZjFhOTEwYWZkNzY0NjYxYjlmOWEwZDBmNDdkZDg4ZSIsInVzZXJfaWQiOjE0fQ.cTls_i_E0BAV6PiAISEJ1VPvuzN5ZgfUfLBBiaddZ0M','2024-05-19 12:20:13.610932','2024-06-18 12:20:13.000000',14,'2f1a910afd764661b9f9a0d0f47dd88e'),(12,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODgwMDc5MiwiaWF0IjoxNzE2MjA4NzkyLCJqdGkiOiI5YThlMzdkOGFhZmU0MzRlODIzZDA4OGE4MzUyNDVmYiIsInVzZXJfaWQiOjE1fQ.owPlYSMK5pYQNBGr_K1zk8rmoiKCP6T-_BvJeVvnm48','2024-05-20 12:39:52.004370','2024-06-19 12:39:52.000000',15,'9a8e37d8aafe434e823d088a835245fb'),(13,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODgwNzU5MywiaWF0IjoxNzE2MjE1NTkzLCJqdGkiOiIwNTA2NDdhYTc0MGU0YTQxYmQzYzBhNWE0MTNjMWY4OCIsInVzZXJfaWQiOjExfQ.ICDmbGcTCdyJ4CeJthE5oTq4meXKCIb1jV6lxcrdlpk','2024-05-20 14:33:13.331809','2024-06-19 14:33:13.000000',11,'050647aa740e4a41bd3c0a5a413c1f88'),(14,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODgwODM0MiwiaWF0IjoxNzE2MjE2MzQyLCJqdGkiOiJkMmRhNjc4Y2Q3MmI0ZGMyOTA3YmQ3YjYwNWU3NWYwNiIsInVzZXJfaWQiOjExfQ.Oorp7fhr5exYwHc-3XmH4amanpE2tatdd1p6R6GieVI','2024-05-20 14:45:42.987281','2024-06-19 14:45:42.000000',11,'d2da678cd72b4dc2907bd7b605e75f06'),(15,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODg3MjE2MiwiaWF0IjoxNzE2MjgwMTYyLCJqdGkiOiI3YTYzZWFkNWM0NjM0YzIwODI4MTFlNGVkYTVmYWQ2YSIsInVzZXJfaWQiOjExfQ.g3FvljFejOWVz7tlLT57FtL_Rbr4uHnCT95bQ-oPZ0A','2024-05-21 08:29:22.539731','2024-06-20 08:29:22.000000',11,'7a63ead5c4634c2082811e4eda5fad6a'),(16,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODg3MjE5OCwiaWF0IjoxNzE2MjgwMTk4LCJqdGkiOiIzZTdmZGU2ZjVjNzk0YjczODk2MGI2NDA0MDU4MjE5NyIsInVzZXJfaWQiOjE0fQ.vpdaqfc_DLReSDK9MbhvtxT73GnX2xPRsHMjTseYf3w','2024-05-21 08:29:58.116333','2024-06-20 08:29:58.000000',14,'3e7fde6f5c794b738960b64040582197'),(17,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODg3MzE3OSwiaWF0IjoxNzE2MjgxMTc5LCJqdGkiOiI1ZmZkY2NlOWNkMDE0MGE5OTJkZWNjYWZmMjY3MzE5YyIsInVzZXJfaWQiOjE1fQ.uW1-6nXxzbmuVMC_mDTFjX5tjGS6Zm2vN_QTuTCSprE','2024-05-21 08:46:19.730632','2024-06-20 08:46:19.000000',15,'5ffdcce9cd0140a992deccaff267319c'),(18,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxOTMyNDk0NiwiaWF0IjoxNzE2NzMyOTQ2LCJqdGkiOiIwMGUxYTMyMWM1OTc0YzFmOTYyYjE0ZGZiYzk3NGRiZiIsInVzZXJfaWQiOjE1fQ._O11KCflEdMT1edwkoq5lUE7npUHRByjGI9KAQF5OEA','2024-05-26 14:15:46.479343','2024-06-25 14:15:46.000000',15,'00e1a321c5974c1f962b14dfbc974dbf'),(19,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxOTQyNTc4MSwiaWF0IjoxNzE2ODMzNzgxLCJqdGkiOiIzOGE5MmFjZGYyNTc0YjJmYjU0ODU5M2RjNzQxMzM1NCIsInVzZXJfaWQiOjE0fQ.GndP0rs4jDk0sB79y_uzFGDQ84FZc8gh_m8CTyjW-tg','2024-05-27 18:16:21.337143','2024-06-26 18:16:21.000000',14,'38a92acdf2574b2fb548593dc7413354'),(20,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxOTczODUzMCwiaWF0IjoxNzE3MTQ2NTMwLCJqdGkiOiJhOWMwMTg5MzQ0M2U0N2NkOWIzZGUxNjg1NjIzNGE2NyIsInVzZXJfaWQiOjE1fQ.TFniIGI56jyeBBt49yrTaM3DWHtegCZDwGiMjTKu-40','2024-05-31 09:08:50.673221','2024-06-30 09:08:50.000000',15,'a9c01893443e47cd9b3de16856234a67'),(21,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxOTczODkwNSwiaWF0IjoxNzE3MTQ2OTA1LCJqdGkiOiI1YWUyMTAzY2Q2OTU0ZDY0YjY4ZWQ5MTFlYTU5ZmQ0ZiIsInVzZXJfaWQiOjExfQ.3VCLgDupt7-PnQsOunAwXkjoQe4rB0hXot4RT9kbIro','2024-05-31 09:15:05.625690','2024-06-30 09:15:05.000000',11,'5ae2103cd6954d64b68ed911ea59fd4f'),(22,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxOTc0MDQ0OCwiaWF0IjoxNzE3MTQ4NDQ4LCJqdGkiOiJhY2I3YjNlMjhjODg0YmE2YTQ3Y2RkYzBmNWVjZDY3ZiIsInVzZXJfaWQiOjExfQ.dKGfF24iz8tg7ZMdOkCX0lbCIrBPDSeZ7JAka9JXzFw','2024-05-31 09:40:48.350792','2024-06-30 09:40:48.000000',11,'acb7b3e28c884ba6a47cddc0f5ecd67f'),(23,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxOTc0MDc0MiwiaWF0IjoxNzE3MTQ4NzQyLCJqdGkiOiJmNjM5OWIyNjkwNWI0OTc1OWM2MTY2MTNlNTIwZjQxZiIsInVzZXJfaWQiOjExfQ.YsbhxcCjBPPIjFdjZ_O2as21ugLaBw9Ou6lrsxwykek','2024-05-31 09:45:42.503339','2024-06-30 09:45:42.000000',11,'f6399b26905b49759c616613e520f41f'),(24,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMDE3Mzg1MywiaWF0IjoxNzE3NTgxODUzLCJqdGkiOiJhODI1MjJiYzJlMDA0YWE0YmMwM2U0NWQyZDVhZWVmNyIsInVzZXJfaWQiOjE3fQ.l1TQmjN9boPt0pIhY914DF1_AMjZUxQjMfmFrsP8E0o','2024-06-05 10:04:13.728192','2024-07-05 10:04:13.000000',17,'a82522bc2e004aa4bc03e45d2d5aeef7'),(25,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMDE3NDU3NywiaWF0IjoxNzE3NTgyNTc3LCJqdGkiOiI0YjY1NjYyMzIzMDM0NjhiYWQ1NGJiMjNiMjQwYmUxYSIsInVzZXJfaWQiOjE3fQ.ET14NHyT0i5H2O-GdS1ugId-tdEcWz-ByCCMN2u-Q7A','2024-06-05 10:16:17.475643','2024-07-05 10:16:17.000000',17,'4b6566232303468bad54bb23b240be1a'),(26,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMDI0Njg0MywiaWF0IjoxNzE3NjU0ODQzLCJqdGkiOiI1NTFlZjdmZDMyMTA0Mzk2YTAyNjQwMTk2ZTI0YmE2ZiIsInVzZXJfaWQiOjE3fQ.8er0PZvHzK6G3YE_kPtL07IgaDKiGpVet5QmJlzV-tY','2024-06-06 06:20:43.101954','2024-07-06 06:20:43.000000',17,'551ef7fd32104396a02640196e24ba6f'),(27,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMTIyNjExNiwiaWF0IjoxNzE4NjM0MTE2LCJqdGkiOiJlMTljZmVmMWMwYTU0YzgwYjExOWNmNTM0YzcwMmM3NSIsInVzZXJfaWQiOjE4fQ.OtZ7-bMtlG3dJEZ3fWwIoi8Xl3u1YM_vsy8ZYu0Gt38','2024-06-17 14:21:56.738113','2024-07-17 14:21:56.000000',18,'e19cfef1c0a54c80b119cf534c702c75'),(28,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjAwNTQ0MiwiaWF0IjoxNzE5NDEzNDQyLCJqdGkiOiIzMGY3MGEzZGQ3N2Y0N2RlOTIxOGVjNjM4NWIzZTRiMCIsInVzZXJfaWQiOjE5fQ.PnubBerSIkIPuRrI276idKSLq-R8LHdCuII7vANvWYI','2024-06-26 14:50:42.821714','2024-07-26 14:50:42.000000',19,'30f70a3dd77f47de9218ec6385b3e4b0'),(29,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjA3Mjk0MywiaWF0IjoxNzE5NDgwOTQzLCJqdGkiOiJjMGUxMDQyMjI5ZDU0OTFhYTI4ZGU0OWMwYzhlMTY0NCIsInVzZXJfaWQiOjE5fQ.V8VSyEExcQHkvXmJJ58N1SEsJV9zi96ECkFDg_11DsI','2024-06-27 09:35:43.522625','2024-07-27 09:35:43.000000',19,'c0e1042229d5491aa28de49c0c8e1644'),(30,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjA3Mjk0NiwiaWF0IjoxNzE5NDgwOTQ2LCJqdGkiOiJhNTAyOTMyZmZlZjM0NGY4OWNhYmUxY2NhYWFjOWQyYyIsInVzZXJfaWQiOjE5fQ.iz0geiRuomabiP6YLg6iin6mrhu-XrapCAVECzwk6ho','2024-06-27 09:35:46.119983','2024-07-27 09:35:46.000000',19,'a502932ffef344f89cabe1ccaaac9d2c'),(31,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQwODg0OSwiaWF0IjoxNzE5ODE2ODQ5LCJqdGkiOiIyYmQxMWM3YTdhMTU0M2JkOWFkNjY3MTNhM2I3YzdhMyIsInVzZXJfaWQiOjE4fQ.qMbRgvt4bs6f3M0aXeG5Qc2TViY_GQxqamFbPFu9qaY','2024-07-01 06:54:09.637225','2024-07-31 06:54:09.000000',18,'2bd11c7a7a1543bd9ad66713a3b7c7a3'),(32,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQxNzE5OSwiaWF0IjoxNzE5ODI1MTk5LCJqdGkiOiIwMTA4NWFkYzM1NmU0NzcxODcwMjViYTAyZmYzY2Y4OSIsInVzZXJfaWQiOjExfQ.Ct707mR6ISWHnipiP98SECeWeb1iXsrttJnGvFSiM2s','2024-07-01 09:13:19.180388','2024-07-31 09:13:19.000000',11,'01085adc356e477187025ba02ff3cf89'),(33,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc4MTIyNywiaWF0IjoxNzIwMTg5MjI3LCJqdGkiOiIwNDUxOTFmYTRkNGE0OTU1YjJjMGUwZTM4M2ExMTMwNyIsInVzZXJfaWQiOjIwfQ.cj7fmPZuF4NbWOCkpXHkGyaOTkQ3grKwUGcnhbyp6AQ','2024-07-05 14:20:27.424127','2024-08-04 14:20:27.000000',20,'045191fa4d4a4955b2c0e0e383a11307'),(34,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzc4Mzk1MiwiaWF0IjoxNzIxMTkxOTUyLCJqdGkiOiJlYTE1MDJhZjFiZjI0ZDRmYjUzNmFlN2IyYjk3NDljMSIsInVzZXJfaWQiOjIxfQ.j6NxbIVsL9rwMereMb9ao6D_jUkENXD7KXkML78fLmY','2024-07-17 04:52:32.836061','2024-08-16 04:52:32.000000',21,'ea1502af1bf24d4fb536ae7b2b9749c1'),(35,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzg3NTA2OSwiaWF0IjoxNzIxMjgzMDY5LCJqdGkiOiI2ODRjMTc0ODQ3OGQ0YTVmOGM0M2UzNTJlZjFkNTkzYyIsInVzZXJfaWQiOjIxfQ.57TZE02XWChRqCjxXuLokzQkIvDFM-yUsJoBE8C6fQk','2024-07-18 06:11:09.203561','2024-08-17 06:11:09.000000',21,'684c1748478d4a5f8c43e352ef1d593c'),(36,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzg5MzUxNSwiaWF0IjoxNzIxMzAxNTE1LCJqdGkiOiIzM2NkYzI1MTM3NGM0YTRhOTliMzczNmRhZWY2YTM1ZSIsInVzZXJfaWQiOjIyfQ.JYMInQFrbF5lNx3dn9lQq4FfawBU1utDVNkMX-cFnsE','2024-07-18 11:18:35.199970','2024-08-17 11:18:35.000000',22,'33cdc251374c4a4a99b3736daef6a35e'),(37,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDIxMzU5MSwiaWF0IjoxNzIxNjIxNTkxLCJqdGkiOiJiMmM3YTUxZDkyZDk0NmU5YmM1MjQ2YmQwN2U2ZTAzYSIsInVzZXJfaWQiOjIzfQ.W-Lk6IAflyLvVu66JFyNBRLAK3hZBrtklhWNJ7wZ1gM','2024-07-22 04:13:11.513282','2024-08-21 04:13:11.000000',23,'b2c7a51d92d946e9bc5246bd07e6e03a'),(38,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDI0MTUwNSwiaWF0IjoxNzIxNjQ5NTA1LCJqdGkiOiIyNTkxY2YyNDYyNDU0MWVlYTExNmQ3Mzk4NzhkNmQwYiIsInVzZXJfaWQiOjIyfQ.alcYC_goXrrhMY8vqywbQMcyWO_BM7vV7LIE32xoHys','2024-07-22 11:58:25.137418','2024-08-21 11:58:25.000000',22,'2591cf24624541eea116d739878d6d0b'),(39,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDMwMjM1OCwiaWF0IjoxNzIxNzEwMzU4LCJqdGkiOiIwMzk2NTJmZDc0ZGU0YWVkYTk1NWQ4ZTg5NjMyZWEzZiIsInVzZXJfaWQiOjIxfQ.vFg-8SmDeTduv6AJxLxNzYQ1FzC-fCeYxXGECCC1-FM','2024-07-23 04:52:38.010496','2024-08-22 04:52:38.000000',21,'039652fd74de4aeda955d8e89632ea3f'),(40,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDMyMDU5NywiaWF0IjoxNzIxNzI4NTk3LCJqdGkiOiIwOWEyZDhiMTdhMzY0MWI4OGFjZDI5Y2ExMTY2NWNiYSIsInVzZXJfaWQiOjIxfQ.R36x1k86VTZ12WTmiP0XyU3OKtaAkN4PVhuqGDgQuKM','2024-07-23 09:56:37.142755','2024-08-22 09:56:37.000000',21,'09a2d8b17a3641b88acd29ca11665cba'),(41,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDMyMDY5NiwiaWF0IjoxNzIxNzI4Njk2LCJqdGkiOiI5YjNlNTc1ZjIyZjE0YWJhYTk2OTg0Y2M5OWU1MmNlOSIsInVzZXJfaWQiOjIyfQ.928g0sX48tYt5mAROKuGZ442NFKMcuFNL7mQlXDKy9M','2024-07-23 09:58:16.213933','2024-08-22 09:58:16.000000',22,'9b3e575f22f14abaa96984cc99e52ce9'),(42,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDQ4OTQ4MCwiaWF0IjoxNzIxODk3NDgwLCJqdGkiOiI3MjlkYTc4M2NlMGE0YjZmYmNlZDQ2M2U1YTY0YzlkNCIsInVzZXJfaWQiOjI0fQ.gZbLKoZ1olzi5gn54PsZ8WJhY64WCABW7tVHkjglwN4','2024-07-25 08:51:20.293433','2024-08-24 08:51:20.000000',24,'729da783ce0a4b6fbced463e5a64c9d4'),(43,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTAzNzUxMywiaWF0IjoxNzIyNDQ1NTEzLCJqdGkiOiI1ZDVhOGQzODQxZWE0M2U0YWU1ZjA0N2I0NzBmYjY5NiIsInVzZXJfaWQiOjI1fQ.YYZ1FpUObgtGZ-5Hl6FPxux6E0kPufoCwhBwTbh7dYc','2024-07-31 17:05:13.181155','2024-08-30 17:05:13.000000',25,'5d5a8d3841ea43e4ae5f047b470fb696'),(44,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTI1ODU0MiwiaWF0IjoxNzIyNjY2NTQyLCJqdGkiOiJjYjZiNDJlMjVmMDc0ZWQ0YjNiNWNiNWJmZTQwMzhmOCIsInVzZXJfaWQiOjIzfQ.bDs5Ghx3pxVDrsvRnii1FBVlqKXJL2d1Cfi0YuxJUys','2024-08-03 06:29:02.061317','2024-09-02 06:29:02.000000',23,'cb6b42e25f074ed4b3b5cb5bfe4038f8'),(45,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTMxMjU0MSwiaWF0IjoxNzIyNzIwNTQxLCJqdGkiOiJiYzRjMGExNmZmZDY0YjZkYjcxZmMwODNkODI2ODc5NiIsInVzZXJfaWQiOjI1fQ.7LaGTy3RJ6cAw5unrkDczojHxmMwHQohsW3R_omA46E','2024-08-03 21:29:01.177688','2024-09-02 21:29:01.000000',25,'bc4c0a16ffd64b6db71fc083d8268796'),(46,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTMxMjU0MSwiaWF0IjoxNzIyNzIwNTQxLCJqdGkiOiIxNjI2ODQ3MDVhMDM0ZjFiOTg4OWJhZWM3OWE0MTg5ZSIsInVzZXJfaWQiOjI1fQ.ZhrHLu0XHloYnMzG9BYRw7cVkvhnCiX8YMybu9fIjnA','2024-08-03 21:29:01.896633','2024-09-02 21:29:01.000000',25,'162684705a034f1b9889baec79a4189e'),(47,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTk5NzU4MywiaWF0IjoxNzIzNDA1NTgzLCJqdGkiOiJlZWNlNWQ0NzFlNjE0YjVjYjQzZjNjMDg4ZTViNTIyYyIsInVzZXJfaWQiOjE5fQ.OYIQYg86VVhFJnjvPyaXGPzqaJV32CoW7tsh7xJOiZc','2024-08-11 19:46:23.051309','2024-09-10 19:46:23.000000',19,'eece5d471e614b5cb43f3c088e5b522c'),(48,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjA1MjQ3MSwiaWF0IjoxNzIzNDYwNDcxLCJqdGkiOiI1YzZkZTM2MTYyNDc0Mzk2YTgyNGQxYzJkZDljYjBmNiIsInVzZXJfaWQiOjIxfQ.mvCSlN72J0OOSP6rSvuTqWM8BH5UJtsMkN-lxMLaH1o','2024-08-12 11:01:11.109279','2024-09-11 11:01:11.000000',21,'5c6de36162474396a824d1c2dd9cb0f6'),(49,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjA2OTI0NywiaWF0IjoxNzIzNDc3MjQ3LCJqdGkiOiIwNWNjNTc4ZjI2Yzc0MDNlOTA2MjcxNDZhNTVjODExOSIsInVzZXJfaWQiOjExfQ.Ej5SHsElg-29ClF9lNI9LpDiDGWWeHtRB6B58QHliI4','2024-08-12 15:40:47.421351','2024-09-11 15:40:47.000000',11,'05cc578f26c7403e90627146a55c8119'),(50,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjA2OTI1MywiaWF0IjoxNzIzNDc3MjUzLCJqdGkiOiIxNjU4MmQ0MGEwODk0MjQzODMyMjM2MjM1OTJlM2MzMyIsInVzZXJfaWQiOjE5fQ.lGv5mJXaYjmeiTy_1PiHRZH3RLM9wUBStn9uDrlwh1s','2024-08-12 15:40:53.293708','2024-09-11 15:40:53.000000',19,'16582d40a089424383223623592e3c33'),(51,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjA2OTI4MywiaWF0IjoxNzIzNDc3MjgzLCJqdGkiOiJmMzJmMzRiYjY2MjA0M2EzYmVjZThmYjI1NjAyOThlZCIsInVzZXJfaWQiOjI3fQ.9KLnT4lIvzpLDSMo6Chk2QR12_8-NDIZgGVHlwwEkWE','2024-08-12 15:41:23.314446','2024-09-11 15:41:23.000000',27,'f32f34bb662043a3bece8fb2560298ed'),(52,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjA3MDYzMywiaWF0IjoxNzIzNDc4NjMzLCJqdGkiOiIyMDBkN2VmYzhkZWY0ZTk0Yjk1NjMwNjA5MzVmN2YzNCIsInVzZXJfaWQiOjE5fQ.pIOr6xaPOhZXltWnSQ_Z6aXrJoREISyWJhwCLLjyG-Y','2024-08-12 16:03:53.845292','2024-09-11 16:03:53.000000',19,'200d7efc8def4e94b9563060935f7f34'),(53,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjA3MDgzOSwiaWF0IjoxNzIzNDc4ODM5LCJqdGkiOiJkYzhiYjQwY2VjZTI0OGFkYjAyODFiZGQyMTJiMDAxZCIsInVzZXJfaWQiOjE5fQ.-oc0A25i3GN4dQuAxG5MRks-rEhifZ6K1FAQkZs3_fM','2024-08-12 16:07:19.827788','2024-09-11 16:07:19.000000',19,'dc8bb40cece248adb0281bdd212b001d'),(54,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjA3MTg4NywiaWF0IjoxNzIzNDc5ODg3LCJqdGkiOiI1YjRkNzFhN2FhMzE0ZTlhODJjOGUzYjZjZGU5NDczMCIsInVzZXJfaWQiOjE5fQ.eUAhKpBP6sXcXBu7wDQ_9TlX569NmcW7sjaSRI4ALKY','2024-08-12 16:24:47.256439','2024-09-11 16:24:47.000000',19,'5b4d71a7aa314e9a82c8e3b6cde94730'),(55,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjEyMjMxMiwiaWF0IjoxNzIzNTMwMzEyLCJqdGkiOiJjMGI0NDFkYjFkNWI0MWFhOWJmMmQ4NmEyYzRhYmVlMSIsInVzZXJfaWQiOjE5fQ.ZDIbKRetqFit8NDCKiRl3En-1dwneqXgkXeX_w8qcbQ','2024-08-13 06:25:12.244560','2024-09-12 06:25:12.000000',19,'c0b441db1d5b41aa9bf2d86a2c4abee1'),(56,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjEzMTYwNCwiaWF0IjoxNzIzNTM5NjA0LCJqdGkiOiIzMGUxNGZkYWUzNDk0MGQwODViY2FlYTc5NWMxZWFiMiIsInVzZXJfaWQiOjIxfQ.8j2H7DxnFyWUcQF56V1DGB2lXpiBkHzKsV5ULiIjLpQ','2024-08-13 09:00:04.401801','2024-09-12 09:00:04.000000',21,'30e14fdae34940d085bcaea795c1eab2'),(57,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjIwNTMyMiwiaWF0IjoxNzIzNjEzMzIyLCJqdGkiOiJkNGMxYTVjMmExODI0MWY2OTkxNTc5YzcxNTc5MDZjYyIsInVzZXJfaWQiOjIxfQ.Z7qyvBVJAmi_bBnkCFBeDrubQpMRTmQfyJTcz_jFTF8','2024-08-14 05:28:42.292364','2024-09-13 05:28:42.000000',21,'d4c1a5c2a18241f6991579c7157906cc'),(58,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjIxMTk3NSwiaWF0IjoxNzIzNjE5OTc1LCJqdGkiOiJmYWEzYmU5OWUyOWY0MDE0YWJmZmNhNmNhOWJmNjMxNyIsInVzZXJfaWQiOjIxfQ.S3EOiE68ReFABw_cFloWSmfJGgeioEHTUs_lzaB-JnY','2024-08-14 07:19:35.309383','2024-09-13 07:19:35.000000',21,'faa3be99e29f4014abffca6ca9bf6317'),(59,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjIxNzEzMywiaWF0IjoxNzIzNjI1MTMzLCJqdGkiOiI0YTkwNTVhZjE2ZjA0NGVkYTVkYmZiN2ViMDgzNjBjNSIsInVzZXJfaWQiOjMwfQ.7a8iHdW-BxfV4TmyCyFTQcgQMZCGJaPHH2RuAZ4Fads','2024-08-14 08:45:33.520791','2024-09-13 08:45:33.000000',30,'4a9055af16f044eda5dbfb7eb08360c5'),(60,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjIxODE0OCwiaWF0IjoxNzIzNjI2MTQ4LCJqdGkiOiIyODI0M2NiY2VhZDY0MzMwYTM3ODg2NDI0ZjczZTE3ZCIsInVzZXJfaWQiOjMwfQ.iEqRQ2f9BahmdJ9KY8q77675huYnKOtacDOLk1r1bEQ','2024-08-14 09:02:28.621819','2024-09-13 09:02:28.000000',30,'28243cbcead64330a37886424f73e17d'),(61,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjIyMDQwNCwiaWF0IjoxNzIzNjI4NDA0LCJqdGkiOiI1OWE2ODVjNGE2YmI0ZTAxOGM4Mzc0ZGVlOGVlYzAyYSIsInVzZXJfaWQiOjI0fQ.gAok8uBIrkF3F1ZfXkTDN6Rx72YPsq5k0xNJ_CJW5Bs','2024-08-14 09:40:04.612939','2024-09-13 09:40:04.000000',24,'59a685c4a6bb4e018c8374dee8eec02a'),(62,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjIyMDQ2NiwiaWF0IjoxNzIzNjI4NDY2LCJqdGkiOiJjMTVkY2FiZTI1MWU0NDUxYTI3OGU3MzdiOTE0NDljNCIsInVzZXJfaWQiOjMwfQ.H0MhNKUEtQLrE9bM3QxzFdwGa6hQwxQQUVzSj6WfmaY','2024-08-14 09:41:06.335973','2024-09-13 09:41:06.000000',30,'c15dcabe251e4451a278e737b91449c4'),(63,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjIyMDcwNCwiaWF0IjoxNzIzNjI4NzA0LCJqdGkiOiI1Njg4MjE1MDM0NWU0NjgzYjgwZTM2Y2IwMDc4Y2Q1YiIsInVzZXJfaWQiOjIxfQ.wj7L2l8bT1eYxjHqSXO029XUbA_NoNu_uy6jnlELRFY','2024-08-14 09:45:04.748507','2024-09-13 09:45:04.000000',21,'56882150345e4683b80e36cb0078cd5b'),(64,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjIyMDcwNSwiaWF0IjoxNzIzNjI4NzA1LCJqdGkiOiJhYjE0ZDEyOTVlNTc0ZGRjYjE3ZmYxZjY3Y2ZhYWMyNiIsInVzZXJfaWQiOjIxfQ.srzMWTPa_3bHx9V6j67Sv3s_KZVKH35C3VnrD4QYAHQ','2024-08-14 09:45:05.019392','2024-09-13 09:45:05.000000',21,'ab14d1295e574ddcb17ff1f67cfaac26'),(65,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjIyMTI3MCwiaWF0IjoxNzIzNjI5MjcwLCJqdGkiOiJlNjUxOGM2YmYxZjc0OWE4OGQxNDZkN2I1Mjk3ZWRjOSIsInVzZXJfaWQiOjM1fQ.XGgrFCab-bUY1im4pifzQH-HEak7rxe3xp3ZYRYPQaI','2024-08-14 09:54:30.188998','2024-09-13 09:54:30.000000',35,'e6518c6bf1f749a88d146d7b5297edc9'),(66,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjIyMjE0OSwiaWF0IjoxNzIzNjMwMTQ5LCJqdGkiOiIxY2RkMjE0OTc4ZGM0ODllYjU2OTk1N2ZkNzYxNWQzZCIsInVzZXJfaWQiOjM1fQ.UnXyxIas-JonvuonpFOkFX6d4507J3o7w95Zhbdq9Hc','2024-08-14 10:09:09.173155','2024-09-13 10:09:09.000000',35,'1cdd214978dc489eb569957fd7615d3d'),(67,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjI1NDY5MywiaWF0IjoxNzIzNjYyNjkzLCJqdGkiOiI0MmMwNWIxOTVkNTA0YmQ1YjJjNWY0ZGRhNDJiMjkzNyIsInVzZXJfaWQiOjI1fQ.vxvlebuwRSYrH--s2jSNFtDQnM2tQCpDK3RHVvDYX1A','2024-08-14 19:11:33.752888','2024-09-13 19:11:33.000000',25,'42c05b195d504bd5b2c5f4dda42b2937'),(68,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjI1NDc5NywiaWF0IjoxNzIzNjYyNzk3LCJqdGkiOiI4MmQ4MzVkOGRiOWI0YmZjODgxNDcwN2U2ZWM5YTAwOSIsInVzZXJfaWQiOjE5fQ.mtkhZa7DgxTrJWWS2npHy_HRtSaWEqDyfyCYwhpM6rE','2024-08-14 19:13:17.389301','2024-09-13 19:13:17.000000',19,'82d835d8db9b4bfc8814707e6ec9a009'),(69,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjI1NDkxMCwiaWF0IjoxNzIzNjYyOTEwLCJqdGkiOiJkMTdlNWJhYmI5NzA0ZGRiODdkYTNmY2IzNzJhZjQyNyIsInVzZXJfaWQiOjE5fQ.H8Rm-cXZR4ec-6G_1dqGBPcB6hI2YUgqLHUj1F19OMc','2024-08-14 19:15:10.209838','2024-09-13 19:15:10.000000',19,'d17e5babb9704ddb87da3fcb372af427'),(70,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjI1NDk4NywiaWF0IjoxNzIzNjYyOTg3LCJqdGkiOiI2OTNiZTMzNWY1MzE0ODJhYTZkY2U0YzQ1ZTI5MjMzOCIsInVzZXJfaWQiOjE5fQ.836joA_WUgVkCY40OrMrmSFbV1dwLtxdN2LNDrTUe_Q','2024-08-14 19:16:27.428393','2024-09-13 19:16:27.000000',19,'693be335f531482aa6dce4c45e292338'),(71,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjMwOTUwNiwiaWF0IjoxNzIzNzE3NTA2LCJqdGkiOiIzZmYyZjQwNjYyNzY0OWNkYjZmYjAwOTc0Zjk3ZjJhOCIsInVzZXJfaWQiOjExfQ.vUUb4ktZoQLDjKy5PXPUYA6USFwFR7AbuNzbmuzx_4Q','2024-08-15 10:25:06.577574','2024-09-14 10:25:06.000000',11,'3ff2f406627649cdb6fb00974f97f2a8'),(72,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjMwOTU2MywiaWF0IjoxNzIzNzE3NTYzLCJqdGkiOiIxYTM4YjdlYzg3MTA0ODg5YTVhZjA5Mjc4ZmVjMTQzZCIsInVzZXJfaWQiOjExfQ.83vhNgUx_zRbJbf9kXbzbROALmdSK_gJtr2gqQvKLDA','2024-08-15 10:26:03.054025','2024-09-14 10:26:03.000000',11,'1a38b7ec87104889a5af09278fec143d'),(73,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjcxMjc2OCwiaWF0IjoxNzI0MTIwNzY4LCJqdGkiOiJhYjQ0ZGRjNzZhMDU0OWUwYjJlNTk0NzIyNDcwZTUzNyIsInVzZXJfaWQiOjI1fQ.BRNsfC632sFfiZsH1zhihUovvI8-O--BDcNcUVNhvN8','2024-08-20 02:26:08.367457','2024-09-19 02:26:08.000000',25,'ab44ddc76a0549e0b2e594722470e537'),(74,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjgxOTE2MiwiaWF0IjoxNzI0MjI3MTYyLCJqdGkiOiJmMjcyYTdjMDc3MDM0ZWU0OWViMDk3YjFlNmZjMjI0YSIsInVzZXJfaWQiOjI1fQ.ECDueXIWckPXmpG0YKW0kWGjT5LbWB-5SyPl2D6F0ts','2024-08-21 07:59:22.725152','2024-09-20 07:59:22.000000',25,'f272a7c077034ee49eb097b1e6fc224a'),(75,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjgyNTExNSwiaWF0IjoxNzI0MjMzMTE1LCJqdGkiOiJlYzc5ZTVlY2I0MWM0MDVhODc3NTAyOTllMjFmMjdhNiIsInVzZXJfaWQiOjI1fQ.iOSXQxHo8hsE6q47ULtEl5671yAmrrPTFzoBoWKJA3E','2024-08-21 09:38:35.025097','2024-09-20 09:38:35.000000',25,'ec79e5ecb41c405a87750299e21f27a6'),(76,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjk0NDM4MCwiaWF0IjoxNzI0MzUyMzgwLCJqdGkiOiI0OGNmOGEwNzRmMjU0ZDliYjJmMjM2ODY5NTg0YjE0MyIsInVzZXJfaWQiOjE5fQ.F9FxQGUrcHCVHW8ZRQ25wQLRnk-YfaE7thUAsMvtS5k','2024-08-22 18:46:20.898793','2024-09-21 18:46:20.000000',19,'48cf8a074f254d9bb2f236869584b143');
/*!40000 ALTER TABLE `token_blacklist_outstandingtoken` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-03  8:06:27
