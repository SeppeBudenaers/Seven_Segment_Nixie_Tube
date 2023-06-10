# Seven Segment Nixie Tube
 This repository contains the code and design files for a LED filament seven segment display, designed to resemble a nixie tube. The display can be configured in either common anode or WS2811 mode, providing a modern twist on the classic nixie tube aesthetic. It provides a warm glow to resemble a nixie tube while taking advantage of LED technology. Explore the provided files to build your own LED filament seven segment display and infuse your projects with a touch of vintage charm.
## How to use it 
To configure the LED filament seven segment display to common anode mode, solder the first and second pads of every solder bridge together.

To configure the LED filament seven segment display to WS2811 mode, solder the second and third pads of every solder bridge together.
## Bill of Material
### common anode mode

| Item                                   | Quantity | Link                                                                                                                                                       |
|----------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Glas tube 30x60mm                      | x1       | [AliExpress Link](https://nl.aliexpress.com/item/32813289039.html?spm=a2g0o.order_list.order_list_main.5.21ef79d2e9LWZz&gatewayAdapt=glo2nld)                    |
| Red LED filament                       | x7       | [AliExpress Link](https://nl.aliexpress.com/item/1005003834518235.html?spm=a2g0o.order_list.order_list_main.10.21ef79d2e9LWZz&gatewayAdapt=glo2nld-)              |
| 47 ohm resistors                       | x7       | [LCSC Link](https://www.lcsc.com/product-detail/_UNI-ROYAL-Uniroyal-Elec-_C25315.html)                                                                    |
| 8 2,54mm pinheader reverse bending 90° | x1       | [AliExpress Link](https://nl.aliexpress.com/item/4000660389713.html?spm=a2g0o.productlist.main.5.6b8d804dlred9v&algo_pvid=283ea269-678a-498f-bd60-9fb64c34b0f6&algo_exp_id=283ea269-678a-498f-bd60-9fb64c34b0f6-2&pdp_npi=3%40dis%21EUR%210.67%210.62%21%21%21%21%21%402100b18f16839900715117374d078a%2110000005517155325%21sea%21BE%213754600235&curPageLogUid=IQMuIH5lTEpR) |

### WS2811 mode

| Item                                   | Quantity | Link                                                                                                                                                       |
|----------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Glas tube 30x60mm                      | x1       | [AliExpress Link](https://nl.aliexpress.com/item/32813289039.html?spm=a2g0o.order_list.order_list_main.5.21ef79d2e9LWZz&gatewayAdapt=glo2nld)                    |
| Red LED filament                       | x7       | [AliExpress Link](https://nl.aliexpress.com/item/1005003834518235.html?spm=a2g0o.order_list.order_list_main.10.21ef79d2e9LWZz&gatewayAdapt=glo2nld)              |
| 47 ohm resistor                        | x7       | [LCSC Link](https://www.lcsc.com/product-detail/_UNI-ROYAL-Uniroyal-Elec-_C25315.html)                                                                    |
| 100 ohm resistor                       | x3       | [LCSC Link](https://www.lcsc.com/product-detail/_UNI-ROYAL-Uniroyal-Elec-_C17408.html)                                                                    |
| WS2811                                 | x3       | [LCSC Link](https://www.lcsc.com/product-detail/LED-Drivers_Worldsemi-WS2811_C114581.html)                                                                |
| 8 2,54mm pinheader reverse bending 90° | x1       | [AliExpress Link](https://nl.aliexpress.com/item/4000660389713.html?spm=a2g0o.productlist.main.5.6b8d804dlred9v&algo_pvid=283ea269-678a-498f-bd60-9fb64c34b0f6&algo_exp_id=283ea269-678a-498f-bd60-9fb64c34b0f6-2&pdp_npi=3%40dis%21EUR%210.67%210.62%21%21%21%21%21%402100b18f16839900715117374d078a%2110000005517155325%21sea%21BE%213754600235&curPageLogUid=IQMuIH5lTEpR) |

## todo
[_] Add media.
[_] Write a library for arduino to use my segments in WS2811 mode.
