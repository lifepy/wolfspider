# coding=utf-8
huabei = ['beijing','tianjin','hebei','shanxi','neimenggu']
huadong = ['shandong','jiangsu','zhejiang','anhui','jiangxi','fujian','taiwan']
huazhong = ['hunan','hubei','henan']
huanan = ['guangdong','guangxi','hainan']
xinan = ['sichuan','yunnan','guizhou','chongqing','xizang']
xibei = ['']
province_dict = {
    # 华东地区：山东、江苏、浙江、安徽、江西、福建、台湾
    'shandong':( # 山东
        # 济南市 青岛市 淄博市 枣庄市 东营市 烟台市
        'jinan', 'zibo', 'zaozhuang', 'dongying', 'yantai',
        # 潍坊市 济宁市 泰安市 威海市 日照市 莱芜市 临沂市
        'weifang', 'jining', 'taian','weihai','rizhao','laiwu','linyi'
        # 德州市 聊城市 滨州市 菏泽市
        'dezhou', 'liaocheng', 'binzhou','heze'),

    'jiangsu': ( # 江苏
        # 南京市 无锡市 徐州市 常州市 苏州市 南通市
        'nanjing', 'wuxi', 'xuzhou', 'changzhou', 'nantong',
        # 连云港市 淮安市 盐城市 扬州市 镇江市 泰州市 宿迁市
        'lianyungang', 'huaian', 'yancheng', 'zhenjiang', 'taizhou', 'suqian'),

    'shanghai':('shanghai',),

    'zhejiang': ( # 浙江
        # 杭州市 宁波市 温州市 嘉兴市 湖州市 绍兴市
        'hangzhou','ningbo','wenzhou','jiaxing','huzhou','shaoxing',
        # 金华市 衢州市 舟山市 *台州市 丽水市
        'jinhua','quzhou','zhoushan','zhejiangtaizhou','lishui'),
    
    'anhui':( #安徽
        # 合肥市 芜湖市 蚌埠市 淮南市 马鞍山市 淮北市 
        'hefei','wuhu','bangbu','huainan','maanshan','huaibei',
        # 铜陵市 安庆市 黄山市 滁州市 阜阳市 *宿州市 
        'tongling','anqing','huangshan','chuzhou','buyang','anhuisuzhou',
        # 巢湖市 六安市 亳州市(点评不存在) 池州市 宣城市
        'chaohu','liuan','haozhou','chizhou','xuancheng'),

    'jiangxi':( #江西
        # 南昌市 景德镇市 萍乡市 九江市 新余市 鹰潭市 
        'nanchang','jingdezhen','pingxiang','jiujiang','xinyu','yingtan',
        # 赣州市 吉安市 *宜春市 *抚州市 上饶市
        'ganzhou','jian','jiangxiyichun','jiangxifuzhou','shangrao'),

    'fujian':( # 福建
        # 福州市 厦门市 莆田市 三明市 泉州市 漳州市
        'fuzhou', 'xiamen' 'putian', 'sanming', 'quanzhou','zhangzhou'
        # 南平市 龙岩市 宁德市
        'nanping', 'longyan', 'ningde'),

     'taiwan':( 'taiwan', ), # 台湾

    # 华南地区：广东、广西、海南
    'guangdong':(# 广东
         # 广州市 韶关市 深圳市 珠海市 汕头市 佛山市 
         'guangzhou','shaoguan','shenzhen','zhuhai','shantou','foshan',
         # 江门市 湛江市 茂名市 肇庆市 惠州市 梅州市 
         'jiangmen','zhanjiang','maoming','zhaoqing','huizhou','meizhou',
         # 汕尾市 河源市 阳江市 清远市 东莞市 中山市
         'shanwei','heyuan','yangjiang','qingyuan','dongguan','zhongshan'
         # 潮州市 揭阳市 云浮市
         'chaozhou','jieyang','yunfu'),

    'hainan':(# 海南
        # 海口市 三亚市
        'haikou','sanya'),

    'guangxi':( # 广西
        # 南宁市 柳州市 桂林市 梧州市 北海市 防城港市
        'nanning', 'liuzhou', 'guilin' 'wuzhou', 'beihai', 'fangchenggang',
        # 钦州市 贵港市 玉林市 百色市 贺州市 河池市
        'qinzhou', 'guigang', 'yulin', 'baise','hezhou','hechi',
        # 来宾市 崇左市
        'laibin', 'chongzuo'),

    # 华中地区：河南、湖北、湖南
    'henan':(# 河南
        # 郑州市 开封市 洛阳市 平顶山市 安阳市 鹤壁市 
        'zhengzhou','kaifeng','luoyang','pingdingshan','anyang','hebi'
        # 新乡市 焦作市 濮阳市 许昌市 漯河市 三门峡市 
        'xinxiang','jiaozuo','puyang','xuchang','luohe','sanmenxia',
        # 南阳市 商丘市 信阳市 周口市 驻马店市
        'nanyang','shangqiu','yinyang','zhoukou','zhumadian'),

    'hubei':(# 湖北
        # 武汉市 黄石市 十堰市 宜昌市 襄阳市 荆州市 
        'wuhan','huangshi','shiyan','yichang','xiangyang','jingzhou',
        # 荆门市 鄂州市 孝感市 黄冈市 咸宁市 随州市 *恩施州
        'jinmen','ezhou','xiaogan','huanggang','xianning','suizhou','enshizhou'),

    'hunan':(# 湖南
         # 长沙市 株洲市 湘潭市 衡阳市 邵阳市 岳阳市 
         'changsha','zhuzhou','xiangtan','hengyang','zhaoyang','yueyang',
         # 常德市 张家界市 益阳市 郴州市 永州市 怀化市 娄底市 湘西州
         'changde','zhangjiajie','yiyang','chenzhou','yongzhou','huaihua','loudi','xiangxi'),

    # 西南地区：四川、云南、贵州、重庆、西藏
    'sichuan':(# 四川
        # 成都市 自贡市 攀枝花市 泸州市 德阳市 绵阳市 
        'chengdu','zigong','panzhihua','luzhou','deyang','mianyang',
        # 广元市 遂宁市 内江市 乐山市 南充市 眉山市
        'guangyuan','suining','neijiang','leshan','nanchong','meishan',
        # 宜宾市 广安市 达州市 雅安市 巴中市 资阳市 阿坝州 甘孜州 凉山州
        'yibin','guangan','dazhou','yaan','bazhong','ziyang','aba','ganzi','liangshan'),

    'yunnan':(# 云南
        # 昆明市 曲靖市 玉溪市 保山市 昭通市 丽江市 
        'kunming','qujing','yuxi','baoshan','zhaotong','lijiang',
        # 普洱市（点评不存在） 临沧市 楚雄州 红河州 文山州 西双版纳州 
        'linchang','chuxiong','honghe','wenshan','xishuangbanna',
        # *大理州 德宏州 怒江州 迪庆州
        'dalizhou','dehong','nujiang','diqing'),

    'guizhou':(# 贵州
        # 贵阳市 六盘水市 遵义市 安顺市 *铜仁地区 黔西南州 *毕节地区 黔东南州 黔南州
        'guiyang','liupanshui','zunyi','anshun','tongrendiqu','bijiediqu','qianxinan','qiandongnan','qiannan'),

    'chongqing':('chongqing',),

    'xizang':(# 西藏
        # 拉萨市 *昌都地区 山南地区 *日喀则地区 那曲地区 阿里地区 林芝地区
        'lasa','changdudiqu','shannan','rikazediqu','naqu','ali','linzhi'),

    # 华北地区：北京、天津、河北、山西、内蒙古
    'beijing':('beijing',),
    'tianjin':('tianjing',),
    
    'hebei':(# 河北
        # 石家庄市 唐山市 秦皇岛市 邯郸市 邢台市 保定市 
        'shijiazhuang','tangshan','qinghuangdao','handan','xingtai','baoding',
        # 张家口市 承德市 沧州市 廊坊市 衡水市
        'zhangjiakou','chengde','cangzhou','langfang','hengshui'),

    'shanxi':(# 山西
        # 太原市 大同市 阳泉市 长治市 晋城市 朔州市 
        'taiyuan','datong','yangquan','changzhi','jincheng','shuozhou',
        # 晋中市 运城市 忻州市 临汾市 吕梁市
        'jinzhong','yuncheng','xinzhou','linfen','lvliang'),
    
    'neimenggu':(# 内蒙古
        # 呼和浩特市 包头市 乌海市 赤峰市 通辽市 鄂尔多斯市 
        'huhehaote','baotou','wuhai','chifeng','tongliao','eerduosi',
        # 呼伦贝尔市 巴彦淖尔市 乌兰察布市 兴安盟 锡林郭勒盟 阿拉善盟
        'hulunbeier','bamunaoer','wulanchabu','xingan','xilinguole','alashan'),

    # 直辖市
}
