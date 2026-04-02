from colorama import Fore, init,Back,Style
import random
from rich.console import Console
from rich.panel import Panel
# init() #to initialize colorama
console = Console()

console.print("Welcom To Guess The Number Game",style="bold green")


while True:
    #choose difficulty
    console.print(f"[blue]Diffculty levels[/blue]")
    console.print("[blue]Easy(E) 1-50 / Medium(M) 1-100/ Hard(H) 1-500[/blue]")
    N=0
    while N==0:
        lvl= input("Enter the diffculty level:")
        if lvl == 'E' or lvl=='e':
            N=50
        elif lvl=='M'or lvl =='m':
            N=100
        elif lvl == 'H' or lvl =='h':
            N = 500
        else:
            console.print("[red]Invalid input[/red]")
    


    real_num = random.randint(1,N)
    attempts = 0
    num=0
    while num != real_num:
        
        try:
            num=int(input("Guess the number(integer): "))
        except ValueError as e:
            console.print("[red]Enter integer value only[/red]")
        else:
            attempts+=1 
            if num < real_num:
                console.print("[yellow]Too LOW[/yellow]")
            
            elif num > real_num:
                console.print("[red]Too high[/red]")
        
        
    console.print("[cyan bold]YAYY Number Guessed!![/bold cyan]")
    console.print("No of attempts",attempts)
 
    ch=input("play again (Y/N)?")
    ch = ch.upper()
    if ch =='N':
        break

