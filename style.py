from colored import Fore, Back, Style

default: str = f"{Style.reset}{Fore.light_salmon_3a}"

defb: str = f"{Style.reset}{Fore.light_salmon_3a}{Style.bold}"

defbu: str = f"{Style.reset}{Fore.light_salmon_3a}{Style.bold}{Style.underline}"

bold: str = f"{Style.bold}"

bold_res: str = f"{Style.res_bold}"

und: str = f"{Style.underline}"

und_res: str = f"{Style.res_underline}"

b_und: str = f"{Style.bold}{Style.underline}"

inp: str = f"{Fore.cyan}"

err: str = f"{Fore.light_red}"

hp: str = f"{Fore.green}"

hit: str = f"{Fore.red}{Style.bold}{Style.underline}"

