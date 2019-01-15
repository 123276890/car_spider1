# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    carBrand = scrapy.Field()                      # 车品牌
    cars = scrapy.Field()                          # 车系
    link = scrapy.Field()                          # 链接
    carName = scrapy.Field()                       # 车名字
    modelLevel = scrapy.Field()                    # 车型级别
    bodyForm = scrapy.Field()                      # 车身形式
    bodySize = scrapy.Field()                      # 车身尺寸
    combined = scrapy.Field()                      # 综合油耗
    EPStandard = scrapy.Field()                    # 环保标准
    engine = scrapy.Field()                        # 发动机
    driveAndGearbox = scrapy.Field()               # 驱动及变速箱
    mostPowerful = scrapy.Field()                  # 最大功率
    carId = scrapy.Field()                         # 车id
    slowtime = scrapy.Field()                      # 慢充时间
    quicktime = scrapy.Field()                     # 快充时间
    quickpercent = scrapy.Field()                  # 快充百分比
    settings = scrapy.Field()
    type_id = scrapy.Field()                       # 汽车之家车型id' == carId
    car_name = scrapy.Field()
    car_type = scrapy.Field()                      # 0/1是否显示电动机表
    series_name = scrapy.Field()                   # 车系名称
    series_id = scrapy.Field()                     # 车系id
    brand_name = scrapy.Field()                    # 品牌名称
    produce_type_str = scrapy.Field()              # 生产方式
    manufacturer = scrapy.Field()                  # 厂商
    car_level_str = scrapy.Field()                 # 级别
    market_price_str = scrapy.Field()              # 厂商指导价
    energy_type_str = scrapy.Field()               # 能源类型
    market_time = scrapy.Field()                   # 上市时间
    gearbox = scrapy.Field()                       # 变速箱
    car_size = scrapy.Field()                      # 长*宽*高(mm)
    car_struct = scrapy.Field()                    # 车身结构
    max_speed = scrapy.Field()                     # 最高车速(km/h)
    official_speedup = scrapy.Field()              # 官方0-100km/h加速(s)
    actual_speedup = scrapy.Field()                # 实测0-100km/h加速(s)
    actual_brake = scrapy.Field()                  # 实测100-0km/h制动(m)
    actual_fueluse = scrapy.Field()                # 实测油耗(L/100km)
    gerenal_fueluse = scrapy.Field()               # 工信部综合油耗(L/100km)
    actual_ground = scrapy.Field()                 # 实测离地间隙(mm)
    quality_guarantee = scrapy.Field()             # 整车质保
    max_power = scrapy.Field()                     # 最大功率(kW)
    max_torque = scrapy.Field()                    # 最大扭矩(N・m)
    e_mileage = scrapy.Field()                     # 工信部纯电续驶里程(km)
    length = scrapy.Field()                        # 长度(mm)
    width = scrapy.Field()                         # 宽度(mm)
    height = scrapy.Field()                        # 高度(mm)
    shaft_distance = scrapy.Field()                # 轴距(mm)
    front_wheels_gap = scrapy.Field()              # 前轮距(mm)
    back_wheels_gap = scrapy.Field()               # 后轮距(mm)
    min_ground = scrapy.Field()                    # 最小离地间隙(mm)
    body_struct = scrapy.Field()                   # 车身结构
    doors = scrapy.Field()                         # 车门数(个)
    seats = scrapy.Field()                         # 座位数(个)
    fuel_vol = scrapy.Field()                      # 油箱容积(L)
    cargo_vol = scrapy.Field()                     # 行李厢容积(L)
    open_type = scrapy.Field()                     # 后排车门开启方式
    cargo_size = scrapy.Field()                    # 货箱尺寸(mm)
    total_weight = scrapy.Field()                  # 整备质量(kg)
    carry_cap = scrapy.Field()                     # 最大载重质量(kg)
    engine_type = scrapy.Field()                   # 发动机型号
    cc = scrapy.Field()                            # 排量(mL)
    air_intake = scrapy.Field()                    # 进气形式
    cylinder_arrange = scrapy.Field()              # 气缸排列形式
    cylinders = scrapy.Field()                     # 气缸数(个)
    valves = scrapy.Field()                        # 每缸气门数(个)
    compress_rate = scrapy.Field()                 # 压缩比
    valve_machanism = scrapy.Field()               # 配气机构
    cylinder_radius = scrapy.Field()               # 缸径(mm)
    stroke = scrapy.Field()                        # 行程(mm)
    engine_hp = scrapy.Field()                     # 最大马力(Ps)
    engine_power = scrapy.Field()                  # 最大功率(kW)
    engine_rpm = scrapy.Field()                    # 最大功率转速(rpm)
    engine_torque = scrapy.Field()                 # 最大扭矩(N・m)
    torque_rpm = scrapy.Field()                    # 最大扭矩转速(rpm)
    tech_spec = scrapy.Field()                     # 发动机特有技术
    engine_energy = scrapy.Field()                 # 燃料形式
    roz = scrapy.Field()                           # 燃油标号
    oil_drive = scrapy.Field()                     # 供油方式
    cylinder_cover = scrapy.Field()                # 缸盖材料
    cylinder_body = scrapy.Field()                 # 缸体材料
    environmental_standard = scrapy.Field()        # 环保标准
    motor_type = scrapy.Field()                    # 电机类型
    motor_power = scrapy.Field()                   # 电动机总功率(kW)
    motor_torque = scrapy.Field()                  # 电动机总扭矩(N・m)
    motor_front_power = scrapy.Field()             # 前电动机最大功率(kW)
    motor_front_torque = scrapy.Field()            # 前电动机最大扭矩(N・m)
    motor_back_power = scrapy.Field()              # 后电动机最大功率(kW)
    motor_back_torque = scrapy.Field()             # 后电动机最大扭矩(N・m)
    sys_power = scrapy.Field()                     # 系统综合功率(kW)
    sys_torque = scrapy.Field()                    # 系统综合扭矩(N・m)
    motor_num = scrapy.Field()                     # 驱动电机数
    motor_arrange = scrapy.Field()                 # 电机布局
    bat_type = scrapy.Field()                      # 电池类型
    mileage = scrapy.Field()                       # 工信部续航里程(km)
    bat_cap = scrapy.Field()                       # 电池容量(km)
    bat_use = scrapy.Field()                       # 百公里耗电量(kWh/100km)
    bat_guarantee = scrapy.Field()                 # 电池组质保
    bat_charge = scrapy.Field()                    # 电池充电时间
    fast_charge = scrapy.Field()                   # 快充电量(%)
    charge_pile_price = scrapy.Field()             # 充电桩价格
    gearbox_name = scrapy.Field()                  # 简称
    gears_num = scrapy.Field()                     # 挡位个数
    gears_type = scrapy.Field()                    # 变速箱类型
    drive_type = scrapy.Field()                    # 驾驶类型：手动，自动
    drive_method = scrapy.Field()                  # 驱动方式
    susp_front_type = scrapy.Field()               # 前悬架类型
    susp_back_type = scrapy.Field()                # 后悬架类型
    assist_type = scrapy.Field()                   # 助力类型
    structure = scrapy.Field()                     # 车体结构
    four_wheel_drive = scrapy.Field()              # 四驱形式
    central_diff = scrapy.Field()                  # 中央差速器结构
    front_brake = scrapy.Field()                   # 前制动器类型
    back_brake = scrapy.Field()                    # 后制动器类型
    park_brake = scrapy.Field()                    # 驻车制动类型
    front_wheel_size = scrapy.Field()              # 前轮胎规格
    back_wheel_size = scrapy.Field()               # 后轮胎规格
    backup_wheel = scrapy.Field()                  # 备胎规格
    seat_srs = scrapy.Field()                      # 主/副驾驶座安全气囊
    side_airbag = scrapy.Field()                   # 前/后排侧气囊
    head_srs = scrapy.Field()                      # 前/后排头部气囊(气帘)
    knee_srs = scrapy.Field()                      # 膝部气囊
    tire_pres_monitor = scrapy.Field()             # 胎压监测装置
    zero_tire_pres = scrapy.Field()                # 零胎压继续行驶
    unbelt_notice = scrapy.Field()                 # 安全带未系提示
    isofix = scrapy.Field()                        # ISOFIX儿童座椅接口
    anti_lock = scrapy.Field()                     # ABS防抱死
    bfd = scrapy.Field()                           # 制动力分配(EBD/CBC等)
    bas = scrapy.Field()                           # 刹车辅助(EBA/BAS/BA等)
    tcs = scrapy.Field()                           # 牵引力控制(ASR/TCS/TRC等)
    stable_control = scrapy.Field()                # 车身稳定控制(ESC/ESP/DSC等)
    bsa = scrapy.Field()                           # 并线辅助
    ldw = scrapy.Field()                           # 车道偏离预警系统
    abs = scrapy.Field()                           # 主动刹车/主动安全系统
    nvs = scrapy.Field()                           # 夜视系统
    tired_drive = scrapy.Field()                   # 疲劳驾驶提示
    radar = scrapy.Field()                         # 前/后驻车雷达
    reverse_video = scrapy.Field()                 # 倒车视频影像
    panorama = scrapy.Field()                      # 全景摄像头
    cruise_ctrl = scrapy.Field()                   # 定速巡航
    self_adpt_cruise = scrapy.Field()              # 自适应巡航
    auto_park_in = scrapy.Field()                  # 自动泊车入位
    engine_start_stop = scrapy.Field()             # 发动机启停技术
    auto_drive = scrapy.Field()                    # 自动驾驶技术
    hac = scrapy.Field()                           # 上坡辅助
    auto_park = scrapy.Field()                     # 自动驻车
    hdc = scrapy.Field()                           # 陡坡缓降
    variable_susp = scrapy.Field()                 # 可变悬架
    air_susp = scrapy.Field()                      # 空气悬架
    e_susp = scrapy.Field()                        # 电磁感应悬架
    vgrs = scrapy.Field()                          # 可变转向比
    front_diff_lock = scrapy.Field()               # 前桥限滑差速器/差速锁
    central_diff_lock = scrapy.Field()             # 中央差速器锁止功能
    back_diff_lock = scrapy.Field()                # 后桥限滑差速器/差速锁
    ads = scrapy.Field()                           # 整体主动转向系统
    e_sunroof = scrapy.Field()                     # 电动天窗
    pano_sunroof = scrapy.Field()                  # 全景天窗
    sunroofs = scrapy.Field()                      # 多天窗
    sport_package = scrapy.Field()                 # 运动外观套件
    alloy_wheel = scrapy.Field()                   # 铝合金轮圈
    e_suction_door = scrapy.Field()                # 电动吸合门
    slide_door = scrapy.Field()                    # 侧滑门
    e_cargo = scrapy.Field()                       # 电动后备厢
    react_cargo = scrapy.Field()                   # 感应后备厢
    roof_rack = scrapy.Field()                     # 车顶行李架
    engine_e_guard = scrapy.Field()                # 发动机电子防盗
    e_ctrl_lock = scrapy.Field()                   # 车内中控锁
    remote_key = scrapy.Field()                    # 遥控钥匙
    keyless_start = scrapy.Field()                 # 无钥匙启动系统
    keyless_enter = scrapy.Field()                 # 无钥匙进入系统
    remote_start = scrapy.Field()                  # 远程启动
    leather_steering = scrapy.Field()              # 皮质方向盘
    steer_adjt = scrapy.Field()                    # 方向盘调节
    steer_e_adjt = scrapy.Field()                  # 方向盘电动调节
    functional_steer = scrapy.Field()              # 多功能方向盘
    steer_shift = scrapy.Field()                   # 方向盘换挡
    steer_heat = scrapy.Field()                    # 方向盘加热
    steer_mem = scrapy.Field()                     # 方向盘记忆
    computer_scr = scrapy.Field()                  # 行车电脑显示屏
    lcd_panel = scrapy.Field()                     # 全液晶仪表盘
    hud = scrapy.Field()                           # HUD抬头数字显示
    car_dvr = scrapy.Field()                       # 内置行车记录仪
    anc = scrapy.Field()                           # 主动降噪
    wireless_charge = scrapy.Field()               # 手机无线充电
    seat_mat = scrapy.Field()                      # 座椅材质
    sport_seat = scrapy.Field()                    # 运动风格座椅
    height_adjt = scrapy.Field()                   # 座椅高低调节
    lumbar_support = scrapy.Field()                # 腰部支撑调节
    shoulder_support = scrapy.Field()              # 肩部支撑调节
    seat_e_adjt = scrapy.Field()                   # 主/副驾驶座电动调节
    snd_backrest_adjt = scrapy.Field()             # 第二排靠背角度调节
    snd_seat_mv = scrapy.Field()                   # 第二排座椅移动
    back_seat_adjt = scrapy.Field()                # 后排座椅电动调节
    vice_adjt_btn = scrapy.Field()                 # 副驾驶位后排可调节按钮
    e_seat_mem = scrapy.Field()                    # 电动座椅记忆
    seat_heat = scrapy.Field()                     # 前/后排座椅加热
    seat_vent = scrapy.Field()                     # 前/后排座椅通风
    seat_masg = scrapy.Field()                     # 前/后排座椅按摩
    snd_row_seat = scrapy.Field()                  # 第二排独立座椅
    third_row_seat = scrapy.Field()                # 第三排座椅
    back_seat_down = scrapy.Field()                # 后排座椅放倒方式
    handrail = scrapy.Field()                      # 前/后中央扶手
    back_cup_hold = scrapy.Field()                 # 后排杯架
    heat_cold_cup = scrapy.Field()                 # 可加热/制冷杯架
    gps = scrapy.Field()                           # GPS导航系统
    gps_interact = scrapy.Field()                  # 定位互动服务
    colorful_scr = scrapy.Field()                  # 中控台彩色大屏
    colorful_scr_size = scrapy.Field()             # 中控台彩色大屏尺寸
    lcd_sep = scrapy.Field()                       # 中控液晶屏分屏显示
    blueteeth = scrapy.Field()                     # 蓝牙/车载电话
    mobile_map = scrapy.Field()                    # 手机互联/映射
    network = scrapy.Field()                       # 车联网
    television = scrapy.Field()                    # 车载电视
    back_lcd = scrapy.Field()                      # 后排液晶屏
    back_power_supply = scrapy.Field()             # 220V/230V电源
    external_audio = scrapy.Field()                # 外接音源接口
    cddvd = scrapy.Field()                         # CD/DVD
    speaker_brand = scrapy.Field()                 # 扬声器品牌
    speaker_num = scrapy.Field()                   # 扬声器数量
    low_beam = scrapy.Field()                      # 近光灯
    high_beam = scrapy.Field()                     # 远光灯
    led_beam = scrapy.Field()                      # LED日间行车灯
    adaptive_beam = scrapy.Field()                 # 自适应远近光
    head_light = scrapy.Field()                    # 自动头灯
    turn_light = scrapy.Field()                    # 转向辅助灯
    turn_head_light = scrapy.Field()               # 转向头灯
    front_fog_lamp = scrapy.Field()                # 前雾灯
    light_height_adjt = scrapy.Field()             # 大灯高度可调
    light_clean_dev = scrapy.Field()               # 大灯清洗装置
    mood_light = scrapy.Field()                    # 车内氛围灯
    power_window = scrapy.Field()                  # 前/后电动车窗
    e_lift_window = scrapy.Field()                 # 车窗一键升降
    anti_pinch_hand = scrapy.Field()               # 车窗防夹手功能
    insulating_glass = scrapy.Field()              # 防紫外线/隔热玻璃
    e_adjt_rearview = scrapy.Field()               # 后视镜电动调节
    heat_rearview = scrapy.Field()                 # 后视镜加热
    dimming_mirror = scrapy.Field()                # 内/外后视镜自动防眩目
    stream_media_rearview = scrapy.Field()         # 流媒体车内后视镜
    power_mirror = scrapy.Field()                  # 后视镜电动折叠
    mirror_mem = scrapy.Field()                    # 后视镜记忆
    abat_vent = scrapy.Field()                     # 后风挡遮阳帘
    side_abat_vent = scrapy.Field()                # 后排侧遮阳帘
    side_priv_glass = scrapy.Field()               # 后排侧隐私玻璃
    sun_shield = scrapy.Field()                    # 遮阳板化妆镜
    back_wiper = scrapy.Field()                    # 后雨刷
    react_wiper = scrapy.Field()                   # 感应雨刷
    air_type = scrapy.Field()                      # 空调控制方式
    back_air = scrapy.Field()                      # 后排独立空调
    back_outlet = scrapy.Field()                   # 后座出风口
    temper_zone_ctrl = scrapy.Field()              # 温度分区控制
    air_adjt = scrapy.Field()                      # 车内空气调节/花粉过滤
    air_cleaner = scrapy.Field()                   # 车载空气净化器
    car_fridge = scrapy.Field()                    # 车载冰箱
    car_highlights = scrapy.Field()                # 车型亮点

    pass

