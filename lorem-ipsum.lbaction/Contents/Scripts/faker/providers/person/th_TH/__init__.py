from collections import OrderedDict

from .. import Provider as PersonProvider


class Provider(PersonProvider):
    # weights are arbitrarily assigned
    formats_female = OrderedDict((
        ('{{first_name_female}} {{last_name}}', 0.97),
        ('{{prefix_female}}{{first_name_female}} {{last_name}}', 0.015),
        ('{{first_name_female}} {{last_name}} {{suffix_female}}', 0.001),
        ('{{prefix_female}}{{first_name_female}} {{last_name}} {{suffix}}', 0.001),
    ))
    formats_male = OrderedDict((
        ('{{first_name_male}} {{last_name}}', 0.97),
        ('{{prefix_male}}{{first_name_male}} {{last_name}}', 0.015),
        ('{{first_name_male}} {{last_name}} {{suffix_male}}', 0.001),
        ('{{prefix_male}}{{first_name_male}} {{last_name}} {{suffix}}', 0.001),
    ))
    formats_nonbinary = OrderedDict((
        ('{{first_name_nonbinary}} {{last_name}}', 0.97),
        ('{{prefix_nonbinary}}{{first_name_nonbinary}} {{last_name}}', 0.015),
        ('{{first_name_nonbinary}} {{last_name}} {{suffix_nonbinary}}', 0.001),
        ('{{prefix_nonbinary}}{{first_name_nonbinary}} {{last_name}} {{suffix}}', 0.001),
    ))

    # Thai prefix, adapted from
    # http://www.stou.ac.th/thai/grad_stdy/Apply/prefix.asp
    # weights are arbitrarily assigned
    prefixes_female = OrderedDict((
        ("นาง", 0.3),
        ("น.ส.", 0.2),
        ("นางสาว", 0.15),
        ("ด.ญ.", 0.15),
        ("เด็กหญิง", 0.05),
        ("จ.ต.", 0.001),
        ("จ.ท.", 0.001),
        ("จ.ส.ต.", 0.001),
        ("จ.ส.ท.", 0.001),
        ("จ.ส.อ.", 0.001),
        ("จ.อ.", 0.001),
        ("ด.ต.", 0.001),
        ("น.ต.", 0.001),
        ("น.ท.", 0.001),
        ("น.อ.", 0.001),
        ("พ.จ.ต.", 0.001),
        ("พ.จ.ท.", 0.001),
        ("พ.จ.อ.", 0.001),
        ("พ.ต.", 0.001),
        ("พ.ต.ต.", 0.001),
        ("พ.ต.ท.", 0.001),
        ("พ.ต.อ.", 0.001),
        ("พ.ท.", 0.001),
        ("พ.อ.", 0.001),
        ("พ.อ.ต.", 0.001),
        ("พ.อ.ท.", 0.001),
        ("พ.อ.อ.", 0.001),
        ("ร.ต.", 0.001),
        ("ร.ต.ต.", 0.001),
        ("ร.ต.ท.", 0.001),
        ("ร.ต.อ.", 0.001),
        ("ร.ท.", 0.001),
        ("ร.อ.", 0.001),
        ("ส.ต.", 0.001),
        ("ส.ต.ต.", 0.001),
        ("ส.ต.ท.", 0.001),
        ("ส.ต.อ.", 0.001),
        ("ส.ท.", 0.001),
        ("ส.อ.", 0.001),
        ("พล.ต.", 0.0001),
        ("พล.ต.ต.", 0.0001),
        ("พล.ต.ท.", 0.0001),
        ("พล.ต.อ.", 0.0001),
        ("พล.ท.", 0.0001),
        ("พล.ร.ต.", 0.0001),
        ("พล.ร.ท.", 0.0001),
        ("พล.ร.อ.", 0.0001),
        ("พล.อ.", 0.0001),
        ("พล.อ.ต.", 0.0001),
        ("พล.อ.ท.", 0.0001),
        ("พล.อ.อ.", 0.0001),
        ("ม.ร.ว.", 0.0001),
        ("ม.ล.", 0.0001),
        ("หม่อมราชวงศ์", 0.0001),
        ("หม่อมหลวง", 0.0001),
    ))
    prefixes_male = OrderedDict((
        ("นาย", 0.6),
        ("ด.ช.", 0.3),
        ("จ.ต.", 0.001),
        ("จ.ท.", 0.001),
        ("จ.ส.ต.", 0.001),
        ("จ.ส.ท.", 0.001),
        ("จ.ส.อ.", 0.001),
        ("จ.อ.", 0.001),
        ("ด.ต.", 0.001),
        ("น.ต.", 0.001),
        ("น.ท.", 0.001),
        ("น.อ.", 0.001),
        ("พ.จ.ต.", 0.001),
        ("พ.จ.ท.", 0.001),
        ("พ.จ.อ.", 0.001),
        ("พ.ต.", 0.001),
        ("พ.ต.ต.", 0.001),
        ("พ.ต.ท.", 0.001),
        ("พ.ต.อ.", 0.001),
        ("พ.ท.", 0.001),
        ("พ.อ.", 0.001),
        ("พ.อ.ต.", 0.001),
        ("พ.อ.ท.", 0.001),
        ("พ.อ.อ.", 0.001),
        ("ร.ต.", 0.001),
        ("ร.ต.ต.", 0.001),
        ("ร.ต.ท.", 0.001),
        ("ร.ต.อ.", 0.001),
        ("ร.ท.", 0.001),
        ("ร.อ.", 0.001),
        ("ส.ต.", 0.001),
        ("ส.ต.ต.", 0.001),
        ("ส.ต.ท.", 0.001),
        ("ส.ต.อ.", 0.001),
        ("ส.ท.", 0.001),
        ("ส.อ.", 0.001),
        ("พล.ต.", 0.0001),
        ("พล.ต.ต.", 0.0001),
        ("พล.ต.ท.", 0.0001),
        ("พล.ต.อ.", 0.0001),
        ("พล.ท.", 0.0001),
        ("พล.ร.ต.", 0.0001),
        ("พล.ร.ท.", 0.0001),
        ("พล.ร.อ.", 0.0001),
        ("พล.อ.", 0.0001),
        ("พล.อ.ต.", 0.0001),
        ("พล.อ.ท.", 0.0001),
        ("พล.อ.อ.", 0.0001),
        ("ม.ร.ว.", 0.0001),
        ("ม.ล.", 0.0001),
        ("หม่อมราชวงศ์", 0.0001),
        ("หม่อมหลวง", 0.0001),
        ("พระ", 0.0001),
        ("สามเณร", 0.001),
        ("พระครูธรรมธร", 0.00001),
        ("พระครูปลัด", 0.00001),
        ("พระครูวินัยธร", 0.00001),
        ("พระครูสมุห์", 0.00001),
        ("พระครูใบฎีกา", 0.00001),
        ("พระปลัด", 0.00001),
        ("พระมหา", 0.00001),
        ("พระสมุห์", 0.00001),
        ("พระอธิการ", 0.00001),
        ("พระใบฎีกา", 0.00001),
        ("เจ้าอธิการ", 0.00001),
    ))
    prefixes_nonbinary = OrderedDict((
        ("จ.ต.", 0.001),
        ("จ.ท.", 0.001),
        ("จ.ส.ต.", 0.001),
        ("จ.ส.ท.", 0.001),
        ("จ.ส.อ.", 0.001),
        ("จ.อ.", 0.001),
        ("ด.ต.", 0.001),
        ("น.ต.", 0.001),
        ("น.ท.", 0.001),
        ("น.อ.", 0.001),
        ("พ.จ.ต.", 0.001),
        ("พ.จ.ท.", 0.001),
        ("พ.จ.อ.", 0.001),
        ("พ.ต.", 0.001),
        ("พ.ต.ต.", 0.001),
        ("พ.ต.ท.", 0.001),
        ("พ.ต.อ.", 0.001),
        ("พ.ท.", 0.001),
        ("พ.อ.", 0.001),
        ("พ.อ.ต.", 0.001),
        ("พ.อ.ท.", 0.001),
        ("พ.อ.อ.", 0.001),
        ("ร.ต.", 0.001),
        ("ร.ต.ต.", 0.001),
        ("ร.ต.ท.", 0.001),
        ("ร.ต.อ.", 0.001),
        ("ร.ท.", 0.001),
        ("ร.อ.", 0.001),
        ("ส.ต.", 0.001),
        ("ส.ต.ต.", 0.001),
        ("ส.ต.ท.", 0.001),
        ("ส.ต.อ.", 0.001),
        ("ส.ท.", 0.001),
        ("ส.อ.", 0.001),
        ("พล.ต.", 0.0001),
        ("พล.ต.ต.", 0.0001),
        ("พล.ต.ท.", 0.0001),
        ("พล.ต.อ.", 0.0001),
        ("พล.ท.", 0.0001),
        ("พล.ร.ต.", 0.0001),
        ("พล.ร.ท.", 0.0001),
        ("พล.ร.อ.", 0.0001),
        ("พล.อ.", 0.0001),
        ("พล.อ.ต.", 0.0001),
        ("พล.อ.ท.", 0.0001),
        ("พล.อ.อ.", 0.0001),
        ("ม.ร.ว.", 0.0001),
        ("ม.ล.", 0.0001),
        ("หม่อมราชวงศ์", 0.0001),
        ("หม่อมหลวง", 0.0001),
    ))

    prefixes = prefixes_female.copy()
    prefixes.update(prefixes_male)

    prefixes_nonbinary = prefixes.copy()

    # get 250 female names and 250 male names randomly
    # (with approximate fair distribution of length) from
    # https://github.com/PyThaiNLP/pythainlp/blob/dev/pythainlp/corpus/person_names_female_th.txt
    # https://github.com/PyThaiNLP/pythainlp/blob/dev/pythainlp/corpus/person_names_male_th.txt
    first_names_female = (
        "กนกเนตร",
        "กวาง",
        "กองสิน",
        "กะดิรัตน์",
        "กันตวรรณ",
        "กิ่งแก้ว",
        "กิติกานต์",
        "กิติยาธรณ์",
        "กุลปรียา",
        "กุลภาวลัย",
        "เกศรา",
        "เกษรา",
        "แกมแพร",
        "ใกล้รุ่ง",
        "ขอดิเยาะ",
        "เขมจิรา",
        "คณภรณ์",
        "คมคาย",
        "คำ",
        "จณิตตา",
        "จณิสตา",
        "จรรยพร",
        "จริยฉัตร",
        "จักรีรัตน์",
        "จันทนา",
        "จันทภา",
        "จิณภัทตา",
        "จิตตานันท์",
        "จิตรลดา",
        "จินต์จุฑา",
        "จิราภรณ์",
        "จิฬาภรณ์",
        "จีราภรณ์",
        "จุฑาภรณ์",
        "จุฑารัตน์",
        "ฉัตรปรียา",
        "ชนิศา",
        "ชรินทร์ทิพย์",
        "ชลิดา",
        "ชัญญานุนาย",
        "ชัฎชา",
        "ชิดชนก",
        "ซูรัยดา",
        "ซูไรดา",
        "ซูฮัยดา",
        "ฐิตาพร",
        "ฐิติกุล",
        "ฐิติณัฐฐา",
        "ฐิติยาพร",
        "ณภัทร",
        "ณัฐญาดา",
        "ณัฐติญา",
        "ณัฐธภรณ์",
        "ณัฐธิตา",
        "ณัฐพิชา",
        "ณัฐวรินทร",
        "ณาร์รีมาน",
        "ณิชนันท์",
        "ณิชาภัทร",
        "ดวงจันทร์",
        "ดวงพร",
        "ดวงสมร",
        "ดารุนี",
        "ตรีนุช",
        "ทองสิริ",
        "ทับทิม",
        "ทานตะวัน",
        "ทินพร",
        "ทิพย์วารี",
        "ทิพรดา",
        "ทิมาภรณ์",
        "เทพนารี",
        "ธมลพรรณ",
        "ธัชญา",
        "ธัญญกัญญา",
        "ธัญญามาศ",
        "ธีริสรา",
        "นพรัตน์",
        "นพวรรณ",
        "นภัสรินทร์",
        "นราวรรณ",
        "นรีกานต์",
        "นรีรัตน์",
        "นวรรษนันท์",
        "นันทวรรณ",
        "นันทิกานต์",
        "นาตยา",
        "นารดา",
        "นาวีตา",
        "น้ำเพชร",
        "นิติยา",
        "นิภา",
        "นิวิลดาน",
        "นุจรี",
        "เนตรฤดี",
        "บุญทิวา",
        "บุญเทียน",
        "บุญพา",
        "เบญญาทิพย์",
        "ปฐวีกานต์",
        "ปภาวรินทร์",
        "ประจิน",
        "ประไพพักตร์",
        "ประภัทร์สรณ์",
        "ปริญญา",
        "ปัญญาพร",
        "ปัณณธร",
        "ปาริตา",
        "ปิ่นบุญญา",
        "ปิยนาฎ",
        "ปิยนุช",
        "ปิยวดี",
        "ปิยะชาติ",
        "ผกาทิพย์",
        "พชรภรณ์",
        "พรชนก",
        "พรชีวิน",
        "พรเบญญา",
        "พรปราณี",
        "พรพิไล",
        "พรรณปพร",
        "พรสวรรค์",
        "พลานุช",
        "พัชรีนิษฐ์",
        "พันเกล้า",
        "พัสวี",
        "พาดีล๊ะ",
        "พาสุข",
        "พิชญ์สินี",
        "พิมพกานต์",
        "พิมพ์ประภา",
        "พิมพ์พิชญา",
        "พิมพ์สุดา",
        "พิมพ์สุตา",
        "พิไลพร",
        "พิศพรรณ",
        "พีรภัทร์",
        "เพชรมณี",
        "เพ็ญพรรษา",
        "เพ็ญยุภา",
        "เพียงกมล",
        "ฟารินี",
        "ฟิรยา",
        "ภัคชัญญา",
        "ภัคศุภางค์",
        "ภัทรนาฎ",
        "ภัทราวุธ",
        "ภานิณี",
        "ภารวี",
        "ภาสินี",
        "มณียา",
        "มนรัตน์",
        "มนัญชยา",
        "มลิวรรณ",
        "มะลีวัลย์",
        "มัตติกา",
        "มาซีเตาะ",
        "มารีนี",
        "มาสิตะ",
        "เมทนี",
        "เมษา",
        "ยนงคราญ",
        "ยุภา",
        "ยุลิน",
        "เยาวรัตน์",
        "โยธิการ์",
        "รมิตา",
        "รวิวาน",
        "รอกีเย๊าะ",
        "รอซีด๊ะ",
        "รักชนก",
        "รังสินี",
        "ราณี",
        "รูไกยะฮ์",
        "โรสชา",
        "ลักษมี",
        "ลัดดา",
        "วณัฐดา",
        "วนาลี",
        "วรดาพร",
        "วรนาฎ",
        "วรรณกร",
        "วรรณนิสา",
        "วรรณรัตน์",
        "วรรณาต",
        "วสิตา",
        "วันชนก",
        "วัลยา",
        "วิเชียร",
        "วีร์สุดา",
        "ศจีกาญจน์",
        "ศรินยา",
        "ศศิธร",
        "ศศินา",
        "ศศิยา",
        "ศศิรินทร์",
        "ศิริเกศ",
        "ศิริญา",
        "ศิรินันท์",
        "ศุภกรชนา",
        "ศุภนุนาย",
        "สมใจ",
        "สมมล",
        "สราญจิตต์",
        "สโรชา",
        "สหัสมณี",
        "สายสุรีย์",
        "สิราพร",
        "สิริกานต์",
        "สิริลัดดา",
        "สิริ",
        "สุกฤษตา",
        "สุธาวี",
        "สุธินันท์",
        "สุปรานี",
        "สุพัตร",
        "สุพัตรา",
        "สุภัทริดา",
        "สุภาพร",
        "สุภาลินี",
        "สุมัชญา",
        "สุรการณ์",
        "สุรนีย์",
        "โสภณิตา",
        "โสภา",
        "หรรษา",
        "หฤทัย",
        "อณัฐตา",
        "อธิตยา",
        "อเนชา",
        "อรจิรา",
        "อรพิณ",
        "อริสรา",
        "อรุณี",
        "อลิษา",
        "อัญชัญ",
        "อัญชิษฐา",
        "อัญธิกา",
        "อัญพัชร์",
        "อันธิกา",
        "อาซือมะ",
        "อาภัศรา",
        "อารีย์",
        "อาแอเสาะ",
        "อำพร",
        "อำไพ",
        "อุดมลักษณ์",
        "อุลัยพร",
        "อุษณีย์",
        "ฮามีย๊ะ",
    )
    first_names_male = (
        "กรพนธ์",
        "กระสุน",
        "กฤตพร",
        "กฤตเมธ",
        "กวีฉัฏฐ",
        "กษิดิฐ",
        "กิติชัย",
        "กิติวัฒน์",
        "กุลเชษฐ",
        "กุลดิลก",
        "เกริกพล",
        "เกษตร",
        "เกษมชัย",
        "เกียรติก้อง",
        "เกียรติศักดิ์",
        "โกมล",
        "โกวิทย์",
        "ขวัญรุ้ง",
        "เขียว",
        "คมกริบ",
        "คมกฤชญ์",
        "คมสัน",
        "คำปลิว",
        "คำมั่น",
        "จด",
        "จักรกฤนาย",
        "จักรชัย",
        "จักรพันธ์",
        "จำรัส",
        "จิม",
        "จิรวิทย์",
        "จีรยุทธ",
        "เจตธนากร",
        "เจตพินิษฐ์",
        "เจษฎากร",
        "เจษฏาภรณ์",
        "ใจกลาง",
        "ฉลองชัย",
        "เฉลิมพล",
        "เฉลิมรัฐ",
        "เฉลิมรัตน์",
        "ชัชนันท์",
        "ชัชเวศย์",
        "เชิงชาย",
        "โชคภาดล",
        "โชติวุฒิ",
        "ไชยภพ",
        "ซุกรี",
        "ฌาฆีภัตฐ์",
        "ญาณพันธุ์",
        "ฐิติวุฒิ",
        "ณปภัช",
        "ณัฐจศักดิ์",
        "ณัฐศักดิ์",
        "ณิชเชฏฐ์",
        "ดิลก",
        "ตอฮา",
        "ถนอมชัย",
        "เถลิงยศ",
        "ทรรศนชัย",
        "ทวีวัฒน์",
        "ทองรัตน์",
        "ทัตธน",
        "ทินวัฒน์",
        "เทพณรงค์",
        "เทอดศักดิ์",
        "เทียมศักดิ์",
        "ธนกิตต์",
        "ธนนนท์",
        "ธนภณ",
        "ธนวันต์",
        "ธเนษฐ",
        "ธมน",
        "ธราวิทญ์",
        "ธวัศชา",
        "ธารา",
        "ธาเอก",
        "ธีร์ธวันาย",
        "ธีรลักษณ์",
        "ธีรวัช",
        "ธีรวุฒิ",
        "ธีราทัต",
        "นนทกาญจน์",
        "นพ",
        "นภนต์",
        "นัฐพล",
        "นันทวุฒิ",
        "นัสรุน",
        "นาทภูวพัฒน์",
        "นาย",
        "นิชนันท์",
        "นิติ",
        "นิมุ",
        "นิรันดร์",
        "นิรุตต์",
        "เนติลักษณ์",
        "บุญเกิด",
        "บุญญกัลป์",
        "บุญญามี",
        "บุญนพ",
        "บุญเอก",
        "ปฐม",
        "ปรมินทร์",
        "ประเดิม",
        "ประยุทธ์",
        "ประวี",
        "ประสิทธิ์",
        "ประเสริฐ",
        "ปรายกานต์",
        "ปวีณ",
        "ปัณณวัชร",
        "ปัตถพงษ์",
        "ปิยบุตร",
        "ปิยวัจน์",
        "ปิยะนันท์",
        "ปุณณรัตน์",
        "แปลง",
        "ผดุงชาติ",
        "ผดุงพล",
        "พงษ์นเรศ",
        "พลภูมิ",
        "พศร",
        "พัชรพร",
        "พันเทพ",
        "พันธุ์เทพ",
        "พิชาภพ",
        "พิพิธธน",
        "พีรพัฒน์",
        "พีระพงศ์พันธ์",
        "พุทธ",
        "พุทธิพงษ์",
        "เพทาย",
        "ไพสิฐ",
        "ภควัฒน์",
        "ภัคชนน",
        "ภานุพล",
        "ภานุวัตร",
        "ภาสวุฒิ",
        "ภูมิปัญญา",
        "ภูวรา",
        "ภูวฤณ",
        "ภูวัน",
        "ภูวิช",
        "มนัส",
        "มะสูเกียน",
        "มาโนชญ์",
        "มารุด",
        "มูฮัมหมัดอิมรอน",
        "มูฮำมัด",
        "ไมล์",
        "ยศพงศ์",
        "ยศพนต์",
        "ยศวัฒน์",
        "ยอดแมน",
        "ยุศรอน",
        "ยูซุฟ",
        "รชตกร",
        "รภัสพงษ์",
        "รัฐพงษ์",
        "ราชพฤกษ์",
        "ราชันทร์",
        "ราชัน",
        "เรืองเกียรติ",
        "ฤทธิ์ชกร",
        "เลิศเดช",
        "วรปรัชญ์",
        "วรรณชนะชัย",
        "วรศาสส์",
        "วรินทธิ์ธร",
        "วันฉัตร",
        "วัลลภ",
        "วาร์มูฮำหมัด",
        "วาสุเทพ",
        "วิกิจ",
        "วิชชากร",
        "วิชา",
        "วิถี",
        "วิทูลย์",
        "วิพุธ",
        "วิรชัย",
        "วิรศักดิ์",
        "วิสาร",
        "วีรชัย",
        "วีระโชติ",
        "วีระวัฒน์",
        "วุฒิ",
        "ไวพจน์",
        "ศดิศ",
        "ศภัคชคง",
        "ศรลักษณ์",
        "ศรายุธ",
        "ศรีสวัสดิ์",
        "ศิรณัฐ",
        "ศุภชัย",
        "ศุภาศิล",
        "สนั่น",
        "สมเกียรติ",
        "สมนึก",
        "สมปอง",
        "สมพิศ",
        "สมหมาย",
        "สรรเพชญ์",
        "สรายุทธ",
        "สัญชาน",
        "สันชัย",
        "สันติราษฎร์",
        "สิทธัญ",
        "สิทธิชัย",
        "สินสมุทร",
        "สิรวัฒน์",
        "สิริรัตน์",
        "สีหราช",
        "สุชิน",
        "สุทกร",
        "สุทธิณัฐ",
        "สุทธิพจน์",
        "สุพนธ์",
        "สุรธัช",
        "สุรนัย",
        "สุรวัช",
        "สุไฮลัน",
        "เสรี",
        "โสภณ",
        "หรรษธร",
        "หลักทรัพย์",
        "หล้า",
        "หลี",
        "อชิตะวีร์",
        "อณาวิน",
        "อดิสรณ์",
        "อธิวัตร",
        "อนิวัฒน์",
        "อนุบาล",
        "อนุวัช",
        "อภิลักษณ์",
        "อมัด",
        "อรรจน์",
        "อัครพนธ์",
        "อับดุลเลาะห์",
        "อัษฏา",
        "อาฮามัด",
        "อินทรีย์",
        "อิสรันดร์",
        "เอกชัย",
        "เอกวิทย์",
        "เอกอธิพงษ์",
        "เอนกพงศ์",
        "โอภาส",
        "ฮานาฟี",
        "ฮาฟิต",
    )

    first_names = first_names_male + first_names_female
    first_names_nonbinary = first_names_male + first_names_female

    # last name that has given by senior officer
    # http://www.reurnthai.com/index.php?topic=5273.45
    # also partially from
    # https://github.com/PyThaiNLP/pythainlp/blob/dev/pythainlp/corpus/family_names_th.txt
    last_names = (
        "กุมารบุญ",
        "แก้วชลคราม",
        "แก้วอยู่",
        "ขอหมั่นกลาง",
        "ขันธุลา",
        "ขำเอนก",
        "ขุนดำ",
        "เขียวขุ้ย",
        "เขียวอ่อน",
        "คณานุรักษ์",
        "คำลือ",
        "งามพิเชษฐ์",
        "จ้อยนุแสง",
        "จันทา",
        "จันอ้น",
        "เจริญรัมย์",
        "แจ้งสว่าง",
        "ฉัตรอภิเที่ยงค่ำ",
        "ฉัพพรรณธนกูร",
        "ฉายแสง",
        "ฉิมพาลี",
        "ชำนาญวาด",
        "ชุมวระ",
        "เช้าวันดี",
        "ไชยภา",
        "ซาซุม",
        "ซูสารอ",
        "เณรานุสนธิ์",
        "ดวงทับทิม",
        "ด้วงโสน",
        "ดัตพันธุ์",
        "ดาตู",
        "ดาบเงิน",
        "ดาบเพ็ชร์",
        "ดาวกระจาย",
        "ดาวอร่าม",
        "ดำริห์ชอบ",
        "ดิศดใน",
        "ดิสกะประกาย",
        "ดีตพันธุ์",
        "ดุริยพันธุ์",
        "ดุษฎีวนิช",
        "เดชคุ้ม",
        "เดชวา",
        "ตระกูลบุญ",
        "ตระกูลไม้เรียง",
        "ตราชู",
        "ตรีครุธพันธุ์",
        "ตรีเภรินทร์",
        "ตวงทอง",
        "ตวันเยี่ยม",
        "ตะละภัฏ",
        "ตั้งกุลงาม",
        "ตั้งเผ่า",
        "ตั้งรบ",
        "ตัณฑนุช",
        "ตัณสถิตย์",
        "ตันตราจิณ",
        "ตันเผ่า",
        "ตันยา",
        "ติณรัตน์",
        "ติระคมน์",
        "เตชะกำพุ",
        "เตมิยะเดช",
        "แต้กุล",
        "ไตรบรรพ",
        "ถนอมกุลบุตร",
        "ถนอมพลกรัง",
        "ถนอมพล",
        "ถนอมมนุษย์",
        "ถนัดกลึง",
        "ถนัดการเขียน",
        "ถนัดการยนต์",
        "ถนัดเดินข่าว",
        "ถนัดพิมพการ",
        "ถนัดภาษา",
        "ถนัดรบ",
        "ถนัดรักษา",
        "ถนัดหัดถกรรม",
        "ถนัดอักษร",
        "ถนัดอาวุธ",
        "ถนิมมาศ",
        "ถมปัด",
        "ถมังรักษสัตว์",
        "ถ้วนศรี",
        "ถะเกิงชศ",
        "ถาวรรัตน",
        "ถาวระวรณ์",
        "ถาวรายุศม์",
        "ถิรสวัสดิ์",
        "ถุงเงิน",
        "แถมธน",
        "ทรงโกมล",
        "ทรัพย์ธำรงค์",
        "ทรัพย์สาร",
        "ทวนไชย์",
        "ทวนทอง",
        "ทวีเดช",
        "ทศโยธิน",
        "ทหารแท้",
        "ทองแท้",
        "ทองเนื้อดี",
        "ทองประดิฐ",
        "ทองปากน้ำ",
        "ทองลาภ",
        "ทองสินธุ์",
        "ทองสีไพล",
        "ทองสุกเลิศ",
        "ทองอยู่",
        "ทันยุค",
        "ทับทิมไทย",
        "ทัศนสุทธิ",
        "ทำประดู่",
        "ทีฆะ",
        "ทุมะบุตร์",
        "แท่นทอง",
        "ไทไชโย",
        "ไทนิยม",
        "ไทยแท้",
        "ไทยสุชาต",
        "ธนประทีป",
        "ธนรักษ์",
        "ธนูปกรณ์",
        "ธรรมทินนา",
        "ธรรมนิยม",
        "ธรรมเมธา",
        "ธรรมฤดี",
        "ธรรมสถิตไพศาล",
        "ธัญเสถียร",
        "ธัญาโภชน์",
        "ธาราธร",
        "ธีวร",
        "ธุวะนุติ์",
        "ธูปหอม",
        "ธูปะวิโรจน์",
        "เธียรายัน",
        "นกทอง",
        "นครเทพ",
        "นพคเชนทร์",
        "นพตระกูล",
        "นรวิทย์โชติกุล",
        "นฤทุกข์",
        "นฤภัย",
        "นวลฉวี",
        "นวลเพ็ง",
        "นะวะมันดร",
        "นักรบ",
        "นักสำหรวจ",
        "นับเนื่องนอ",
        "นากกนก",
        "นาคพันธุ์",
        "นาควงษ์",
        "นาคสุทิน",
        "นาคะนคร",
        "นาฏคายี",
        "นาถะเดชะ",
        "นาถะพินธุ",
        "นานายน",
        "นามขำ",
        "นามเสวตร",
        "น้ำทิพย์",
        "นำธวัช",
        "นิติสาขา",
        "นิยมเซียม",
        "นิยมธรรม",
        "นิยมสำหรวจ",
        "นิระหานี",
        "นิลวรรณ",
        "นิลวิมล",
        "นิลสลัว",
        "นิลสุวรรณ์",
        "นิลเสนา",
        "นิละทัต",
        "นิษประปัญจ์",
        "นุชแนวนุ่ม",
        "นุตตาร",
        "นุ่มกัน",
        "เนตร์มณี",
        "เนื่องนนท์",
        "เนื้อนุ่ม",
        "แน่นดุจป้อม",
        "แนวพญา",
        "แนวพนิช",
        "บัวเผื่อน",
        "บินดี",
        "บุญญาภิรมย์",
        "บุญญาไลย์",
        "บุญบำรุง",
        "บุญศล",
        "บุญส่ง",
        "บุณยะภาชน์",
        "บุตดา",
        "บุตราช",
        "บุนยะตีรณะ",
        "บุนยะศัพท์",
        "บุนยาภิสนท์",
        "ประจันตะเสน",
        "ปรีชากุลเศรษฐ์",
        "ปานสุวรรณ",
        "ผลบุญ",
        "พงศ์ฉบับนภา",
        "พรมอ่อน",
        "พรรษาสกุล",
        "พรสีมา",
        "พานเกล้า",
        "พีระเพ็ญกุล",
        "เพียยา",
        "โพธิสัตย์",
        "ภูภักดี",
        "มนทอง",
        "มิ่งขวัญ",
        "เมืองสุข",
        "ไม้แดง",
        "ยะผา",
        "ยางสวย",
        "ยาปะโลหิต",
        "เยาวธนโชค",
        "ร่มธิติรัตน์",
        "ราชมณี",
        "เลขะพันธุ์",
        "เลิศกิ่ง",
        "วะคีมัน",
        "วาทา",
        "วิลาสินี",
        "วุฑฒยากร",
        "เวียงจันทึก",
        "ศรทอง",
        "ศรีตะวัน",
        "ศรีธนะเวทย์",
        "ศรีเผด็จ",
        "ศรีวงค์",
        "ศรีสัตย์",
        "ศรีอุ่น",
        "ศาสตร์ศิลป์",
        "ศิวะวรเวท",
        "สงประเสริฐ",
        "สังข์กรด",
        "สันตะวงศ์",
        "สาระพันธ์",
        "สุวรรณหงษ์",
        "ไสยกิจ",
        "หนักแน่น",
        "หนุนสุข",
        "หอมพิกุล",
        "หอมสิน",
        "หิรัญสาลี",
        "แหยมศิริ",
        "อัตตนาถ",
        "อุ่นอก",
        "อุลหัสสา",
    )

    # thai suffix that has given by the king
    # https://th.wikipedia.org/wiki/%E0%B8%99%E0%B8%B2%E0%B8%A1%E0%B8%AA%E0%B8%81%E0%B8%B8%E0%B8%A5%E0%B8%9E%E0%B8%A3%E0%B8%B0%E0%B8%A3%E0%B8%B2%E0%B8%8A%E0%B8%97%E0%B8%B2%E0%B8%99
    suffixes = (
        "ณ กาฬสินธุ์",
        "ณ จัมปาศักดิ์",
        "ณ เชียงใหม่",
        "ณ ตะกั่วทุ่ง",
        "ณ ถลาง",
        "ณ นคร",
        "ณ น่าน",
        "ณ บางช้าง",
        "ณ ป้อมเพชร์",
        "ณ พัทลุง",
        "ณ พิศณุโลก",
        "ณ มโนรม",
        "ณ มหาไชย",
        "ณ ร้อยเอ็จ",
        "ณ ระนอง",
        "ณ ลำปาง",
        "ณ ลำพูน",
        "ณ วิเชียร",
        "ณ สงขลา",
        "ณ หนองคาย",
        "ณ อุบล",
    )